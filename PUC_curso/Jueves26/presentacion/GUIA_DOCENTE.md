# Clase 12 · Introducción a las redes neuronales: perceptrón lineal

Primera propuesta para el jueves 26 de noviembre de 2026. Sigue las tres actividades de `../Clase12.pdf`: retroalimentación del aula invertida, fundamentos y exploración del notebook. Se adapta el estilo de `../../DL_MRI_class/DL_MRI_presentation.tex`: fondo blanco, azul oscuro, títulos subrayados, recuadros de color y ecuaciones junto a esquemas. Se recrea en TikZ el gráfico «Estructura general de una red neuronal» de la página 10/51 del PDF de MRI, colocando la motivación como función a la izquierda y su implementación como red a la derecha. Los demás diagramas también se dibujan en TikZ y las gráficas son reproducibles; la presentación no depende de la carpeta de MRI para compilar.

La versión actual contiene **37 diapositivas**, incluidos portada, cinco separadores y materiales de referencia. La **4** enumera los comportamientos biológicos junto a la ilustración de la neurona. La **5** introduce la forma general de una red artificial con un esquema rotulado, un GIF de propagación y un ejemplo numérico de pesos y sesgo. Las **6 y 7** presentan la historia. La **8** explica una función matemática con su regla, tabla de valores y gráfico; la **9** introduce la red como función ajustable. Las **10 y 11** muestran los modelos lineal y económico. La **12** explica el límite de combinar neuronas afines. Las **13 y 14** presentan el cuadrado y su entrenamiento. Las notas incluyen indicaciones para la exposición.

### Inspiración biológica: diapositivas 4 y 5

Explicar primero cinco comportamientos: recibir señales excitadoras o inhibidoras, integrarlas, generar un potencial de acción al alcanzar un umbral, transmitir información y modificar la eficacia de algunas conexiones. Usar la ilustración para ubicar dendritas, cuerpo celular, axón y terminales.

Después mostrar la forma de una red en la diapositiva 5. Las flechas rotulan entradas, una neurona, conexiones, activación y salida. Identificar los círculos como unidades que reciben señales y producen respuestas; sus conexiones llevan esas respuestas al grupo siguiente. El color representa el nivel de respuesta. Establecer oralmente la asociación con recibir, integrar y transmitir señales. La diapositiva 5 permite un ejemplo aritmético para una neurona; reservar la fórmula general y su notación para más adelante. La integración biológica está distribuida en espacio y tiempo; el modelo simplifica esa idea. El sesgo no es una estructura anatómica y el descenso por gradiente no reproduce el aprendizaje cerebral.

Abrir **`simulacion/propagacion_red.gif`** desde el enlace de la diapositiva. Muestra tres pares de entradas en una red 2–3–2–1 con parámetros fijos. En cada caso se revelan primero los datos, después las respuestas de los grupos intermedios y finalmente la salida. Las respuestas se calculan realmente: los grupos intermedios usan ReLU y la salida usa sigmoide; estos nombres y las fórmulas pueden reservarse para más adelante. El blanco con puntos suspensivos significa «por calcular», el gris con cero significa respuesta nula y el verde codifica respuestas positivas de distinta intensidad. La salida no se presenta como una probabilidad de ninguna tarea concreta.

Esta animación representa **propagación de señales, no entrenamiento**. Los puntos en movimiento y la revelación secuencial son recursos didácticos; no reproducen tiempos biológicos ni implican que las activaciones siempre sean binarias. Diferenciarla de los GIF de entrenamiento, donde sí se modifican parámetros. `simulacion/generar_red_general.py` regenera tanto el GIF como `figuras/red_general.pdf`.

Solo se rotulan los dos pesos que llegan a la primera neurona intermedia: `1.2` y `−1.0`, junto a su sesgo `−0.1`. En el primer ejemplo, `1.2×0.90 − 1.0×0.20 − 0.10 = 0.78`, que coincide con la respuesta mostrada. El borde naranja identifica esa neurona. En el GIF el cálculo se actualiza con cada par de entradas; cuando la combinación es negativa, la respuesta de esta neurona es cero por su activación ReLU. Las otras conexiones conservan sus pesos, aunque no se rotulen. Los números de los círculos son respuestas o entradas; los pesos están en las conexiones.

