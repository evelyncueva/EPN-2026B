"""Genera la secuencia una entrada → dos entradas → red no lineal.

La etapa económica tiene dos variables explicativas y una sola salida.
Los hogares son observaciones sintéticas, no estimaciones sobre hogares reales.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent
FIGURAS = BASE.parent / "figuras"


def predecir(x, parametros):
    p = np.asarray(parametros).reshape(-1, 2)
    return np.asarray(x)[..., None] * p[:, 0] + p[:, 1]


def perdida_y_gradiente(x, y, parametros):
    error = predecir(x, parametros) - y
    # El MSE promedia observaciones y salidas. Cada neurona es independiente.
    factor = 2 / error.size
    gradiente = np.column_stack((factor * (error * x[:, None]).sum(axis=0),
                                 factor * error.sum(axis=0))).ravel()
    return float(np.mean(error ** 2)), gradiente


def entrenar(salidas):
    x = np.linspace(-2, 2, 21)
    y = np.column_stack((2 * x + 1, -x + 2))[:, :salidas]
    parametros = np.array([-0.5, 0.0, 0.5, -1.0])[:2 * salidas].copy()
    _, gradiente = perdida_y_gradiente(x, y, parametros)
    numerico = []
    for j in range(len(parametros)):
        mas, menos = parametros.copy(), parametros.copy()
        mas[j] += 1e-6
        menos[j] -= 1e-6
        numerico.append((np.mean((predecir(x, mas) - y) ** 2)
                         - np.mean((predecir(x, menos) - y) ** 2)) / 2e-6)
    np.testing.assert_allclose(gradiente, numerico, rtol=1e-5, atol=1e-7)

    guardar = set(range(0, 11)) | set(range(15, 101, 5)) | set(range(120, 401, 20))
    estados = []
    for epoca in range(401):
        perdida, gradiente = perdida_y_gradiente(x, y, parametros)
        if epoca in guardar:
            estados.append({"epoca": epoca, "mse": perdida,
                            "parametros": parametros.tolist()})
        if epoca < 400:
            parametros -= 0.05 * gradiente

    objetivo = np.array([2, 1, -1, 2])[:2 * salidas]
    np.testing.assert_allclose(parametros, objetivo, atol=1e-7)
    assert estados[-1]["mse"] < 1e-15
    assert not np.any(np.isclose(x, 1.5))
    # Los coeficientes también se contrastan con mínimos cuadrados.
    solucion = np.linalg.lstsq(np.column_stack((x, np.ones_like(x))), y, rcond=None)[0].T.ravel()
    np.testing.assert_allclose(parametros, solucion, atol=1e-7)
    resumen = {"salidas": salidas, "parametros_entrenables": 2 * salidas,
               "epocas": 400, "tasa": 0.05,
               "mse_inicial": estados[0]["mse"], "mse_final": estados[-1]["mse"],
               "parametros_finales": parametros.tolist(),
               "entrada_reservada": 1.5, "prediccion_reservada": predecir(1.5, parametros).tolist(),
               "gradiente_verificado": True}
    return {"salidas": salidas, "x": x.tolist(), "y": y.tolist(),
            "estados": estados, "resumen": resumen}


def entrenar_multivariable():
    # Ingreso expresado en miles de unidades monetarias; personas por hogar.
    x = np.array([(ingreso, personas) for ingreso in [1, 1.5, 2, 3, 4]
                  for personas in [1, 2, 3, 4, 5]], dtype=float)
    matriz = np.column_stack((x, np.ones(len(x))))
    referencia = np.array([60.0, 40.0, 50.0])
    y = matriz @ referencia
    parametros = np.array([10.0, 10.0, 0.0])

    def perdida(p):
        return float(np.mean((matriz @ p - y) ** 2))

    gradiente = 2 * matriz.T @ (matriz @ parametros - y) / len(y)
    numerico = []
    for j in range(3):
        mas, menos = parametros.copy(), parametros.copy()
        mas[j] += 1e-5
        menos[j] -= 1e-5
        numerico.append((perdida(mas) - perdida(menos)) / 2e-5)
    np.testing.assert_allclose(gradiente, numerico, rtol=1e-6, atol=1e-5)
    assert np.linalg.matrix_rank(matriz) == 3
    guardar = set(range(0, 21)) | set(range(25, 501, 25)) | set(range(600, 6001, 100))
    estados = []
    for epoca in range(6001):
        error = matriz @ parametros - y
        if epoca in guardar:
            estados.append({"epoca": epoca, "mse": float(np.mean(error ** 2)),
                            "parametros": parametros.tolist()})
        if epoca < 6000:
            parametros -= 0.02 * 2 * matriz.T @ error / len(y)
    solucion = np.linalg.lstsq(matriz, y, rcond=None)[0]
    np.testing.assert_allclose(parametros, solucion, atol=1e-7)
    consulta = np.array([2.5, 3.0, 1.0])
    assert not np.any(np.all(np.isclose(x, consulta[:2]), axis=1))
    assert abs(float(consulta @ parametros) - 320) < 1e-6
    assert estados[-1]["mse"] < 1e-15
    resumen = {"entradas": 2, "salidas": 1, "observaciones": len(x),
               "parametros_entrenables": 3, "epocas": 6000, "tasa": 0.02,
               "mse_inicial": estados[0]["mse"], "mse_final": estados[-1]["mse"],
               "parametros_finales": parametros.tolist(),
               "entrada_reservada": consulta[:2].tolist(),
               "prediccion_reservada": float(consulta @ parametros),
               "gradiente_verificado": True, "datos_sinteticos": True}
    np.savetxt(BASE / "observaciones_hogares.csv", np.column_stack((x, y)), delimiter=",",
               header="ingreso_miles_um,integrantes,gasto_um", comments="", fmt="%.2f")
    return {"x": x.tolist(), "y": y.tolist(), "estados": estados,
            "referencia": referencia.tolist(), "resumen": resumen}


def exportar_figuras(casos):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": 0.15, "pdf.fonttype": 42})
    xs = np.linspace(-2, 2, 200)
    colores = ["#087f6b", "#8052a0"]
    lineal = casos[0]
    fig, ejes = plt.subplots(1, 2, figsize=(8.6, 3.0), layout="constrained")
    for ax, estado, titulo in zip(ejes, [lineal["estados"][0], lineal["estados"][-1]],
                                  ["Antes de entrenar", "Después: 400 épocas"]):
        ax.scatter(lineal["x"], np.array(lineal["y"])[:, 0], color="#12315a", s=20)
        ax.plot(xs, predecir(xs, estado["parametros"])[:, 0], color=colores[0], lw=2.3)
        ax.set(xlim=(-2.1, 2.1), ylim=(-3.7, 5.7), xlabel="Entrada x", ylabel="Salida", title=titulo)
    fig.savefig(FIGURAS / "simulacion_lineal.pdf", bbox_inches="tight")
    plt.close(fig)

def main():
    FIGURAS.mkdir(parents=True, exist_ok=True)
    casos = [entrenar(1), entrenar_multivariable()]
    plantilla = (BASE / "plantilla_afin.html").read_text(encoding="utf-8")
    estilo = (BASE / "plantilla.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]
    plantilla = plantilla.replace("__ESTILOS__", estilo)
    paginas = []
    for caso, nombre in zip(casos, ["lineal", "multivariable"]):
        if nombre == "multivariable":
            plantilla = (BASE / "plantilla_multivariable.html").read_text(encoding="utf-8").replace("__ESTILOS__", estilo)
        datos = json.dumps(caso, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
        html = plantilla.replace("__DATOS_JSON__", datos)
        (BASE / f"simulacion_{nombre}.html").write_text(html, encoding="utf-8")
        paginas.append(html)
    # Se conserva el entrenamiento cuadrático ya validado; no se vuelve a codificar.
    paginas.append((BASE / "simulacion_cuadrado.html").read_text(encoding="utf-8"))
    contenido = json.dumps(paginas, ensure_ascii=False).replace("<", "\\u003c")
    portal = (BASE / "plantilla_progresiva.html").read_text(encoding="utf-8")
    (BASE / "simulacion_progresiva.html").write_text(
        portal.replace("__PAGINAS_JSON__", contenido), encoding="utf-8")
    (BASE / "resumen_progresion.json").write_text(
        json.dumps([c["resumen"] for c in casos], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    exportar_figuras(casos)
    print(json.dumps([c["resumen"] for c in casos], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
