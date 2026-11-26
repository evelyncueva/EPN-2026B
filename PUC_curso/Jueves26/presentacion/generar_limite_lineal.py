"""Compara el óptimo afín con los datos cuadráticos de la simulación."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 21)
y = x ** 2
w, b = np.linalg.lstsq(np.column_stack((x, np.ones_like(x))), y, rcond=None)[0]
assert abs(w) < 1e-12
fig, ax = plt.subplots(figsize=(7.6, 4.0), layout="constrained")
xs = np.linspace(-2, 2, 200)
ax.plot(xs, xs ** 2, "--", color="0.5", label="Referencia: y = x²")
ax.scatter(x, y, color="#12315a", s=26, label="21 pares de entrenamiento", zorder=3)
ax.plot(xs, w * xs + b, color="#d65324", lw=2.4, label="Mejor recta posible con estos datos")
for i in [0, 5, 10, 15, 20]:
    ax.plot([x[i], x[i]], [y[i], w * x[i] + b], color="#d65324", alpha=0.5, lw=1.3)
ax.set(xlabel="Entrada x", ylabel="Salida", ylim=(-0.3, 4.8),
       title=f"Óptimo lineal: w ≈ 0, b ≈ {b:.3f} · MSE = {np.mean((w*x+b-y)**2):.4f}")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.15)
ax.legend(fontsize=9, loc="upper center")
fig.savefig(Path(__file__).parent / "figuras/limite_lineal_cuadrado.pdf")
plt.close(fig)