Cada grupo está encerrado en un recuadro para introducir el concepto de **capa**: capa de entrada, dos capas intermedias u ocultas y capa de salida. Recorrerlos de izquierda a derecha en el esquema y en el GIF. La capa de entrada presenta los datos; las intermedias y la de salida procesan las respuestas. Los recuadros indican agrupación y no son neuronas adicionales ni parámetros nuevos.

### Historia: diapositivas 6 y 7

Seguir los hitos de `Resumen12.pdf`, sección Historia, p. 1. La primera diapositiva incluye el modelo de McCulloch y Pitts (1943), el perceptrón de Rosenblatt (1958), las limitaciones destacadas por Minsky y Papert en *Perceptrons* (1969) y la retropropagación de Rumelhart, Hinton y Williams (1986). La segunda incluye LeNet y dígitos manuscritos con LeCun y sus colegas (1989), popularización de GPUs (2010), ImageNet con Hinton y sus colegas (2012) y Transformer con Vaswani et al. (2017).

Dedicar unos tres minutos al conjunto: la primera diapositiva conecta representación, aprendizaje y limitaciones; la segunda sitúa aplicaciones, cómputo y nuevas arquitecturas. Las líneas de tiempo muestran el orden de los eventos, sin distancias proporcionales al tiempo. Para 1986 se habla de difusión de la retropropagación, evitando presentar esa fecha como la invención del método. Ambas diapositivas indican el resumen como fuente.

### Función matemática y analogía con la red: diapositivas 8 y 9

Primero presentar una función como una asignación de una única salida a cada entrada. Usar `f(x) = 2x + 1`, calcular las filas de la tabla y ubicar el par `(1, 3)` en su gráfico. Aquí se conoce la regla y se aplica directamente; no hay parámetros por estimar ni entrenamiento.

En la siguiente diapositiva, introducir la red como una función con parámetros ajustables. La arquitectura determina la familia de funciones y los ejemplos permiten estimar parámetros para aproximar la relación deseada. Recorrer entrada, predicción, comparación con la referencia y actualización. Esta separación conserva la diferencia entre definir una regla y aprender una aproximación a partir de datos.

### Progresión de modelos: diapositivas 10 a 14

Abrir **`simulacion/simulacion_progresiva.html`**. Es un archivo autónomo, sin internet, con tres etapas: una relación afín de una entrada, una relación afín con dos entradas y una relación cuadrática. Cada etapa permite reproducir un entrenamiento real, consultar entradas nuevas y leer pesos, sesgos y predicciones. Cambiar de etapa reinicia su reproducción. Las demostraciones actuales también se conservan por separado en `simulacion_lineal.html`, `simulacion_multivariable.html` y `simulacion_cuadrado.html`.

1. **Una relación, una neurona:** `y = 2x + 1`. La neurona aprende `w ≈ 2` y `b ≈ 1`. Para `x = 1.5` produce aproximadamente `4`. Mostrar pendiente y desplazamiento como dos parámetros con papeles distintos.
2. **Dos variables explicativas, una respuesta:** gasto mensual en alimentación según ingreso e integrantes del hogar. Una neurona calcula `ŷ = w₁x₁ + w₂x₂ + b`. `x₁` es ingreso mensual en miles de unidades monetarias, `x₂` es número de integrantes e `y` es gasto mensual en unidades monetarias. Con 25 observaciones sintéticas se estiman `w₁ ≈ 60`, `w₂ ≈ 40` y `b ≈ 50`. Después se predice el gasto de un hogar nuevo: ingreso 2500 u.m. y tres integrantes → aproximadamente **320 u.m.** Hay dos entradas, una salida y tres parámetros; es regresión lineal múltiple.
3. **Puente conceptual, diapositiva 12:** presentar `x → f₁ → h → f₂ → ŷ` y escribir `ŷ = (f₂ ∘ f₁)(x)`. Con `f₁(x)=w₁x+b₁` y `f₂(h)=w₂h+b₂`, la composición sigue siendo `Ax+B`. Distinguir la suma ponderada de entradas dentro de una neurona de la composición de funciones entre capas. El ejemplo escalar simplifica la notación; el resultado también vale para capas afines de varias neuronas.
4. **Una relación curva:** retomar `y = x²` y la red 1–6–1 con tanh. Ahora las activaciones no lineales amplían la familia de funciones. Comparar con la recta ajustada a los mismos datos.

