# Clase 14: perceptrón multicapa

Fuente: `clase14_multicapa.tex`. Mantiene el estilo de la clase del jueves; no se compiló.

## Propósito y secuencia

Según `../Clase14.pdf`, explicar la arquitectura MLP y aplicarla a regresión, clasificación binaria, multiclase y un caso práctico.

1. Mostrar círculos concéntricos: una frontera lineal no basta.
2. Dibujar capas y distinguir suma dentro de la neurona y composición entre capas.
3. Demostrar que capas afines sin activaciones no lineales colapsan en un modelo afín.
4. Interpretar bisagras ReLU, contar parámetros y conectar con Keras.
5. Comparar las tres configuraciones de salida y recorrer los notebooks.
6. Trabajar el caso Pokémon separando datos antes del escalado.

Distribución orientativa: 35% arquitectura, 35% aplicaciones y 30% caso práctico y evaluación. Si falta tiempo, conservar regresión y círculos como demostraciones centrales; dejar multiclase como comparación guiada.

## Cuadernos y correcciones para la práctica

Los originales se conservan. Las diapositivas muestran adaptaciones propuestas, no resultados de ejecuciones nuevas.

- `14-1-Perceptron-Multicapa-Regresion.ipynb`: `Input` seguido de `Dense(1, linear)` no tiene capa oculta. Comparar el cuadrático con una capa oculta de 4 u 8 unidades. Una sola ReLU oculta aporta una única bisagra y tiene capacidad limitada.
- `14-2-Perceptron-Multicapa-Clasificacion.ipynb`: en la celda 26 usar `loss = BinaryCrossentropy()`; el original omite los paréntesis. Comparar datos de `make_blobs` y `make_circles` con y sin capa oculta.
- `14-3-Perceptron-Multicapa-Multiclase.ipynb`: el modelo original es `Dense(3, softmax)`, sin capa oculta. La presentación añade `Dense(8, relu)` para mostrar el MLP; conservar el original como referencia lineal.
- `14-4-Perceptron-Practica.ipynb`: seis variables numéricas y objetivo Stage. Separar entrenamiento/validación/prueba antes de ajustar `StandardScaler`. Verificar faltantes, duplicados y codificación de clases. No usar Name como entrada.
- Los cuadernos usan TensorFlow/Keras para redes; scikit-learn prepara datos y calcula métricas. Los encabezados originales confunden esa distinción.

## Preparación del caso real

La URL del CSV está en la celda 10 del notebook 14-4. Verificar disponibilidad antes de clase; preparar una copia local si se necesita trabajar sin conexión. Las diapositivas no afirman métricas del dataset.

Partir de `X` sin escalar y de etiquetas enteras `y`. El código de separación de la presentación produce `X_train`, `X_val` y `X_test`. Después crear las etiquetas one-hot con tres columnas para las variantes categóricas. Las diapositivas de código son fragmentos, con las importaciones del notebook correspondiente.

Registrar arquitectura, semilla, tasa, épocas y desempeño de validación. Reservar prueba para el modelo elegido. La red 6–12–6–3 aprende 183 parámetros; la red 2–4–1 aprende 17.

## Recursos y comprobación

Las figuras `relu_cuadrado` y `circulos` son ilustraciones construidas, no ajustes de Keras. Regenerar desde la raíz con `python scripts/generar_figuras_clases13_15.py`.

Compilar desde esta carpeta: `pdflatex -interaction=nonstopmode -halt-on-error clase14_multicapa.tex`, dos pasadas. No se ejecutaron TensorFlow ni los notebooks; revisar diseño y comportamiento en el entorno de clase antes de usarlos.

Para el miércoles: video de retropropagación indicado en el aula virtual por la guía. Pregunta puente: ¿cómo calcular las 183 derivadas sin perturbar cada peso por separado?
