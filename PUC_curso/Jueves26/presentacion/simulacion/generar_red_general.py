"""Ilustra una propagación hacia delante con parámetros fijos (no entrenamiento)."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np
from PIL import Image

BASE = Path(__file__).resolve().parent
AZUL, VERDE, NARANJA = "#12315a", "#087f6b", "#d65324"
W1 = np.array([[1.2, -1.0], [-0.8, 1.2], [0.6, 0.6]])
B1 = np.array([-0.1, -0.1, -0.5])
W2 = np.array([[1.1, -0.6, 0.8], [-0.4, 1.0, 0.7]])
B2 = np.array([-0.1, -0.1])


def propagar(entrada):
    h1 = np.maximum(W1 @ entrada + B1, 0)
    h2 = np.maximum(W2 @ h1 + B2, 0)
    salida = 1 / (1 + np.exp(-(np.array([1.1, -0.7]) @ h2 + 0.1)))
    return [np.array(entrada), h1, h2, np.array([salida])]


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "text.color": AZUL})
    entradas = [np.array([0.9, 0.2]), np.array([0.2, 0.9]), np.array([0.7, 0.7])]
    valores = [propagar(x) for x in entradas]
    assert valores[0][1][1] == 0 and valores[1][1][0] == 0
    assert np.all(valores[2][2] > 0)
    np.testing.assert_allclose(valores[0][1][0], 1.2 * 0.9 - 1.0 * 0.2 - 0.1)
    assert all(np.all(np.isfinite(capa)) for caso in valores for capa in caso)
    posiciones = [[(0.6, 0.8), (0.6, -0.8)],
                  [(3.6, 1.25), (3.6, 0), (3.6, -1.25)],
                  [(6.6, 0.8), (6.6, -0.8)], [(9.4, 0)]]
    fig, ax = plt.subplots(figsize=(12.8, 5.6), dpi=95)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.17, top=0.89)
    ax.set(xlim=(-0.9, 11), ylim=(-2.75, 2.3), aspect="equal")
    ax.axis("off")
    nombres = ["Capa de\nentrada", "Capa intermedia 1\n(oculta)",
               "Capa intermedia 2\n(oculta)", "Capa de\nsalida"]
    for capa, nombre in zip(posiciones, nombres):
        centro = capa[0][0]
        ax.add_patch(Rectangle((centro - 0.53, -1.72), 1.06, 3.44,
                               facecolor="#f3f6fa", edgecolor="#91a3b9",
                               linewidth=1.15, zorder=0))
        ax.text(centro, -2.3, nombre, ha="center", va="center", fontsize=13)
    conexiones = []
    for k in range(3):
        grupo = []
        for j, inicio in enumerate(posiciones[k]):
            for fin in posiciones[k + 1]:
                flecha = FancyArrowPatch(inicio, fin, arrowstyle="-|>", mutation_scale=10,
                                         shrinkA=19, shrinkB=19, color="#b8c4d1", lw=1)
                ax.add_patch(flecha)
                grupo.append((j, np.array(inicio), np.array(fin), flecha))
        conexiones.append(grupo)
    circulos, textos = [], []
    for capa in posiciones:
        cs, ts = [], []
        for x, y in capa:
            c = Circle((x, y), 0.31, facecolor="white", edgecolor=AZUL, lw=1.4, zorder=4)
            ax.add_patch(c)
            t = ax.text(x, y, "", ha="center", va="center", fontsize=14, zorder=5)
            cs.append(c); ts.append(t)
        circulos.append(cs); textos.append(ts)
    def etiqueta(texto, xy, destino, alineacion="center"):
        ax.annotate(texto, xy=destino, xytext=xy, ha=alineacion, va="center", fontsize=16,
                    arrowprops={"arrowstyle": "->", "color": AZUL, "lw": 1.2}, color=AZUL)
    etiqueta("Entradas", (-0.1, 1.9), (0.5, 1.08))
    etiqueta("Neurona", (3.1, 2.05), (3.5, 1.55))
    etiqueta("Activación", (7.0, 1.95), (6.7, 1.02))
    etiqueta("Salida", (10.5, 1.2), (9.65, 0.22))
    etiqueta("Conexiones", (2.0, -1.9), (2.0, -0.3))
    # Solo se rotulan los dos pesos de la primera neurona intermedia.
    for j in range(2):
        inicio = np.array(posiciones[0][j])
        fin = np.array(posiciones[1][0])
        xy = inicio + 0.38 * (fin - inicio)
        angulo = np.degrees(np.arctan2(*(fin - inicio)[::-1]))
        ax.text(*xy, f"peso: {W1[0, j]:.1f}", ha="center", va="center",
                fontsize=12.5, rotation=angulo, color=NARANJA, zorder=8,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    etiqueta(f"Sesgo: {B1[0]:.1f}", (4.8, 1.7), (3.87, 1.35))
    circulos[1][0].set_edgecolor(NARANJA)
    circulos[1][0].set_linewidth(2.2)
    ax.text(6.4, -1.98, "El color indica el nivel de respuesta", ha="center", fontsize=14)
    fig.text(0.5, 0.97, "", ha="center", va="top", fontsize=18)
    titulo = fig.texts[-1]
    fase = fig.text(0.5, 0.105, "", ha="center", fontsize=14)
    calculo = fig.text(0.5, 0.065, "", ha="center", fontsize=11.5)
    fig.text(0.5, 0.028, "Blanco: por calcular   ·   Gris con 0: respuesta nula   ·   Verde: respuesta positiva de distinta intensidad",
             ha="center", fontsize=11)
    pulsos = []
    for _ in range(6):
        punto, = ax.plot([], [], "o", color=NARANJA, ms=5, zorder=3)
        pulsos.append(punto)
    fases = ["Llegan los datos a las entradas", "Las entradas alimentan a las primeras neuronas",
             "Cada neurona combina señales y produce una respuesta", "Las respuestas pasan al siguiente grupo",
             "Las siguientes neuronas calculan sus respuestas", "Las respuestas llegan a la neurona de salida",
             "Se obtiene la salida; otra entrada puede producir otra respuesta"]

    def dibujar(caso, paso, avance=0.0):
        capas = valores[caso]
        calculadas = [True, paso >= 2, paso >= 4, paso >= 6]
        for k, (cs, ts) in enumerate(zip(circulos, textos)):
            for j, (c, t) in enumerate(zip(cs, ts)):
                v = float(capas[k][j])
                t.set_color(AZUL)
                if not calculadas[k]:
                    c.set_facecolor("white"); t.set_text("…")
                elif k == 0:
                    c.set_facecolor("#e1eaf4"); t.set_text(f"{v:.2f}")
                elif v == 0:
                    c.set_facecolor("#e4e7eb"); t.set_text("0")
                else:
                    intensidad = min(v, 1) * 0.7 + 0.15
                    c.set_facecolor((1 - intensidad) * np.ones(3) + intensidad * np.array(to_rgb(VERDE)))
                    t.set_color("white" if intensidad > 0.6 else AZUL)
                    t.set_text(f"{v:.2f}")
        for k, grupo in enumerate(conexiones):
            for m, (_, _, _, flecha) in enumerate(grupo):
                flecha.set_color("#b8c4d1"); flecha.set_linewidth(1)
                if k == 0 and m in (0, 3):
                    flecha.set_color(AZUL); flecha.set_linewidth(1.8)
        for p in pulsos:
            p.set_data([], [])
        if paso in (1, 3, 5):
            k = (paso - 1) // 2
            for m, (j, inicio, fin, flecha) in enumerate(conexiones[k]):
                if capas[k][j] > 0:
                    flecha.set_color(VERDE); flecha.set_linewidth(1.7)
                    xy = inicio + (0.15 + avance * 0.7) * (fin - inicio)
                    pulsos[m].set_data([xy[0]], [xy[1]])
        titulo.set_text(f"De la entrada a la salida · Ejemplo {caso + 1}")
        fase.set_text(fases[paso])
        if paso >= 2:
            z = float(W1[0] @ capas[0] + B1[0])
            calculo.set_text(f"Neurona señalada: 1.2 × {capas[0][0]:.2f} − 1.0 × {capas[0][1]:.2f} − 0.10 = {z:.2f}"
                             f"     →     respuesta: {capas[1][0]:.2f}")
        else:
            calculo.set_text("Los pesos y el sesgo se mantienen fijos al cambiar las entradas")

    dibujar(0, 6)
    titulo.set_text("Una red es un conjunto de neuronas conectadas")
    fase.set_text("Cada respuesta puede alimentar a las neuronas siguientes")
    destino_pdf = BASE.parent / "figuras/red_general.pdf"
    fig.savefig(destino_pdf, bbox_inches="tight")
    imagenes, duraciones = [], []
    try:
        for caso in range(3):
            for paso in range(7):
                for t in range(4):
                    dibujar(caso, paso, t / 3)
                    fig.canvas.draw()
                    imagenes.append(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB").quantize(colors=256))
                    duraciones.append(120 if paso in (1, 3, 5) else 220)
            print(f"Ejemplo {caso + 1}/3 renderizado", flush=True)
        duraciones[0], duraciones[-1] = 900, 2000
        destino = BASE / "propagacion_red.gif"
        imagenes[0].save(destino, save_all=True, append_images=imagenes[1:],
                         duration=duraciones, loop=0, disposal=2, optimize=False)
        with Image.open(destino) as gif:
            for i in range(gif.n_frames):
                gif.seek(i); gif.load()
            print(f"GIF verificado: {gif.n_frames} fotogramas, {gif.size}", flush=True)
    finally:
        plt.close(fig)
        for im in imagenes:
            im.close()


if __name__ == "__main__":
    main()