La arquitectura se elige según la estructura de la tarea y la precisión buscada. En esta progresión, una variable explicativa adicional añade un peso a la misma neurona; una relación curva motiva activaciones no lineales. Más salidas motivarían más neuronas de salida, pero ese no es el caso económico actual. No presentar una correspondencia universal «función más compleja = más capas»: importan también las características de entrada, el tipo de activación y la tolerancia al error.

La primera etapa se entrena con 21 datos, tasa `0.05` y 400 épocas. La etapa económica usa 25 hogares, tasa `0.02` y 6000 épocas. Los gradientes se verifican por diferencias finitas y los parámetros finales se contrastan con mínimos cuadrados. Se reservan `1.5` para la primera etapa y el cuadrado, y el par `(2.5, 3)` para la etapa económica. El entrenamiento cuadrático y su GIF se conservan sin cambios.

### Datos económicos de la diapositiva 11

Los hogares se crean cruzando ingresos de `[1, 1.5, 2, 3, 4]` miles de u.m. con tamaños de `[1, 2, 3, 4, 5]` personas. La regla sintética es `y = 60x₁ + 40x₂ + 50`, sin ruido. La diapositiva muestra seis filas identificadas del conjunto de 25; todas las observaciones se pueden desplegar en la simulación y están en **`simulacion/observaciones_hogares.csv`**. La matriz de diseño tiene rango tres, por lo que permite identificar ambos pesos y el sesgo.

Comparar hogares con igual ingreso y distinto tamaño para motivar `w₂`, y con igual tamaño y distinto ingreso para motivar `w₁`. Interpretar los incrementos como asociaciones del modelo sintético manteniendo fija la otra variable. Los datos no describen una economía real ni prueban causalidad. **Se estiman parámetros; se predice la variable respuesta.** En la simulación, la gráfica fija el número de integrantes para mostrar una sección del plano; el MSE sigue calculándose con los 25 hogares.

### Alternativas en GIF para las tres etapas

- **`simulacion/entrenamiento_lineal.gif`**: muestra cómo cambia la recta, el peso, el sesgo, la pérdida y la predicción para `x = 1.5`.
- **`simulacion/entrenamiento_multivariable.gif`**: muestra en tres dimensiones el plano `ŷ = w₁x₁ + w₂x₂ + b`, las 25 observaciones y la predicción para el hogar `(2.5, 3)`. Sus etiquetas permiten seguir los tres parámetros. El MSE incluye todos los hogares.
- **`simulacion/entrenamiento_cuadrado.gif`**: conserva la animación de la red 1–6–1 aproximando `x²`.

Los dos nuevos GIF reproducen los estados reales de los mismos entrenadores de la simulación interactiva. Se repiten automáticamente, con una pausa al principio y al final. Los valores de época indican el avance real; los estados guardados no tienen separación temporal uniforme. Los nuevos gráficos de pérdida limitan su representación inferior a `10⁻¹²`, mientras los títulos muestran el MSE numérico completo. Para regenerarlos, ejecutar `python simulacion/generar_gifs.py` con NumPy, Matplotlib y Pillow.

Se verificó la lectura de todos los fotogramas: 44 estados y 8.78 segundos por ciclo en el GIF lineal; 96 estados y 16.06 segundos en el económico. Sus pérdidas se contrastan con las calculadas a partir de los parámetros guardados. Se revisaron visualmente los estados inicial, intermedio y final de ambas animaciones.

