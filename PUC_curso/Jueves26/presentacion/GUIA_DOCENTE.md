# Clase 12 · Introducción a las redes neuronales: perceptrón lineal

Primera propuesta para el jueves 26 de noviembre de 2026. Sigue las tres actividades de `../Clase12.pdf`: retroalimentación del aula invertida, fundamentos y exploración del notebook. Se adapta el estilo de `../../DL_MRI_class/DL_MRI_presentation.tex`: fondo blanco, azul oscuro, títulos subrayados, recuadros de color y ecuaciones junto a esquemas. Se recrea en TikZ el gráfico «Estructura general de una red neuronal» de la página 10/51 del PDF de MRI, colocando la motivación como función a la izquierda y su implementación como red a la derecha. Los demás diagramas también se dibujan en TikZ y las gráficas son reproducibles; la presentación no depende de la carpeta de MRI para compilar.

La versión actual contiene **36 diapositivas**, incluidos portada, cinco separadores y materiales de referencia. La **5** presenta una ilustración de la neurona biológica, sin fórmulas. Las **6 y 7** recogen los ocho hitos históricos de `Resumen12.pdf`. La **8** motiva la red como función ajustable. La **9** comienza con una entrada y una salida lineal; la **10** introduce dos variables económicas explicativas y una sola respuesta. La **11** muestra que componer neuronas afines sigue produciendo una función afín. Las **12 y 13** pasan al cuadrado y a su entrenamiento con una red no lineal. Las notas de cada diapositiva incluyen preguntas o indicaciones para la exposición.

### Historia: diapositivas 6 y 7

Seguir los hitos de `Resumen12.pdf`, sección Historia, p. 1. La primera diapositiva incluye el modelo de McCulloch y Pitts (1943), el perceptrón de Rosenblatt (1958), las limitaciones destacadas por Minsky y Papert en *Perceptrons* (1969) y la retropropagación de Rumelhart, Hinton y Williams (1986). La segunda incluye LeNet y dígitos manuscritos con LeCun y sus colegas (1989), popularización de GPUs (2010), ImageNet con Hinton y sus colegas (2012) y Transformer con Vaswani et al. (2017).

Dedicar unos tres minutos al conjunto: la primera diapositiva conecta representación, aprendizaje y limitaciones; la segunda sitúa aplicaciones, cómputo y nuevas arquitecturas. Las líneas de tiempo muestran el orden de los eventos, sin distancias proporcionales al tiempo. Para 1986 se habla de difusión de la retropropagación, evitando presentar esa fecha como la invención del método. Ambas diapositivas indican el resumen como fuente.

### Progresión de modelos: diapositivas 9 a 13

Abrir **`simulacion/simulacion_progresiva.html`**. Es un archivo autónomo, sin internet, con tres etapas: una relación afín de una entrada, una relación afín con dos entradas y una relación cuadrática. Cada etapa permite reproducir un entrenamiento real, consultar entradas nuevas y leer pesos, sesgos y predicciones. Cambiar de etapa reinicia su reproducción. Las demostraciones actuales también se conservan por separado en `simulacion_lineal.html`, `simulacion_multivariable.html` y `simulacion_cuadrado.html`.

1. **Una relación, una neurona:** `y = 2x + 1`. La neurona aprende `w ≈ 2` y `b ≈ 1`. Para `x = 1.5` produce aproximadamente `4`. Mostrar pendiente y desplazamiento como dos parámetros con papeles distintos.
2. **Dos variables explicativas, una respuesta:** gasto mensual en alimentación según ingreso e integrantes del hogar. Una neurona calcula `ŷ = w₁x₁ + w₂x₂ + b`. `x₁` es ingreso mensual en miles de unidades monetarias, `x₂` es número de integrantes e `y` es gasto mensual en unidades monetarias. Con 25 observaciones sintéticas se estiman `w₁ ≈ 60`, `w₂ ≈ 40` y `b ≈ 50`. Después se predice el gasto de un hogar nuevo: ingreso 2500 u.m. y tres integrantes → aproximadamente **320 u.m.** Hay dos entradas, una salida y tres parámetros; es regresión lineal múltiple.
3. **Puente conceptual:** sustituir las expresiones de dos neuronas afines en una tercera. El resultado sigue siendo `Ax + B`: añadir capas o neuronas con identidad no introduce curvatura.
4. **Una relación curva:** retomar `y = x²` y la red 1–6–1 con tanh. Ahora las activaciones no lineales amplían la familia de funciones. Comparar con la recta ajustada a los mismos datos.

La arquitectura se elige según la estructura de la tarea y la precisión buscada. En esta progresión, una variable explicativa adicional añade un peso a la misma neurona; una relación curva motiva activaciones no lineales. Más salidas motivarían más neuronas de salida, pero ese no es el caso económico actual. No presentar una correspondencia universal «función más compleja = más capas»: importan también las características de entrada, el tipo de activación y la tolerancia al error.

