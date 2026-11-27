# Clase 15: entrenamiento de redes neuronales

Fuente: `clase15_entrenamiento.tex`. Mismo diseño de la clase del jueves; no se compiló.

## Propósito y recorrido

La guía `../Clase15.pdf` pide deducción de retropropagación, regularización y optimizadores.

1. Distinguir forward pass, backward pass y actualización.
2. Derivar completa una red escalar y comprobar un paso a mano.
3. Generalizar a capas y explicar gradientes pequeños.
4. Comparar SGD, momentum, RMSProp y Adam.
5. Diagnosticar sobreajuste con validación; introducir L1, L2, dropout y early stopping.
6. Experimentar con el notebook y discutir el desempeño por clase.

Distribución orientativa: 40% retropropagación, 25% optimización y 35% regularización y laboratorio. La deducción matricial puede darse después del cálculo escalar en pizarra.

## Ejemplo numérico verificable

`x=2`, `y=3`, `w=1`, `b=0`, `v=0.5`, `c=0`. Una ReLU oculta y salida lineal; pérdida `0.5*(y_hat-y)**2`.

- Forward: `z=2`, `h=2`, `y_hat=1`, pérdida 2.
- Gradientes: `dv=-4`, `dc=-2`, `dw=-2`, `db=-1`.
- Con tasa 0.1: `w=1.2`, `b=0.1`, `v=0.9`, `c=0.2`.
- Nuevo forward: `y_hat=2.45`, pérdida 0.15125.

Calcular todos los gradientes con los parámetros anteriores antes de actualizar. El factor 1/2 es una convención pedagógica distinta del MSE de Keras.

## Notebook original y adaptaciones propuestas

`../15-Entrenamiento-Redes.ipynb` se conserva intacto. Las diapositivas aportan la deducción manual; el cuaderno implementa experimentos con Keras.

- Preparación: celdas 11–13 (posición desde 1). Separar datos sin escalar en 60/20/20 antes de `StandardScaler().fit(X_train)`. Transformar validación y prueba sin reajustar.
- Regularización: celdas 16–26. Baseline, L2, dropout y parada temprana. Probar inicialmente una técnica por vez.
- Optimizadores: celdas 32–36. SGD con momentum 0.9 y tasa 0.01; Adam y RMSprop con tasa 0.001. Mantener pesos iniciales y particiones; declarar que se comparan configuraciones, no un único hiperparámetro.
- El código original grafica la época de detención de early stopping. Esa época no es necesariamente la de menor `val_loss`; marcar ambas si se muestran resultados.
- Con regularización, la pérdida reportada puede incluir penalizaciones: no comparar directamente su magnitud con la pérdida de datos de un modelo sin penalización sin explicar la diferencia.
- El CSV Pokémon requiere conexión o copia local preparada con su procedencia. Comprobar faltantes y etiquetas antes de entrenar.

## Actividad y evaluación

Registrar semilla, optimizador, tasa, regularización, mejor época de validación y métricas por clase. Repetir con varias semillas cuando el tiempo lo permita. Elegir con validación y evaluar en prueba solo al final.

La gráfica de sobreajuste es conceptual y está rotulada como tal. Regenerarla desde la raíz: `python scripts/generar_figuras_clases13_15.py`.

Compilar desde esta carpeta: `pdflatex -interaction=nonstopmode -halt-on-error clase15_entrenamiento.tex`, dos pasadas. No se ejecutó el notebook ni TensorFlow y no se revisó el renderizado de las diapositivas; esas comprobaciones quedan para el entorno docente.
