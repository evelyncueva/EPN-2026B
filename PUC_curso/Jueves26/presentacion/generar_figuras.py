"""Genera figuras del perceptrón lineal con los datos del notebook de clase."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DESTINO = Path(__file__).resolve().parent / "figuras"
AZUL = "#12315a"
VERDE = "#087f6b"
NARANJA = "#d65324"
GRIS = "#687585"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelcolor": AZUL,
    "text.color": AZUL,
    "axes.titlecolor": AZUL,
    "axes.grid": True,
    "grid.alpha": 0.15,
    "pdf.fonttype": 42,
})


def datos(pendiente=2, sesgo=0):
    """Misma secuencia aleatoria que np.random.seed(42) en el notebook."""
    rng = np.random.RandomState(42)
    x = rng.rand(30)
    y = pendiente * x + sesgo + (rng.rand(30) - 0.5) * 0.5
    return x, y


def entrenar(x, y, *, lr=0.1, epocas=50, con_sesgo=False, semilla=42):
    rng = np.random.RandomState(semilla)
    w = rng.rand()
    b = rng.rand() if con_sesgo else 0.0
    trayectoria = [(w, b, np.mean((w * x + b - y) ** 2))]
    for _ in range(epocas):
        error = w * x + b - y
        dw = 2 * np.mean(error * x)
        db = 2 * np.mean(error) if con_sesgo else 0.0
        w -= lr * dw
        b -= lr * db
        trayectoria.append((w, b, np.mean((w * x + b - y) ** 2)))
    return np.asarray(trayectoria)


def guardar(figura, nombre):
    figura.savefig(DESTINO / f"{nombre}.pdf", bbox_inches="tight")
    plt.close(figura)


def generar_tasas_aprendizaje():
    x, y = datos()
    fig, ax = plt.subplots(figsize=(9, 3.5), layout="constrained")
    for lr, color in [(0.1, VERDE), (0.01, NARANJA), (0.001, GRIS)]:
        tr = entrenar(x, y, lr=lr, epocas=50)
        ax.semilogy(np.arange(51), tr[:, 2], lw=2.2, color=color, label=fr"$\eta={lr:g}$")
    ax.set(xlabel="Época (0 = inicialización)", ylabel="MSE · escala logarítmica")
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    guardar(fig, "tasas_aprendizaje")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)

    z = np.linspace(-4, 4, 401)
    activaciones = [
        ("Identidad", z, r"$\sigma(z)=z$"),
        ("Escalón", (z >= 0).astype(float), r"$\sigma(z)=\mathbf{1}_{z\geq 0}$"),
        ("Sigmoide", 1 / (1 + np.exp(-z)), r"$\sigma(z)=1/(1+e^{-z})$"),
        ("tanh", np.tanh(z), r"$\sigma(z)=\tanh(z)$"),
        ("ReLU", np.maximum(z, 0), r"$\sigma(z)=\max(0,z)$"),
    ]
    fig, ejes = plt.subplots(1, 5, figsize=(12.8, 2.7), layout="constrained")
    for ax, (nombre, valores, formula) in zip(ejes, activaciones):
        ax.axhline(0, color=GRIS, lw=0.6)
        ax.axvline(0, color=GRIS, lw=0.6)
        if nombre == "Escalón":
            ax.plot([-4, 0], [0, 0], color=AZUL, lw=2)
            ax.plot([0, 4], [1, 1], color=AZUL, lw=2)
            ax.plot(0, 0, "o", mfc="white", mec=AZUL, ms=5)
            ax.plot(0, 1, "o", color=AZUL, ms=5)
        else:
            ax.plot(z, valores, color=VERDE if nombre == "Identidad" else AZUL, lw=2)
        ax.set_title(nombre, fontweight="bold")
        ax.set_xlabel(formula, fontsize=10)
        ax.set_xticks([-4, 0, 4])
    guardar(fig, "activaciones")

    x, y = datos()
    trayectoria = entrenar(x, y)
    xs = np.linspace(0, 1, 150)

    fig, ax = plt.subplots(figsize=(6.4, 3.8), layout="constrained")
    ax.scatter(x, y, s=32, color=AZUL, label="Datos de entrenamiento")
    ax.plot(xs, 1.2 * xs, color=NARANJA, lw=2, label=r"Predicción: $\hat y=1.2x$")
    for i in np.argsort(x)[[5, 15, 25]]:
        ax.plot([x[i], x[i]], [y[i], 1.2 * x[i]], color=VERDE, lw=2)
    ax.plot([], [], color=VERDE, lw=2, label=r"Residuo: $\hat y-y$")
    ax.set(xlabel="Entrada x", ylabel="Salida y")
    ax.legend(fontsize=9)
    guardar(fig, "residuos")

    fig, (ax, ax_loss) = plt.subplots(1, 2, figsize=(10.6, 3.7), layout="constrained")
    ax.scatter(x, y, s=27, color=AZUL, label="Datos")
    for indice, estilo, color, etiqueta in [
        (0, "--", GRIS, "Inicial"),
        (-1, "-", VERDE, "50 épocas"),
    ]:
        ax.plot(xs, trayectoria[indice, 0] * xs, estilo, color=color, lw=2, label=etiqueta)
    ax.set(xlabel="Entrada x", ylabel="Salida y", title="Ejemplo 1: sesgo fijo en cero")
    ax.legend(fontsize=9)
    ws = np.linspace(0, 4, 200)
    perdidas = [np.mean((w * x - y) ** 2) for w in ws]
    ax_loss.plot(ws, perdidas, color=AZUL)
    puntos = trayectoria[[0, 5, 15, 50]]
    ax_loss.scatter(puntos[:, 0], puntos[:, 2], c=[GRIS, NARANJA, NARANJA, VERDE], s=40, zorder=3)
    ax_loss.annotate("inicio", (puntos[0, 0], puntos[0, 2]), xytext=(8, 5), textcoords="offset points")
    ax_loss.annotate("final", (puntos[-1, 0], puntos[-1, 2]), xytext=(10, 14), textcoords="offset points")
    ax_loss.set(xlabel="Peso w", ylabel="MSE", title="Aprender = recorrer la función de pérdida")
    guardar(fig, "ejemplo_1")

    generar_tasas_aprendizaje()

    x2, y2 = datos(pendiente=4, sesgo=3)
    tr2 = entrenar(x2, y2, epocas=100, con_sesgo=True)
    w_sin_sesgo = np.dot(x2, y2) / np.dot(x2, x2)
    fig, ax = plt.subplots(figsize=(7.8, 3.8), layout="constrained")
    ax.scatter(x2, y2, s=30, color=AZUL, label="Datos del Ejemplo 2")
    ax.plot(xs, w_sin_sesgo * xs, "--", color=NARANJA, lw=2, label="Mejor ajuste con b = 0")
    ax.plot(xs, tr2[-1, 0] * xs + tr2[-1, 1], color=VERDE, lw=2, label="Con sesgo: 100 épocas")
    ax.set(xlabel="Entrada x", ylabel="Salida y")
    ax.legend(fontsize=9)
    guardar(fig, "efecto_sesgo")

    for nombre, tr in [("Ejemplo 1", trayectoria), ("Ejemplo 2", tr2)]:
        w, b, perdida = tr[-1]
        print(f"{nombre}: w={w:.6f}; b={b:.6f}; MSE final={perdida:.6f}")
    print(f"Figuras guardadas en {DESTINO}")


if __name__ == "__main__":
    main()
