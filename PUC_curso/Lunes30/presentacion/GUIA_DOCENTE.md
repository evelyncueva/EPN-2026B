# Clase 13: perceptrón sigmoide y multiclase

Fuente: `clase13_clasificacion.tex`. Diseño y notas docentes heredados de la clase del jueves. No se compiló la presentación.

## Propósito y secuencia

La guía `../Clase13.pdf` pide combinación, activación, pérdida y gradientes para clasificación binaria y multiclase, con implementación en Python.

1. Recuperar la regresión del jueves y distinguir cantidad, probabilidad y clase.
2. Introducir sigmoide, umbral y frontera lineal; comparar BCE y exactitud.
3. Derivar `dL/dz = p-y` y hacer un paso numérico.
4. Explorar el notebook binario.
5. Construir softmax, etiquetas one-hot y entropía cruzada categórica.
6. Revisar dimensiones del gradiente multiclase y experimentar con el segundo notebook.

Distribución orientativa: 40% binaria, 35% multiclase y 25% prácticas y discusión. Las portadillas de sección añaden páginas al conteo de frames explícitos.

## Cuadernos originales y adaptaciones propuestas

Los originales se conservan intactos. Numeración de celdas desde 1, incluyendo Markdown:

- `../13-1-Perceptron-Sigmoide.ipynb`: datos en 7, implementación en 10, entrenamiento en 12, animación en 14.
- `../13-2-Perceptron-Multiclase.ipynb`: misma distribución de celdas. Primera fila de pesos = sesgos, por la columna de unos.
- Para BCE estable, reemplazar el cálculo por `np.mean(np.logaddexp(0, z) - y*z)` desde los logits. La presentación incluye el paso correspondiente.
- Ambas implementaciones guardan pérdida antes de actualizar y pesos después. Para sincronizar animación, registrar ambos antes del paso o recalcular pérdida después del paso antes de guardarla.
- `fit` reinicializa pesos, pero no vacía `ws` ni `losses`: crear una instancia nueva para cada experimento o reiniciar ambas listas al comenzar.
- La animación multiclase elimina colecciones del contorno mediante una interfaz que puede depender de la versión instalada. Si falla, usar una gráfica estática de la frontera final o adaptar el borrado al entorno de la clase.

## Preguntas y actividad

Conservar datos y semilla al comparar tasas 0.1, 0.01 y 0.001. Registrar pérdida y exactitud; luego aumentar la dispersión. Preguntar por qué una sigmoide no convierte una frontera afín en curva y por qué softmax no equivale a varias sigmoides independientes.

## Figuras y preparación

Desde la raíz del repositorio: `python scripts/generar_figuras_clases13_15.py` requiere NumPy y Matplotlib y genera los recursos locales. Las figuras de clasificación son experimentos sintéticos independientes del notebook, documentados en las notas; no presentan resultados de los cuadernos históricos.

Compilar desde esta carpeta: `pdflatex -interaction=nonstopmode -halt-on-error clase13_clasificacion.tex` (dos pasadas para numeración). Revisar visualmente al compilar. No se ejecutaron los notebooks ni se verificó renderizado de Beamer en esta entrega.

Para el martes: retomar la lectura sobre frameworks y API indicada por la guía. Pregunta puente: ¿qué añadir para aprender fronteras curvas?
