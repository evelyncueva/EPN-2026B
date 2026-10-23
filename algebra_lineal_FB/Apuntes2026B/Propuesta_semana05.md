# Propuesta de material — Semana 05, semestre 2026-B

Dos clases de 120 minutos. La distribución es: **clase 1, enlace con el teorema de equivalencias y regla de Cramer; clase 2, concepto de espacio vectorial, ejemplos y operaciones durante toda la sesión**. Los tiempos incluyen trabajo estudiantil y puesta en común.

## Punto de partida y adaptación del material

Se revisaron los apuntes disponibles de 2026B: semana 02 clase 02, semana 03 clase 01 y las dos clases de la semana 04. No se encontró un archivo de la semana 01 en esta carpeta. Las referencias de 2025A son `Primer bimestre/Semana 06 Clase 02.tex` y `Primer bimestre/Semana 07 Clase 01.tex`.

La semana 04 ya presenta inversa, interpretación geométrica del determinante, cofactores, propiedades, eliminación y criterio de invertibilidad. La semana 05 debe usar estos resultados para interpretar y decidir, sin volver a desarrollar toda la teoría.

De 2025A se conservan las equivalencias de invertibilidad, Cramer y la definición formal de espacio vectorial. Se propone adaptar lo siguiente:

- Sustituir el ejemplo central de Cramer de orden tres por uno de orden dos con significado geométrico y continuidad con la semana 02.
- Conservar una motivación breve con desplazamientos y el paralelogramo; presentar después la definición y ejemplos de distintos tipos de vectores.
- Explicar que los axiomas de los ejemplos usuales se heredan de los números reales, por componentes, coeficientes o valores, sin desarrollar ocho demostraciones.
- Incluir matrices, polinomios y funciones, y una observación sobre operaciones no usuales motivada por ganancias de audio. Posponer el estudio sistemático de subespacios y las demostraciones de unicidad del neutro e inverso.
- Corregir la pregunta del ejercicio homogéneo con parámetro de 2025A: todo sistema homogéneo tiene solución trivial; lo que corresponde preguntar es cuándo es **la única**.

## Clase 1 — Equivalencias de invertibilidad y regla de Cramer

### Resultados de aprendizaje

Relacionar determinante, rango, inversa y unicidad mediante el teorema 1 de semana 06 clase 02 de 2025A; aplicar Cramer en sistemas pequeños; comprobar la solución e interpretar sus componentes.

### Secuencia de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
|---|---|---|
| 0–10 | Enunciar el teorema de equivalencias y enlazarlo con la semana 04. | Reconocer distintas formas de expresar la invertibilidad. |
| 10–20 | Un ejemplo breve: matriz del robot de la semana 02. | Deducir rango, inversa y unicidad desde un solo determinante. |
| 20–35 | Presentar Cramer y construir las matrices con columnas reemplazadas. | Identificar la hipótesis y cada matriz. |
| 35–55 | Resolver el objetivo del robot y comprobar el resultado. | Cálculo breve, sustitución e interpretación. |
| 55–75 | Aplicación guiada: producción de dos tipos de kits. | Plantear el sistema antes de usar la fórmula. |
| 75–95 | Trabajo en parejas: un sistema de orden tres con cálculos cortos. | Transferir el procedimiento sin concentrarse en la aritmética. |
| 95–110 | Discusión: cuándo se aplica Cramer y qué ocurre si el determinante es cero. | Distinguir las limitaciones del método de la clasificación del sistema. |
| 110–120 | Salida individual y corrección. | Reemplazar columnas y justificar la aplicabilidad. |

### Enlace breve: teorema de equivalencias

Retomar el **teorema 1 de semana 06 clase 02 de 2025A**. Para una matriz cuadrada real de orden \(n\), son equivalentes:

1. \(A\) es invertible o no singular.
2. \(Ax=0\) tiene únicamente la solución trivial.
3. \(A\) es equivalente por filas a \(I_n\).
4. \(\operatorname{rang}(A)=n\).
5. \(Ax=b\) tiene una única solución para cada \(b\in\mathbb R^n\).
6. \(\det(A)\ne0\).

Presentarlo como síntesis de resultados ya estudiados. Basta recordar que tener un pivote en cada columna conecta rango, reducción e invertibilidad, y que el determinante reconoce esta misma condición. No añadir un taller de cálculo de determinantes.

**Único ejemplo del enlace.** Retomar los desplazamientos del robot de semana 02:

\[
u=(2,1),\qquad v=(1,3),\qquad
A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad \det(A)=5.
\]

