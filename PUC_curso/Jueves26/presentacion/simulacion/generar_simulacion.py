"""Entrena una red pequeña y exporta una demostración sin dependencias de red.

Ejecutar desde cualquier carpeta con NumPy, Matplotlib y Pillow instalados.
El HTML reproduce estados reales; no sustituye predicciones por x**2.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

BASE = Path(__file__).resolve().parent
FIGURAS = BASE.parent / "figuras"
EPOCAS = 12_000
TASA = 0.02
SEMILLA = 7
AZUL, VERDE, NARANJA = "#12315a", "#087f6b", "#d65324"


def inicializar():
    rng = np.random.RandomState(SEMILLA)
    return np.r_[rng.normal(0, 0.8, 6), rng.normal(0, 0.3, 6),
                 rng.normal(0, 0.5, 6), 0.0]


def predecir(x, parametros):
    """Una entrada, seis neuronas tanh y una salida afín (19 parámetros)."""
    w, b, v, c = parametros[:6], parametros[6:12], parametros[12:18], parametros[18]
    activaciones = np.tanh(np.asarray(x)[..., None] * w + b)
    return activaciones @ v + c


def perdida_y_gradiente(x, y, parametros):
    w, b, v, c = parametros[:6], parametros[6:12], parametros[12:18], parametros[18]
    a = np.tanh(x[:, None] * w + b)
    error = a @ v + c - y
    d_salida = 2 * error / len(x)
    d_z = d_salida[:, None] * v * (1 - a * a)
    gradiente = np.r_[np.sum(d_z * x[:, None], axis=0),
                      d_z.sum(axis=0), a.T @ d_salida, d_salida.sum()]
    return np.mean(error * error), gradiente


def verificar_gradiente(x, y):
    """Contrasta las 19 derivadas analíticas con diferencias centrales."""
    parametros = inicializar()
    _, analitico = perdida_y_gradiente(x, y, parametros)
    numerico = np.zeros_like(parametros)
    h = 1e-6
    for j in range(len(parametros)):
        mas, menos = parametros.copy(), parametros.copy()
        mas[j] += h
        menos[j] -= h
        numerico[j] = (np.mean((predecir(x, mas) - y) ** 2)
                       - np.mean((predecir(x, menos) - y) ** 2)) / (2 * h)
    np.testing.assert_allclose(analitico, numerico, rtol=1e-5, atol=1e-7)


def entrenar():
    x = np.linspace(-2, 2, 21)
    # La regla del cuadrado solo genera las etiquetas de referencia.
    y = x ** 2
    verificar_gradiente(x, y)
    parametros = inicializar()
    estados, perdidas = [], []
    guardar = set(range(0, 1001, 20)) | set(range(1120, EPOCAS, 120)) | {EPOCAS}
    peso_lineal, sesgo_lineal = 0.5, 0.0
    for epoca in range(EPOCAS + 1):
        perdida, gradiente = perdida_y_gradiente(x, y, parametros)
        perdidas.append(float(perdida))
        if epoca in guardar:
            estados.append({
                "epoca": epoca,
                "parametros": parametros.round(10).tolist(),
                "mse": float(perdida),
                "lineal": [float(peso_lineal), float(sesgo_lineal)],
            })
        if epoca < EPOCAS:
            # Todos los gradientes se calculan antes de cambiar los parámetros.
            parametros -= TASA * gradiente
            error_lineal = peso_lineal * x + sesgo_lineal - y
            peso_lineal -= TASA * 2 * np.mean(error_lineal * x)
            sesgo_lineal -= TASA * 2 * np.mean(error_lineal)

    # Una malla diferente comprueba interpolación fuera de los puntos entrenados.
    x_nuevos = np.linspace(-1.99, 1.99, 400)
    x_nuevos = x_nuevos[~np.any(np.isclose(x_nuevos[:, None], x), axis=1)]
    mse_nuevos = float(np.mean((predecir(x_nuevos, parametros) - x_nuevos ** 2) ** 2))
    assert not np.any(np.isclose(x, 1.5))
    assert np.all(np.isfinite(perdidas))
    assert perdidas[-1] < 0.005 and perdidas[-1] < perdidas[0] / 100
    assert mse_nuevos < 0.005
    assert abs(float(predecir(1.5, parametros)) - 2.25) < 0.1
    np.testing.assert_allclose([peso_lineal, sesgo_lineal], [0, np.mean(y)], atol=1e-10)
    resumen = {
        "epocas": EPOCAS, "tasa": TASA, "semilla": SEMILLA,
        "arquitectura": [1, 6, 1], "parametros_entrenables": 19,
        "mse_inicial": perdidas[0], "mse_final": perdidas[-1],
        "mse_malla_nueva": mse_nuevos, "entrada_reservada": 1.5,
        "prediccion_reservada": float(predecir(1.5, parametros)),
        "referencia_reservada": 2.25,
        "mse_lineal_final": float(np.mean((peso_lineal * x + sesgo_lineal - y) ** 2)),
        "gradiente_verificado": True,
    }
    trayectoria = {"x": x.tolist(), "y": y.tolist(), "estados": estados,
                   "resumen": resumen}
    return trayectoria


def exportar_figuras(trayectoria):
    FIGURAS.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.labelcolor": AZUL, "text.color": AZUL,
        "axes.titlecolor": AZUL, "axes.grid": True, "grid.alpha": 0.15,
        "pdf.fonttype": 42,
    })
    xs = np.linspace(-2, 2, 250)
    estados = trayectoria["estados"]
    fig, ejes = plt.subplots(1, 3, figsize=(12.4, 3.3), layout="constrained")
    for ax, epoca in zip(ejes, [0, 500, EPOCAS]):
        estado = next(e for e in estados if e["epoca"] == epoca)
        p = np.array(estado["parametros"])
        ax.plot(xs, xs ** 2, "--", color="0.55", lw=1.5, label="Referencia x²")
        ax.scatter(trayectoria["x"], trayectoria["y"], color=AZUL, s=18, label="Datos")
        ax.plot(xs, predecir(xs, p), color=VERDE, lw=2.3, label="Red")
        ax.scatter([1.5], [predecir(1.5, p)], color=NARANJA, marker="D", s=40, zorder=5)
        ax.set(xlim=(-2.1, 2.1), ylim=(-0.7, 4.5), xlabel="Entrada x", ylabel="Salida")
        ax.set_title(f"Época {epoca:,}\nMSE = {estado['mse']:.4f}")
    ejes[0].legend(fontsize=8, loc="upper center")
    fig.savefig(FIGURAS / "simulacion_cuadrado.pdf", bbox_inches="tight")
    plt.close(fig)

    fig, (ax, ax_error) = plt.subplots(1, 2, figsize=(10.4, 4.5),
                                     gridspec_kw={"width_ratios": [1.65, 1]}, layout="constrained")
    ax.plot(xs, xs ** 2, "--", color="0.55", lw=1.4, label="Referencia x²")
    ax.scatter(trayectoria["x"], trayectoria["y"], color=AZUL, s=20, label="Datos de entrenamiento")
    linea, = ax.plot([], [], color=VERDE, lw=2.5, label="Predicción de la red")
    consulta, = ax.plot([], [], "D", color=NARANJA, ms=7, label="Entrada nueva: 1.5")
    ax.set(xlim=(-2.1, 2.1), ylim=(-0.7, 4.5), xlabel="Entrada x", ylabel="Salida")
    ax.legend(fontsize=8)
    traza, = ax_error.plot([], [], color=VERDE, lw=2)
    ax_error.set(xlim=(0, EPOCAS), ylim=(0.002, 6), yscale="log",
                 xlabel="Época", ylabel="MSE de entrenamiento")
    texto = fig.suptitle("")

    def actualizar(i):
        estado = estados[i]
        p = np.array(estado["parametros"])
        linea.set_data(xs, predecir(xs, p))
        consulta.set_data([1.5], [float(predecir(1.5, p))])
        traza.set_data([e["epoca"] for e in estados[:i + 1]], [e["mse"] for e in estados[:i + 1]])
        texto.set_text(f"Red 1–6–1 · Época {estado['epoca']} · "
                       f"ŷ(1.5) = {predecir(1.5, p):.3f} · referencia = 2.25")
        return linea, consulta, traza, texto

    animacion = FuncAnimation(fig, actualizar, frames=len(estados), interval=100, blit=False)
    animacion.save(BASE / "entrenamiento_cuadrado.gif", writer=PillowWriter(fps=10), dpi=85)
    plt.close(fig)


def main():
    trayectoria = entrenar()
    datos = json.dumps(trayectoria, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    plantilla = (BASE / "plantilla.html").read_text(encoding="utf-8")
    assert plantilla.count("__TRAYECTORIA_JSON__") == 1
    (BASE / "simulacion_cuadrado.html").write_text(
        plantilla.replace("__TRAYECTORIA_JSON__", datos), encoding="utf-8")
    (BASE / "resumen.json").write_text(
        json.dumps(trayectoria["resumen"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (BASE / "trayectoria.json").write_text(datos + "\n", encoding="utf-8")
    exportar_figuras(trayectoria)
    r = trayectoria["resumen"]
    (FIGURAS / "simulacion_resultados.tex").write_text(
        "% Valores obtenidos del entrenamiento, generados automáticamente.\n"
        f"\\newcommand{{\\prediccionCuadrado}}{{{r['prediccion_reservada']:.3f}}}\n"
        f"\\newcommand{{\\mseCuadrado}}{{{r['mse_final']:.4f}}}\n", encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print(f"Estados exportados: {len(trayectoria['estados'])}")


if __name__ == "__main__":
    main()
