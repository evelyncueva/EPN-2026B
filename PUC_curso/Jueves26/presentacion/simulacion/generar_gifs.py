"""Exporta a GIF los entrenamientos lineal y económico de la progresión.

Reutiliza los entrenadores y las observaciones de generar_progresion.py.
El GIF económico muestra el plano completo para sus dos entradas.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
from PIL import Image

from generar_progresion import entrenar, entrenar_multivariable, predecir

BASE = Path(__file__).resolve().parent
AZUL, VERDE, NARANJA = "#12315a", "#087f6b", "#d65324"


def estilo():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "text.color": AZUL, "axes.labelcolor": AZUL, "axes.titlecolor": AZUL,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.alpha": 0.16,
    })


def preparar_perdida(ax, estados):
    ax.set(xlim=(0, estados[-1]["epoca"]),
           ylim=(1e-12, max(e["mse"] for e in estados) * 1.4), yscale="log",
           xlabel="Época", ylabel="MSE de entrenamiento")
    ax.set_title("Pérdida · escala logarítmica")
    linea, = ax.plot([], [], color=VERDE, lw=2)
    punto, = ax.plot([], [], "o", color=VERDE, ms=4)
    return linea, punto


def actualizar_perdida(estados, i, linea, punto):
    # El gráfico tiene un mínimo visual; las métricas conservan su valor real.
    perdidas = [max(e["mse"], 1e-12) for e in estados[:i + 1]]
    linea.set_data([e["epoca"] for e in estados[:i + 1]], perdidas)
    punto.set_data([estados[i]["epoca"]], [perdidas[-1]])


def codificar(fig, estados, actualizar, nombre):
    imagenes = []
    try:
        for i in range(len(estados)):
            actualizar(i)
            fig.canvas.draw()
            rgba = np.asarray(fig.canvas.buffer_rgba())
            imagenes.append(Image.fromarray(rgba).convert("RGB").quantize(colors=256))
            if i and i % 25 == 0:
                print(f"  {nombre}: {i}/{len(estados)} estados renderizados", flush=True)
        duraciones = [140] * len(imagenes)
        duraciones[0], duraciones[-1] = 900, 2000
        destino = BASE / nombre
        imagenes[0].save(destino, save_all=True, append_images=imagenes[1:],
                         duration=duraciones, loop=0, optimize=False, disposal=2)
        with Image.open(destino) as gif:
            assert gif.n_frames == len(estados)
            for j in range(gif.n_frames):
                gif.seek(j)
                gif.load()
            duracion = sum(duraciones) / 1000
            print(f"{nombre}: {gif.n_frames} estados, {gif.size}, "
                  f"{duracion:.2f} segundos por ciclo, {destino.stat().st_size} bytes", flush=True)
    finally:
        plt.close(fig)
        for imagen in imagenes:
            imagen.close()


def exportar_lineal():
    caso = entrenar(1)
    estados = caso["estados"]
    x, y = np.array(caso["x"]), np.array(caso["y"])[:, 0]
    for e in estados:
        np.testing.assert_allclose(np.mean((predecir(x, e["parametros"])[:, 0] - y) ** 2),
                                   e["mse"], atol=1e-25, rtol=1e-12)
    fig, (ax, ax_loss) = plt.subplots(1, 2, figsize=(11.4, 5.2), dpi=95,
                                     gridspec_kw={"width_ratios": [1.55, 1]})
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.15, top=0.76, wspace=0.28)
    xs = np.linspace(-2, 2, 160)
    ax.plot(xs, 2 * xs + 1, "--", color="0.55", lw=1.5, label="Referencia: y = 2x + 1")
    ax.scatter(x, y, s=22, color=AZUL, label="21 observaciones", zorder=3)
    linea, = ax.plot([], [], color=VERDE, lw=2.3, label="Neurona: ŷ = wx + b")
    consulta, = ax.plot([], [], "D", color=NARANJA, ms=7, label="Entrada nueva: x = 1.5")
    ax.set(xlim=(-2.1, 2.1), ylim=(-3.7, 5.7), xlabel="Entrada x", ylabel="Salida")
    ax.legend(fontsize=8, loc="upper left")
    traza, punto = preparar_perdida(ax_loss, estados)
    titulo = fig.suptitle("", y=0.97, fontsize=14)
    parametros = fig.text(0.5, 0.86, "", ha="center", va="center", fontsize=11)
    fig.text(0.5, 0.025, "Estados reales de entrenamiento · referencia para x = 1.5: 4 · mínimo visual del MSE: 10⁻¹²",
             ha="center", fontsize=9)

    def actualizar(i):
        e = estados[i]
        w, b = e["parametros"]
        pred = float(predecir(1.5, e["parametros"])[0])
        linea.set_data(xs, predecir(xs, e["parametros"])[:, 0])
        consulta.set_data([1.5], [pred])
        actualizar_perdida(estados, i, traza, punto)
        titulo.set_text(f"Una neurona · Época {e['epoca']} · MSE = {e['mse']:.3e}")
        parametros.set_text(f"w = {w:.4f}     b = {b:.4f}     →     ŷ(1.5) = {pred:.4f}")

    codificar(fig, estados, actualizar, "entrenamiento_lineal.gif")


def exportar_multivariable():
    caso = entrenar_multivariable()
    estados = caso["estados"]
    x, y = np.array(caso["x"]), np.array(caso["y"])
    matriz = np.column_stack((x, np.ones(len(x))))
    for e in estados:
        np.testing.assert_allclose(np.mean((matriz @ e["parametros"] - y) ** 2),
                                   e["mse"], atol=1e-22, rtol=1e-12)
    fig = plt.figure(figsize=(12, 5.8), dpi=95)
    rejilla = fig.add_gridspec(1, 2, width_ratios=[1.45, 1], left=0.035,
                             right=0.97, bottom=0.20, top=0.79, wspace=0.20)
    ax = fig.add_subplot(rejilla[0], projection="3d")
    ax_loss = fig.add_subplot(rejilla[1])
    ax.scatter(x[:, 0], x[:, 1], y, s=24, color=AZUL, depthshade=False)
    ax.scatter([2.5], [3], [320], s=50, marker="o", facecolors="none",
               edgecolors=NARANJA, depthshade=False)
    consulta, = ax.plot([2.5], [3], [55], "D", color=NARANJA, ms=7)
    ax.set(xlim=(0.8, 4.2), ylim=(0.8, 5.2), zlim=(0, 540),
           xlabel="Ingreso x₁ (miles de u.m.)", ylabel="Integrantes x₂",
           zlabel="Gasto ŷ (u.m.)")
    ax.tick_params(labelsize=8)
    ax.xaxis.label.set_size(9)
    ax.yaxis.label.set_size(9)
    ax.zaxis.label.set_size(9)
    ax.view_init(elev=23, azim=-58)
    ax.set_box_aspect((1.1, 1.0, 0.85))
    ax.set_title("Dos entradas, una salida: un plano", fontsize=11)
    xx, yy = np.meshgrid(np.linspace(1, 4, 11), np.linspace(1, 5, 11))
    superficie = None
    traza, punto = preparar_perdida(ax_loss, estados)
    titulo = fig.suptitle("", y=0.98, fontsize=14)
    parametros = fig.text(0.5, 0.89, "", ha="center", va="center", fontsize=11)
    prediccion = fig.text(0.5, 0.84, "", ha="center", va="center", fontsize=10)
    fig.legend(handles=[Line2D([], [], marker="o", ls="", color=AZUL, label="25 hogares sintéticos"),
                        Patch(facecolor=VERDE, alpha=0.4, label="Plano de la neurona"),
                        Line2D([], [], marker="D", ls="", color=NARANJA, label="Predicción del hogar nuevo"),
                        Line2D([], [], marker="o", ls="", markerfacecolor="none", color=NARANJA, label="Referencia: 320 u.m.")],
               loc="lower center", bbox_to_anchor=(0.5, 0.055), ncol=2, frameon=False, fontsize=9)
    fig.text(0.5, 0.018, "ŷ = w₁x₁ + w₂x₂ + b · MSE sobre los 25 hogares · mínimo visual del MSE: 10⁻¹²",
             ha="center", fontsize=9)

    def actualizar(i):
        nonlocal superficie
        e = estados[i]
        w1, w2, b = e["parametros"]
        if superficie is not None:
            superficie.remove()
        superficie = ax.plot_surface(xx, yy, w1 * xx + w2 * yy + b,
                                     color=VERDE, alpha=0.35, edgecolor=VERDE,
                                     linewidth=0.3, antialiased=True)
        pred = w1 * 2.5 + w2 * 3 + b
        consulta.set_data_3d([2.5], [3], [pred])
        actualizar_perdida(estados, i, traza, punto)
        titulo.set_text(f"Una neurona con dos entradas · Época {e['epoca']} · MSE = {e['mse']:.3e}")
        parametros.set_text(f"w₁ = {w1:.4f}     w₂ = {w2:.4f}     b = {b:.4f}")
        prediccion.set_text(f"Hogar nuevo: ingreso 2500 u.m., 3 integrantes → gasto predicho: {pred:.2f} u.m.")

    codificar(fig, estados, actualizar, "entrenamiento_multivariable.gif")


if __name__ == "__main__":
    estilo()
    print("Generando GIF lineal...", flush=True)
    exportar_lineal()
    print("Generando GIF de dos variables económicas...", flush=True)
    exportar_multivariable()