### Motivación con datos: diapositivas 9 y 13

Recorrer primero la función ajustable y después la red que la implementa. Mostrar los pares `(-2,4)`, `(-1,1)`, `(0,0)`, `(1,1)` y `(2,4)`: las salidas son referencias con las que comparar las predicciones y ajustar los parámetros. El entrenamiento repite ese ciclo sobre los datos. Después, con los parámetros fijos, preguntar qué salida produciría la red para `1.5`.

El valor `2.25` es la **referencia que queremos aproximar**, no una predicción calculada por un modelo entrenado. Reservar ese dato para comprobar el error permite introducir la evaluación con datos nuevos. Se trata de una entrada dentro del intervalo de entrenamiento: el ejemplo no demuestra extrapolación. Los pares por sí solos no garantizan recuperar la regla del cuadrado. La diapositiva anticipa una red no lineal; conectar con el trabajo de hoy diciendo: «Empezaremos por una relación lineal como `y = 2x`, para entender primero cómo se ajustan los parámetros».

### Simulación del cuadrado: diapositiva 14

Usar la tercera etapa de **`simulacion/simulacion_progresiva.html`** o abrir **`simulacion/simulacion_cuadrado.html`** para mostrar solo el cuadrado. Ambos funcionan sin internet ni instalación. El HTML reproduce estados reales del entrenamiento, permite recorrer las épocas, consultar entradas de −2 a 2 y observar cualquiera de las seis neuronas. El PDF muestra tres estados estáticos y ofrece un enlace al HTML. Como alternativa, abrir `simulacion/entrenamiento_cuadrado.gif`.

Secuencia sugerida, de unos cinco minutos:

1. Mostrar el estado inicial. Preguntar si la curva ya ajusta los ejemplos.
2. Reproducir el entrenamiento y detenerlo. Observar los cambios de la curva y la pérdida.
3. Seleccionar la neurona 1 y leer el cálculo **peso × entrada + sesgo**. Relacionar cada número con `z = wx + b` y su respuesta `tanh(z)`. La tabla permite seguir los seis pesos de entrada, los seis sesgos y los seis pesos de salida; la salida tiene además un sesgo propio.
4. Ir al último estado y consultar `1.5`. La predicción es aproximadamente **2.3071**, frente a la referencia **2.25**. Cambiar la entrada: las predicciones cambian con parámetros fijos.
5. Activar «Comparar con una neurona lineal». Mostrar que una recta ajustada a los mismos datos conserva un error mayor porque no puede representar la curva. Regresar a una sola neurona para estudiar el cálculo en el notebook de clase.

La red tiene arquitectura **1–6–1**, activación **tanh** en las seis neuronas intermedias y salida afín: `a_j = tanh(w_j*x + b_j)` y `ŷ = Σ v_j*a_j + c`. Son **19 parámetros entrenables**. Se ajustan por descenso por gradiente de lote completo, tasa `0.02`, semilla `7` y `12 000` épocas. La entrada original `x`, sin transformarla en `x²`, se proporciona al modelo; el cuadrado se usa solo para generar referencias y comprobar errores.

El entrenamiento usa **21 pares** uniformemente espaciados en `[−2, 2]`; la tabla anterior ilustra cinco de ellos. `1.5` no aparece en esos 21 valores. El MSE de entrenamiento final es aproximadamente **0.003215**. La predicción es una aproximación y esta demostración evalúa interpolación. Los estados exportados se guardan con mayor frecuencia al principio para visualizar mejor el aprendizaje; el control muestra la época real.

El código reproducible es `simulacion/generar_simulacion.py`, que necesita NumPy, Matplotlib y Pillow. Al ejecutarlo genera el HTML autónomo, el GIF, la trayectoria, un resumen de métricas y las figuras usadas en la diapositiva. Para modificar el diseño del HTML, editar `simulacion/plantilla.html` y regenerar.