Sin calcular la inversa ni reducir la matriz, pedir que completen: el rango es 2, la matriz es invertible, el sistema homogéneo solo tiene la solución trivial y cada objetivo real tiene una única solución. La siguiente pregunta conduce directamente a Cramer: **¿cómo obtener esa solución usando determinantes?**

Para el modelo geométrico se permiten intensidades reales; una intensidad negativa significa invertir el movimiento. Si solo se admiten activaciones enteras no negativas, comprobar esa restricción física después de resolver.

### Regla de Cramer: resolver el objetivo conocido

**Teorema.** Para \(A\in\mathbb R^{n\times n}\) con \(\det(A)\ne0\), la solución de \(Ax=b\) cumple

\[
x_j=\frac{\det(A^{(j)})}{\det(A)},
\]

donde \(A^{(j)}\) reemplaza la columna \(j\) de \(A\) por \(b\). Usar esta notación evita confundirla con el menor \(A_{ij}\) de la semana 04.

Para el robot y \(b=(8,9)\):

\[
A^{(1)}=\begin{pmatrix}8&1\\9&3\end{pmatrix},\qquad
A^{(2)}=\begin{pmatrix}2&8\\1&9\end{pmatrix}.
\]

Así, \(x_1=15/5=3\), \(x_2=10/5=2\), y se comprueba \(3u+2v=(8,9)\).

**Lectura geométrica:** estos números indican cuánto aporta cada dirección para construir el objetivo. En orden dos, las fórmulas también comparan áreas orientadas.

**Práctica:** para el mismo robot, alcanzar \((5,5)\). Clave: \(x_1=x_2=1\). Preguntar qué ocurriría con Cramer si ambos mecanismos fueran paralelos: la fórmula no se aplica, y no debe interpretarse una división entre cero como clasificación del sistema.

Presentar Cramer como una fórmula útil para sistemas pequeños y expresiones con parámetros. Para resolver sistemas grandes, conservar la eliminación como herramienta principal. La demostración general de Cramer puede quedar para lectura posterior.

### Aplicación guiada: producción de kits

Retomar el taller de la semana 04: cada kit \(P\) requiere dos horas de corte y una de ensamblaje; cada kit \(Q\), una hora de cada actividad. Se usarán por completo 11 horas de corte y 7 de ensamblaje.

1. Definir las incógnitas y plantear \(2p+q=11\), \(p+q=7\).
2. Comprobar que el determinante es \(2-1=1\) antes de aplicar Cramer.
3. Reemplazar columnas: \(p=(11-7)/1=4\), \(q=(14-11)/1=3\).
4. Comprobar horas utilizadas e interpretar las cantidades de kits.

Conectar con la inversa de semana 04: cambió el procedimiento, pero se obtiene la misma producción. Preguntar qué indicaría una cantidad negativa o no entera.

### Práctica en parejas: orden tres sin cálculos extensos

Usar el ejercicio final de semana 06 clase 02 de 2025A:

\[
\left\{\begin{aligned}
3x+2y+z&=2,\\
2x+2y+z&=2,\\
x+y+z&=1.
\end{aligned}\right.
\]

El determinante de la matriz de coeficientes es 1. Los determinantes al reemplazar las columnas son, respectivamente, 0, 1 y 0; así, la solución es \((0,1,0)\). Repartir los numeradores entre integrantes y verificar juntos la solución en el sistema original. Elegir operaciones o cofactores convenientes para evitar expansiones largas.

### Alcance del método y salida

Para \(S=\begin{pmatrix}2&4\\1&2\end{pmatrix}\), el determinante es cero: Cramer no se aplica. Comparar brevemente los lados derechos \((8,4)\), con infinitas soluciones reales, y \((8,9)\), sin solución. La proporcionalidad de las ecuaciones permite reconocer ambos casos sin otro desarrollo completo.

**Salida individual:** para la matriz del robot y el objetivo \((5,5)\), escribir las matrices de Cramer, resolver y comprobar. Clave: numeradores 5 y 5, solución \((1,1)\). Explicar por qué la fórmula no puede aplicarse si el denominador es cero.

## Clase 2 — Concepto de espacio vectorial, ejemplos y operaciones

### Resultados de aprendizaje

Identificar el conjunto, los escalares y las dos operaciones de un espacio vectorial real; reconocer números, tuplas, matrices, polinomios y funciones como vectores; efectuar sus operaciones e identificar neutros e inversos. Comprender que otras operaciones pueden dar una estructura vectorial diferente sobre un mismo conjunto.

### Secuencia de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
|---|---|---|
| 0–10 | Suma y escala de desplazamientos; un paralelogramo. | Interpretar suma, inverso y cero en el plano. |
| 10–30 | Definición, clausura y lectura de los axiomas. | Distinguir vectores, escalares y operaciones. |
| 30–40 | Ejemplos conocidos: R, R² y R³. | Reconocer propiedades heredadas de los reales sin repetir demostraciones. |
| 40–70 | Matrices de tamaño fijo, polinomios de grado acotado y funciones de dominio común. | Calcular sumas y múltiplos, e identificar los respectivos neutros e inversos. |
| 70–90 | Observación y ejemplo de ganancias de audio. | Comprender operaciones no usuales y el papel del cambio logarítmico de coordenadas. |
| 90–110 | Ejercicios de operaciones y discusión en parejas. | Transferir las operaciones a diferentes objetos. |
| 110–120 | Salida individual y puesta en común. | Explicar por qué el conjunto solo no determina el espacio vectorial. |

### Alcance y decisiones didácticas

Conservar una sola figura geométrica, con u=(2,1), v=(1,3) y su suma. Retirar el desarrollo de rectas, planos y el criterio de subespacios; reservarlo para su estudio posterior. Mantener la definición formal completa y explicar la clausura. Aclarar que el producto escalar aquí significa multiplicar por un número y no el producto punto.

En R, R², R³ y Rⁿ con sus operaciones usuales, los axiomas se heredan de los reales. No afirmar lo mismo de cualquier subconjunto: el primer cuadrante sirve como contraejemplo breve.

En matrices reales de tamaño fijo, operar entrada por entrada; el neutro es la matriz nula. En P_n incluir todos los polinomios de grado **a lo sumo n**, incluido el cero; operar por coeficientes. En F(R,R), sumar y escalar punto a punto; el neutro es la función idénticamente nula. No confundir estas operaciones con multiplicación matricial o composición de funciones.

### Observación aplicada: otras operaciones

Usar V=(0,∞) con g ⊕ h = gh y α ⊙ g = g^α, con escalares reales. El neutro es 1, el inverso aditivo de g es 1/g y 0 ⊙ g = 1. El cambio biyectivo φ(g)=ln(g) transforma estas operaciones en suma y producto escalar usuales de R, lo que justifica todos los axiomas. Mostrar además una distributividad usando propiedades de potencias.

Motivación: dos factores positivos de ganancia de amplitud aplicados sucesivamente se multiplican. Al usar D(g)=20 log10(g), las ganancias en decibelios se suman. Dos factores 2 producen un factor 4: aproximadamente 6.02+6.02=12.04 dB. Esto se usa en software de audio; la estructura vectorial propuesta es una interpretación matemática de esa regla, no una afirmación sobre cómo está implementado el software. Excluir la ganancia 0. Fuente de la aplicación: [MathWorks, dB Gain](https://www.mathworks.com/help/dsp/ref/dbgain.html).

### Ejercicios y claves docentes

- Reconocer vectores y neutros en los seis espacios presentados. Todos los escalares son reales; el objeto que actúa como vector cambia.
- Con A=((1,-2),(0,3)) y B=((2,1),(-1,0)), obtener 2A−B=((0,-5),(1,6)) y A+(−A)=0.
- Para p=1−t+2t² y q=3+t−t², obtener p+q=4+t² y 2p−q=−1−3t+5t². Ambos pertenecen a P₂. Los polinomios t² y −t² muestran por qué grado exactamente 2 no define un espacio con las operaciones usuales.
- Con f(t)=t² y g(t)=t+1, obtener (f+g)(t)=t²+t+1 y (2f−g)(t)=2t²−t−1; en t=2 valen 7 y 5.
- Con las operaciones de ganancias: 4 ⊕ 1/2 = 2, (1/2) ⊙ 4 = 2, (−1) ⊙ 4 = 1/4 y 4 ⊕ (1/4) = 1 = 0_V.
- Salida: precisar conjunto, escalares y operaciones. Los positivos con operaciones usuales no admiten todos los múltiplos reales ni contienen el cero usual.

## Trabajo autónomo y alcance de los apuntes

Después de la clase 2, completar operaciones con matrices, polinomios y funciones e identificar los neutros. El ejemplo de ganancias permite una primera lectura de operaciones distintas; no exigir ocho verificaciones aisladas como tarea. La clasificación de subespacios queda para una sesión posterior.

Los apuntes estudiantiles están en `Semana05_clase01.tex` y `Semana05_clase02.tex`; las claves y tiempos de esta propuesta son para el docente. La clase 2 se dedica íntegramente a espacios vectoriales, sin trasladar a ella ejercicios pendientes de Cramer.