La primera etapa se entrena con 21 datos, tasa `0.05` y 400 épocas. La etapa económica usa 25 hogares, tasa `0.02` y 6000 épocas. Los gradientes se verifican por diferencias finitas y los parámetros finales se contrastan con mínimos cuadrados. Se reservan `1.5` para la primera etapa y el cuadrado, y el par `(2.5, 3)` para la etapa económica. El entrenamiento cuadrático y su GIF se conservan sin cambios.

### Datos económicos de la diapositiva 10

Los hogares se crean cruzando ingresos de `[1, 1.5, 2, 3, 4]` miles de u.m. con tamaños de `[1, 2, 3, 4, 5]` personas. La regla sintética es `y = 60x₁ + 40x₂ + 50`, sin ruido. La diapositiva muestra seis filas identificadas del conjunto de 25; todas las observaciones se pueden desplegar en la simulación y están en **`simulacion/observaciones_hogares.csv`**. La matriz de diseño tiene rango tres, por lo que permite identificar ambos pesos y el sesgo.

Comparar hogares con igual ingreso y distinto tamaño para motivar `w₂`, y con igual tamaño y distinto ingreso para motivar `w₁`. Interpretar los incrementos como asociaciones del modelo sintético manteniendo fija la otra variable. Los datos no describen una economía real ni prueban causalidad. **Se estiman parámetros; se predice la variable respuesta.** En la simulación, la gráfica fija el número de integrantes para mostrar una sección del plano; el MSE sigue calculándose con los 25 hogares.

### Motivación con datos: diapositivas 8 y 12

Recorrer primero la función ajustable y después la red que la implementa. Mostrar los pares `(-2,4)`, `(-1,1)`, `(0,0)`, `(1,1)` y `(2,4)`: las salidas son referencias con las que comparar las predicciones y ajustar los parámetros. El entrenamiento repite ese ciclo sobre los datos. Después, con los parámetros fijos, preguntar qué salida produciría la red para `1.5`.

El valor `2.25` es la **referencia que queremos aproximar**, no una predicción calculada por un modelo entrenado. Reservar ese dato para comprobar el error permite introducir la evaluación con datos nuevos. Se trata de una entrada dentro del intervalo de entrenamiento: el ejemplo no demuestra extrapolación. Los pares por sí solos no garantizan recuperar la regla del cuadrado. La diapositiva anticipa una red no lineal; conectar con el trabajo de hoy diciendo: «Empezaremos por una relación lineal como `y = 2x`, para entender primero cómo se ajustan los parámetros».

### Simulación del cuadrado: diapositiva 13

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
- `simulacion/simulacion_cuadrado.html`: demostración interactiva autónoma; `entrenamiento_cuadrado.gif` es la alternativa animada. `generar_simulacion.py` reproduce el entrenamiento y `resumen.json` conserva sus métricas.
- `simulacion/simulacion_progresiva.html`: secuencia de tres etapas en un solo archivo autónomo. `generar_progresion.py` entrena los ejemplos lineales y los combina con la demostración cuadrática existente; `resumen_progresion.json` conserva sus métricas. Las plantillas `plantilla_afin.html`, `plantilla_multivariable.html` y `plantilla_progresiva.html` permiten editar la presentación interactiva.
- `simulacion/observaciones_hogares.csv`: las 25 observaciones sintéticas del ejemplo económico, con unidades en los nombres de las columnas.
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

# Compilar dos veces para actualizar referencias y total de diapositivas.
pdflatex -interaction=nonstopmode -halt-on-error clase12_perceptron_lineal.tex
pdflatex -interaction=nonstopmode -halt-on-error clase12_perceptron_lineal.tex
```

Se requieren Beamer, Latin Modern, Babel en español, TikZ, listings y booktabs. Para una copia docente con las notas intercaladas, cambiar `hide notes` por `show notes` y compilar con otro nombre mediante `-jobname=clase12_notas`; así se conserva el PDF de proyección.

El cierre mantiene la indicación de la guía: **sin tarea evaluada nueva**. Recordar los dos videos sobre funciones de activación publicados en el aula virtual como preparación para el lunes.

## Validación de esta versión

Se ejecutaron todas las celdas de código del notebook original con un backend no interactivo, sin modificarlo; esta comprobación no renderiza sus animaciones HTML5. La simulación cuadrática verifica las 19 derivadas por diferencias finitas, la reducción de pérdida, una malla de entradas nuevas y la exclusión de `1.5` del entrenamiento. Se verificaron los 143 estados de su GIF. Las nuevas etapas afines verifican sus gradientes y contrastan los parámetros finales con mínimos cuadrados. En Edge se probaron las tres pestañas, reproducción, pausa, reinicio, avance, selección de neurona, cambio de entrada y una pantalla estrecha, sin errores de JavaScript. Las predicciones del navegador concuerdan con NumPy; el cuadrado mantiene una diferencia menor que `1e-8`. La presentación se compiló con pdfLaTeX, sin advertencias ni desbordamientos, y se revisaron visualmente las diapositivas de la progresión.