## Secuencia propuesta

Duración provisional: **120 minutos**, pendiente de confirmar. Los separadores de sección permiten detener la exposición para trabajar con los estudiantes. La idea es alternar **predecir → ejecutar → explicar**.

| Tiempo | Bloque | Intervención y evidencia de aprendizaje |
| --- | --- | --- |
| 0–10 min | Recuperar la lectura previa | Pregunta inicial de la guía; discutir las tres afirmaciones y recoger dos dudas de los materiales previos. |
| 10–25 min | Introducir la neurona | Analogía biológica, hitos históricos y esquema general. |
| 25–45 min | Progresión de modelos | Una relación lineal, dos entradas económicas con una respuesta, límite de componer funciones afines y paso al cuadrado. Usar la simulación para identificar pesos, sesgos y activaciones. |
| 45–65 min | Explicar el aprendizaje | Conectar predicción, MSE, regla de la cadena y actualización. Resolver un paso en pizarra y discutir la tasa. |
| 65–85 min | Notebook: Ejemplo 1 | Ejecutar en orden; predecir la pendiente y experimentar con tres tasas. Registrar peso y pérdida final. |
| 85–105 min | Notebook: Ejemplo 2 | Justificar el sesgo, ejecutar el modelo afín y comparar inicializaciones. |
| 105–110 min | Extensión por bloques | Contar pasos por época y comparar lotes. Se puede sustituir por discusión de dudas. |
| 110–120 min | Cierre | Discutir límites de una neurona lineal; recoger las tres respuestas de salida y recordar la preparación del lunes. |

**Si dura 90 minutos:** dedicar 8 minutos al diagnóstico, 12 a la introducción, 15 a la progresión, 15 al aprendizaje, 15 a cada ejemplo del notebook y 10 al cierre. Omitir la extensión de entrenamiento por bloques. Mostrar una sola corrida del experimento de inicialización; dejar la comparación de 1000 épocas como demostración docente.

**Si dura 180 minutos:** añadir 15 minutos de pausa, 15 de derivación en parejas, 15 de exploración de tasas, 10 de comparación con igual número de actualizaciones y 5 de puesta en común. No es necesario introducir temas nuevos.

## Correspondencia con los materiales

- `../03Est-RedesNeuronales.pdf`: biología, perceptrón, activaciones y descenso del gradiente. Recuperar las dudas de sus interacciones con ChatGPT, videos y lectura; no repetir toda la preparación.
- `../Resumen12.pdf`: notación, combinación, activación identidad, MSE y gradientes. El vector de pesos se presenta primero; las derivadas se desarrollan con una entrada, como en el notebook.
- `../12-Perceptron-Lineal.ipynb`: usar **Ejemplo 1**, **Ejemplo 2** y **Entrenamiento por bloques**, en ese orden. La numeración posicional desde 1 es 7–18, 22–33 y 36–38, respectivamente; los encabezados son la referencia principal si cambian las celdas.
- `../../Lunes30/Clase13.pdf`: el lunes corresponde a sigmoide, softmax y pérdidas de clasificación. Hoy basta con situar esas activaciones, sin desarrollar sus gradientes.

## Preguntas y resultados esperados

