"""Ilustra una pérdida de dos parámetros y su descenso por gradiente."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def perdida(w, b):
    return 2 * (w - 2) ** 2 + (b + 1) ** 2


def main():
    plt.rcParams.update({"font.size": 11, "text.color": "#12315a",
                         "axes.labelcolor": "#12315a"})
    w, b = np.meshgrid(np.linspace(-0.8, 4.8, 120),
                       np.linspace(-3.5, 2.3, 120))
    trayectoria = [np.array([0.0, 1.0])]
    for _ in range(8):
        punto = trayectoria[-1]
        gradiente = np.array([4 * (punto[0] - 2), 2 * (punto[1] + 1)])
        trayectoria.append(punto - 0.2 * gradiente)
    trayectoria = np.array(trayectoria)

    fig = plt.figure(figsize=(12, 3.7), constrained_layout=True)
    ax = fig.add_subplot(121, projection="3d")
    ax.plot_surface(w, b, perdida(w, b), cmap="Blues", alpha=0.8,
                    linewidth=0, rcount=45, ccount=45)
    ax.plot(trayectoria[:, 0], trayectoria[:, 1],
            perdida(trayectoria[:, 0], trayectoria[:, 1]) + 0.15,
            "o-", color="#087f6b", markersize=4, linewidth=2)
    ax.scatter([2], [-1], [0], color="#d65324", s=45)
    ax.set(xlabel="$w$", ylabel="$b$", zlabel="$L(w,b)$",
           title="La pérdida forma un paraboloide")
    ax.view_init(elev=27, azim=40)
    ax.set_zlim(0, 33)

    ax = fig.add_subplot(122)
    curvas = ax.contour(w, b, perdida(w, b), levels=[0.5, 2, 5, 12, 20, 30],
                        cmap="Blues")
    ax.clabel(curvas, inline=True, fontsize=9, fmt="%g")
    ax.plot(trayectoria[:, 0], trayectoria[:, 1], "o-", color="#087f6b",
            markersize=4, linewidth=1.5)
    ax.scatter([2], [-1], color="#d65324", marker="*", s=130, zorder=5)
    ax.annotate("Mínimo (2, −1)", (2, -1), xytext=(2.4, -2.2),
                arrowprops={"arrowstyle": "->", "color": "#12315a"})
    ax.annotate("Inicio (0, 1)", (0, 1), xytext=(0.2, 1.9))
    # Ambas flechas parten del mismo punto; se escalan solo para visualizarlas.
    for extremo, color in [((-0.8, 1.4), "#d65324"),
                            ((0.8, 0.6), "#087f6b")]:
        ax.annotate("", xy=extremo, xytext=(0, 1),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
    # Extremos en coordenadas absolutas: dirección proporcional a (−8, 4).
    ax.text(-0.75, 1.55, "$+\\nabla L$", color="#d65324")
    ax.text(0.65, 0.25, "$-\\nabla L$", color="#087f6b")
    ax.set(xlabel="$w$ (peso)", ylabel="$b$ (sesgo)",
           title="Curvas de nivel: igual valor de L", xlim=(-1.1, 4.8), ylim=(-3.5, 2.3))
    ax.set_aspect("equal")
    destino = Path(__file__).resolve().parents[1] / "figuras"
    fig.savefig(destino / "gradiente_paraboloide.pdf")
    fig.savefig(destino / "gradiente_paraboloide.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
