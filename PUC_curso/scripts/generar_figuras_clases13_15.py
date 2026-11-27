"""Figuras reproducibles para las clases 13--15; no compila LaTeX.

Ejecutar desde cualquier carpeta con NumPy y Matplotlib.
Las figuras conceptuales se distinguen de los ajustes entrenados.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
AZUL, VERDE, NARANJA = "#12315a", "#087f6b", "#d65324"
COLORES = [VERDE, NARANJA, AZUL]
plt.rcParams.update({"font.size": 11, "text.color": AZUL,
                     "axes.labelcolor": AZUL, "axes.spines.top": False,
                     "axes.spines.right": False, "pdf.fonttype": 42})


def guardar(fig, carpeta, nombre):
    destino = ROOT / carpeta / "presentacion" / "figuras"
    destino.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino / f"{nombre}.pdf", bbox_inches="tight")
    fig.savefig(destino / f"{nombre}.png", dpi=140, bbox_inches="tight")
    plt.close(fig)


def softmax(z):
    e = np.exp(z - z.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def clasificacion(k):
    rng = np.random.default_rng(42)
    centros = np.array([[-1.5, -1], [1.5, -0.5], [0, 1.7]])[:k]
    x = np.concatenate([rng.normal(c, 0.7, size=(40, 2)) for c in centros])
    y = np.repeat(np.arange(k), 40)
    a = np.column_stack([np.ones(len(x)), x])
    w = rng.normal(0, 0.15, size=(3, k))
    losses = []
    for _ in range(150):
        p = softmax(a @ w)
        losses.append(-np.log(p[np.arange(len(y)), y]).mean())
        w -= 0.1 * a.T @ (p - np.eye(k)[y]) / len(x)
    grid = np.linspace(-3.5, 3.5, 180)
    xx, yy = np.meshgrid(grid, grid)
    prob = softmax(np.column_stack([np.ones(xx.size), xx.ravel(), yy.ravel()]) @ w)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6), layout="constrained")
    axes[0].contourf(xx, yy, prob.argmax(axis=1).reshape(xx.shape),
                     levels=np.arange(k + 1) - 0.5,
                     cmap=ListedColormap(COLORES[:k]), alpha=0.14)
    for c in range(k):
        axes[0].scatter(*x[y == c].T, color=COLORES[c], s=15, label=f"Clase {c}")
    axes[0].set(xlabel="$x_1$", ylabel="$x_2$", title="Regiones aprendidas (datos sintéticos)")
    axes[0].legend(fontsize=8)
    axes[1].plot(np.arange(1, 151), losses, color=VERDE)
    axes[1].set(xlabel="Actualización", ylabel="Entropía cruzada",
                title="Pérdida antes de cada actualización")
    guardar(fig, "Lunes30", f"clasificacion_{k}")


def main():
    z = np.linspace(-6, 6, 400)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.4), layout="constrained")
    axes[0].plot(z, 1 / (1 + np.exp(-z)), color=VERDE)
    axes[0].axhline(0.5, color=NARANJA, linestyle="--")
    axes[0].axvline(0, color=AZUL, linestyle=":")
    axes[0].set(xlabel="Combinación z", ylabel="p = sigmoide(z)", title="De puntaje a probabilidad")
    p = np.linspace(0.001, 0.999, 400)
    axes[1].plot(p, -np.log(p), color=VERDE, label="Etiqueta y = 1")
    axes[1].plot(p, -np.log(1 - p), color=NARANJA, label="Etiqueta y = 0")
    axes[1].set(xlabel="Probabilidad predicha p", ylabel="Pérdida por observación", title="Equivocarse con confianza cuesta más")
    axes[1].legend()
    guardar(fig, "Lunes30", "sigmoide_perdida")
    clasificacion(2)
    clasificacion(3)

    x = np.linspace(-2, 2, 401)
    knots = np.linspace(-2, 2, 9)
    valores = knots ** 2
    pendientes = np.diff(valores) / np.diff(knots)
    # Interpolación lineal exacta expresada como suma de bisagras ReLU.
    aprox = valores[0] + pendientes[0] * (x - knots[0])
    for j in range(1, len(knots) - 1):
        aprox += (pendientes[j] - pendientes[j - 1]) * np.maximum(x - knots[j], 0)
    assert np.max(np.abs(aprox - x ** 2)) < 0.063
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), layout="constrained")
    for j, knot in enumerate([-1, 0, 1]):
        axes[0].plot(x, np.maximum(x - knot, 0), color=COLORES[j], label=f"ReLU(x − ({knot}))")
    axes[0].set(title="Cada neurona aporta una bisagra", xlabel="x", ylabel="Activación")
    axes[0].legend(fontsize=8)
    axes[1].plot(x, x ** 2, color=AZUL, linewidth=3, label="Objetivo x²")
    axes[1].plot(x, np.full_like(x, np.mean(x ** 2)), "--", color=NARANJA, label="Mejor modelo afín en esta malla")
    axes[1].plot(x, aprox, color=VERDE, label="Combinación de bisagras (construida)")
    axes[1].set(xlabel="x", ylabel="Salida", title="No linealidad y varias neuronas")
    axes[1].legend(fontsize=8)
    guardar(fig, "Martes01", "relu_cuadrado")

    rng = np.random.default_rng(7)
    angulo = rng.uniform(0, 2 * np.pi, 200)
    radio = np.repeat([0.35, 1], 100) + rng.normal(0, 0.06, 200)
    x1, x2 = radio * np.cos(angulo), radio * np.sin(angulo)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), layout="constrained")
    for ax in axes:
        for c in range(2):
            sl = slice(c * 100, (c + 1) * 100)
            ax.scatter(x1[sl], x2[sl], color=COLORES[c], s=13)
        ax.set(xlabel="$x_1$", ylabel="$x_2$", aspect="equal")
    axes[0].plot([-1.2, 1.2], [-0.6, 0.6], "--", color=AZUL)
    axes[0].set_title("Una recta no separa interior y exterior")
    theta = np.linspace(0, 2 * np.pi, 300)
    axes[1].plot(0.67 * np.cos(theta), 0.67 * np.sin(theta), color=VERDE)
    axes[1].set_title("Frontera no lineal deseada (ilustración)")
    guardar(fig, "Martes01", "circulos")

    t = np.arange(1, 101)
    train = 0.9 * np.exp(-t / 23) + 0.08
    val = 0.8 * np.exp(-t / 20) + 0.2 + 0.00011 * np.maximum(t - 25, 0) ** 2
    mejor = np.argmin(val)
    fig, ax = plt.subplots(figsize=(8.5, 3.5), layout="constrained")
    ax.plot(t, train, color=VERDE, label="Entrenamiento")
    ax.plot(t, val, color=NARANJA, label="Validación")
    ax.axvline(t[mejor], color=AZUL, linestyle="--", label="Menor pérdida de validación")
    ax.set(xlabel="Época", ylabel="Pérdida", title="Curvas conceptuales: no son resultados del notebook")
    ax.legend()
    guardar(fig, "Miércoles02", "sobreajuste")
    print("Figuras generadas: 6 PDF y sus vistas PNG. No se compiló LaTeX.")


if __name__ == "__main__":
    main()