1. **Diagnóstico:** falso, falso, verdadero. La neurona artificial es una simplificación; la identidad, por ejemplo, no devuelve solo 0 o 1.
2. **Predicción manual:** con los valores de la diapositiva, `z = 0.2`; sin sesgo, `z = 0`. Hay dos pesos y un sesgo.
3. **MSE:** los residuos con signos opuestos podrían cancelarse si se promediaran directamente. El cuadrado evita esa cancelación.
4. **Paso de gradiente:** los gradientes son `-12` y `-6`; el siguiente modelo tiene `w = 2.2`, `b = 0.6`. La pérdida cero es particular de ese dato y esa tasa.
5. **Ejemplo 1, 50 épocas, tasa 0.1:** `w ≈ 1.870298`, `b = 0`, MSE final `≈ 0.028635`. El ruido impide exigir pérdida cero; 50 épocas tampoco garantizan convergencia completa.
6. **Ejemplo 2, 100 épocas, tasa 0.1:** `w ≈ 3.328541`, `b ≈ 3.310018`, MSE final `≈ 0.051544`. No exigir que se recuperen exactamente los parámetros generadores `4` y `3`.
7. **Tasas del Ejemplo 1:** `0.001` avanza lentamente, `0.1` reduce la pérdida y `5.0` diverge con estos datos. No son umbrales universales.
8. **Inicialización:** cambiar solamente `random_state` de `fit`, conservando los datos. Con un número finito de épocas las salidas pueden diferir; este problema cuadrático tiene un mínimo único y, con una tasa estable, las trayectorias convergen hacia él.
9. **Lotes:** con 30 datos y tamaños 30, 10 y 1, hay 1, 3 y 30 actualizaciones por época. El bloque del notebook conserva el orden de los datos; no baraja muestras. Un lote menor no es automáticamente mejor.
10. **Limitaciones:** más épocas no convierten una recta en una parábola. Nuevas características o capas con activaciones no lineales amplían la familia del modelo.

## Aclaraciones que conviene hacer explícitas

- En `Resumen12.pdf`, p. 2, aparece un factor cero al derivar respecto al sesgo. Para `ŷ = wx + b`, la derivada correcta es `∂L/∂b = (2/N) Σ(ŷ − y)`. En el primer ejemplo se usa `ŷ = wx`: el sesgo se fija en cero y no se entrena. Las diapositivas distinguen ambos casos.
- Una **época** recorre todos los datos. Solo coincide con una actualización cuando se usa lote completo.
- El modelo práctico es una neurona con activación identidad y pérdida cuadrática, equivalente a regresión lineal. Distinguirlo del perceptrón clásico de clasificación con escalón.
- Las capas afines encadenadas sin activaciones no lineales siguen siendo afines. Evitar afirmar que cualquier red aproxima cualquier función sin condiciones.
- La pérdida mostrada durante `fit` en los dos primeros ejemplos se calcula antes de actualizar los parámetros de esa iteración. Para comparar los modelos devueltos, recalcular `L(s(a(X, w, b)), y)`; las figuras usan esa pérdida final.

## Preparación de la demostración

1. Abrir el notebook con kernel Python 3 y comprobar NumPy y Matplotlib.
2. Reiniciar el kernel y ejecutar las secciones en orden: el notebook redefine `a`, `grad_L` y `fit`. Los experimentos de la presentación deben ejecutarse dentro de su sección correspondiente.
3. En las animaciones, `actualizar` vuelve a llamar a `fit` con su tasa por defecto. Para animar otra tasa, pasar `lr=...` también en esa llamada; cambiar una corrida previa no cambia la animación.
4. La salida HTML5 de Matplotlib puede requerir FFmpeg. Si no está disponible, usar los gráficos estáticos de la presentación o cambiar localmente la representación a `rc('animation', html='jshtml')`.
5. Los PDF y el notebook de entrada se conservan intactos. Los experimentos de las diapositivas son bloques adicionales para copiar al trabajar en clase.

## Archivos y compilación

- `clase12_perceptron_lineal.tex`: presentación editable, con notas ocultas mediante `\note{...}`.
- `clase12_perceptron_lineal.pdf`: versión para proyectar.
- `generar_figuras.py` y `figuras/*.pdf`: figuras vectoriales con los datos y las semillas del notebook; no hace falta regenerarlas para compilar.
- `figuras/estructura_red.tex`: recreación vectorial editable del gráfico de MRI, con la función a la izquierda y la red a la derecha. Se inserta con `\input`.
- `figuras/NN_squeleton.png`: imagen original de MRI conservada como referencia; la versión actual inserta la recreación vectorial.
- `figuras/neurona_biologica.tex`: ilustración vectorial original en TikZ; se inserta con `\input`. Representa dendritas, cuerpo celular, axón y terminales como apoyo a la analogía, sin pretender reproducir toda la fisiología neuronal.
- `figuras/red_general.pdf` y `simulacion/propagacion_red.gif`: esquema rotulado y recorrido de señales de la diapositiva 5. Se regeneran con `simulacion/generar_red_general.py`.
- `simulacion/simulacion_cuadrado.html`: demostración interactiva autónoma; `entrenamiento_cuadrado.gif` es la alternativa animada. `generar_simulacion.py` reproduce el entrenamiento y `resumen.json` conserva sus métricas.
- `simulacion/simulacion_progresiva.html`: secuencia de tres etapas en un solo archivo autónomo. `generar_progresion.py` entrena los ejemplos lineales y los combina con la demostración cuadrática existente; `resumen_progresion.json` conserva sus métricas. Las plantillas `plantilla_afin.html`, `plantilla_multivariable.html` y `plantilla_progresiva.html` permiten editar la presentación interactiva.
- `simulacion/observaciones_hogares.csv`: las 25 observaciones sintéticas del ejemplo económico, con unidades en los nombres de las columnas.
- `simulacion/entrenamiento_lineal.gif` y `simulacion/entrenamiento_multivariable.gif`: animaciones de las dos primeras etapas. `generar_gifs.py` permite reproducirlas sin regenerar el HTML ni la presentación.
- `figuras/simulacion_lineal.pdf`: estados reales del primer ejemplo lineal para la presentación.
- `figuras/simulacion_cuadrado.pdf` y `figuras/simulacion_resultados.tex`: estados y resultados reales del entrenamiento que se insertan en la presentación.
- `.build/`: archivos auxiliares de compilación, excluidos de Git.

Desde esta carpeta, con Python y LaTeX disponibles en el entorno:

```powershell
# Opcional: regenerar las cinco figuras.
python generar_figuras.py

# Opcional: regenerar la simulación del cuadrado y sus figuras.
python simulacion/generar_simulacion.py

# Regenerar las etapas lineales y la secuencia autónoma; ejecutar después
# del comando anterior si también se modificó el ejemplo cuadrático.
python simulacion/generar_progresion.py

# Regenerar los GIF de las etapas lineal y económica.
python simulacion/generar_gifs.py

# Regenerar el esquema general de la red y su GIF de propagación.
python simulacion/generar_red_general.py

# Compilar dos veces para actualizar referencias y total de diapositivas.
pdflatex -interaction=nonstopmode -halt-on-error clase12_perceptron_lineal.tex
pdflatex -interaction=nonstopmode -halt-on-error clase12_perceptron_lineal.tex
```

Se requieren Beamer, Latin Modern, Babel en español, TikZ, listings y booktabs. Para una copia docente con las notas intercaladas, cambiar `hide notes` por `show notes` y compilar con otro nombre mediante `-jobname=clase12_notas`; así se conserva el PDF de proyección.

El cierre mantiene la indicación de la guía: **sin tarea evaluada nueva**. Recordar los dos videos sobre funciones de activación publicados en el aula virtual como preparación para el lunes.

## Validación de esta versión

Se ejecutaron todas las celdas de código del notebook original con un backend no interactivo, sin modificarlo; esta comprobación no renderiza sus animaciones HTML5. La simulación cuadrática verifica las 19 derivadas por diferencias finitas, la reducción de pérdida, una malla de entradas nuevas y la exclusión de `1.5` del entrenamiento. Se verificaron los 143 estados de su GIF. Las nuevas etapas afines verifican sus gradientes y contrastan los parámetros finales con mínimos cuadrados. En Edge se probaron las tres pestañas, reproducción, pausa, reinicio, avance, selección de neurona, cambio de entrada y una pantalla estrecha, sin errores de JavaScript. Las predicciones del navegador concuerdan con NumPy; el cuadrado mantiene una diferencia menor que `1e-8`. La presentación se compiló con pdfLaTeX, sin advertencias ni desbordamientos, y se revisaron visualmente las diapositivas de la progresión.
