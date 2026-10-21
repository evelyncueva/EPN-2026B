# Propuesta de material — Semana 05, semestre 2026-B

Dos clases de 120 minutos. La distribución es: **clase 1, enlace con el teorema de equivalencias y regla de Cramer; clase 2, introducción geométrica a espacios vectoriales durante toda la sesión**. Los tiempos incluyen trabajo estudiantil y puesta en común.

## Punto de partida y adaptación del material

Se revisaron los apuntes disponibles de 2026B: semana 02 clase 02, semana 03 clase 01 y las dos clases de la semana 04. No se encontró un archivo de la semana 01 en esta carpeta. Las referencias de 2025A son `Primer bimestre/Semana 06 Clase 02.tex` y `Primer bimestre/Semana 07 Clase 01.tex`.

La semana 04 ya presenta inversa, interpretación geométrica del determinante, cofactores, propiedades, eliminación y criterio de invertibilidad. La semana 05 debe usar estos resultados para interpretar y decidir, sin volver a desarrollar toda la teoría.

De 2025A se conservan las equivalencias de invertibilidad, Cramer y la definición formal de espacio vectorial. Se propone adaptar lo siguiente:

- Sustituir el ejemplo central de Cramer de orden tres por uno de orden dos con significado geométrico y continuidad con la semana 02.
- Presentar primero desplazamientos, rectas y planos; después, organizar sus propiedades mediante los axiomas.
- Reducir las ocho demostraciones por coordenadas a una verificación representativa y explicar cómo las restantes se heredan de los números reales.
- Posponer operaciones no usuales, espacios de funciones y demostraciones de unicidad del neutro e inverso.
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

## Clase 2 — Espacios vectoriales desde la geometría

### Resultados de aprendizaje

Interpretar suma y producto escalar como desplazamientos; reconocer rectas y planos estables bajo estas operaciones; relacionarlos con sistemas homogéneos; comprender la definición de espacio vectorial real y justificar ejemplos y contraejemplos.

### Secuencia de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
|---|---|---|
| 0–15 | Explorar suma y producto escalar en el plano con flechas. | Interpretar composición, cambio de magnitud, inversión y vector cero. |
| 15–35 | Recta por el origen y recta trasladada en \(\mathbb R^2\). | Pasar del dibujo a una verificación con parámetros generales. |
| 35–55 | Plano por el origen en \(\mathbb R^3\) y contraste con uno trasladado. | Conectar ecuación homogénea y descripción paramétrica. |
| 55–75 | Definición formal de espacio vectorial real y lectura de los axiomas. | Asociar propiedades algebraicas con los movimientos explorados. |
| 75–90 | Verificar una propiedad en \(\mathbb R^2\) y explicar las propiedades heredadas. | Distinguir argumentos generales de ejemplos numéricos. |
| 90–110 | Clasificar conjuntos en parejas y discutir contraejemplos. | Justificar la aceptación o identificar una propiedad que falla. |
| 110–120 | Aplicación a velocidades y salida individual. | Explicar por qué contener al cero no es suficiente. |

### Apertura: operar con desplazamientos

Dibujar \(u=(2,1)\), \(v=(1,3)\), \(u+v\), \(2u\), \(-u\) y \(0u\). Pedir que describan cada operación antes de escribir su cálculo por componentes. Usar la regla del paralelogramo para sumar y distinguir el punto final de una flecha del desplazamiento que representa.

Pregunta conductora: **¿qué conjuntos de movimientos permiten sumar, invertir y cambiar la escala sin salir de ellos?** Primero explorar libremente el plano; después imponer la restricción de moverse por una recta o un plano del espacio.

### Motivación en el plano: ¿qué movimientos permanecen en una dirección?

Sea

\[
L=\{t(2,1):t\in\mathbb R\}.
\]

Dibujar \(u\), \(2u\), \(-u\) y el vector cero. La suma compone desplazamientos; el producto por un escalar cambia magnitud y, si es negativo, sentido. Preguntar si sumar dos movimientos de \(L\), o invertir uno, permite salir de la recta.

Si \(p=su\) y \(q=tu\), entonces

\[
p+q=(s+t)u\in L,\qquad \lambda p=(\lambda s)u\in L.
\]

Contrastar con la recta trasladada \(M=\{(x,y):x-2y=1\}\). Contiene \((1,0)\), pero no \(0(1,0)=(0,0)\). Con las operaciones usuales, no puede ser un espacio vectorial.

**Figura propuesta para los apuntes:** dos paneles con la recta \(x=2y\) y su paralela \(x-2y=1\); señalar el origen, un vector de cada conjunto y su múltiplo cero.

### Motivación en el espacio: movimientos restringidos a un plano

Un dispositivo se mueve en el plano

\[
P=\{(x,y,z):x+y-z=0\}.
\]

Los movimientos \(a=(1,0,1)\) y \(b=(0,1,1)\) pertenecen a él; también \(a+b=(1,1,2)\), \(-a\) y el movimiento nulo. Al despejar \(z=x+y\):

\[
P=\{(s,t,s+t):s,t\in\mathbb R\}
=\{s(1,0,1)+t(0,1,1):s,t\in\mathbb R\}.
\]

Conectar esta descripción con las variables libres de la semana 03. Todavía no se necesita introducir base ni dimensión.

Para verificar la estabilidad con vectores generales, sumar sus ecuaciones: si \(p_1+p_2-p_3=0\) y \(q_1+q_2-q_3=0\), la suma también satisface la ecuación; al multiplicar por cualquier real, el lado derecho sigue siendo cero.

Contrastar con \(Q=\{(x,y,z):x+y-z=1\}\): no contiene el origen. Dos puntos de \(Q\) suman un vector cuyo lado izquierdo vale 2. Aclarar que un plano trasladado puede representar posiciones físicas válidas aunque no sea espacio vectorial con las operaciones usuales.

**Figura propuesta:** un paralelogramo contenido en \(P\), con flechas \(a\), \(b\) y \(a+b\), y el origen señalado. Mostrar una porción finita del plano, indicando que se prolonga indefinidamente.

### Formalización después de los ejemplos

**Definición.** Un espacio vectorial real es un conjunto no vacío \(V\) con una suma \(V\times V\to V\) y un producto escalar \(\mathbb R\times V\to V\) que satisfacen, para cualesquiera \(u,v,w\in V\) y \(\alpha,\beta\in\mathbb R\):

1. \((u+v)+w=u+(v+w)\).
2. \(u+v=v+u\).
3. Existe \(0_V\in V\) tal que \(u+0_V=u\).
4. Para cada \(u\), existe \(-u\in V\) tal que \(u+(-u)=0_V\).
5. \(\alpha(u+v)=\alpha u+\alpha v\).
6. \((\alpha+\beta)u=\alpha u+\beta u\).
7. \(\alpha(\beta u)=(\alpha\beta)u\).
8. \(1u=u\).

Las operaciones deben producir elementos de \(V\): esta es la clausura. Relacionar el neutro con «no moverse», el inverso con «regresar» y la distributividad con escalar un recorrido compuesto.

En \(\mathbb R^n\), las operaciones son por componentes. Verificar como modelo \(\alpha(u+v)=\alpha u+\alpha v\) en \(\mathbb R^2\); las demás identidades se justifican mediante las propiedades de los reales.

**Criterio para los ejemplos de esta clase.** Si \(V\subseteq\mathbb R^n\) usa las operaciones usuales, basta comprobar que contiene al cero, que es cerrado bajo suma y que es cerrado bajo producto por cualquier escalar real. Las otras identidades se heredan de \(\mathbb R^n\), y el inverso pertenece a \(V\) por tomar el escalar \(-1\). Un conjunto así se llama **subespacio** de \(\mathbb R^n\); su estudio sistemático queda para la siguiente semana.

Este criterio no sustituye la verificación de los axiomas cuando se definen operaciones nuevas.

### Actividad de clasificación y aplicación

Para aceptar un conjunto, justificar con elementos generales; para rechazarlo, dar un contraejemplo concreto. Todos usan las operaciones usuales y escalares reales.

| Conjunto | Clave para el docente |
|---|---|
| \(\{(x,y):y=2x\}\) | Sí: \((s,2s)+(t,2t)=(s+t,2(s+t))\); el producto escalar también conserva la forma y contiene al cero. |
| \(\{(x,y):x\ge0,\ y\ge0\}\) | No: contiene \((1,0)\), pero no su múltiplo por \(-1\). |
| \(\{(x,y):xy=0\}\), unión de los ejes | No: contiene al cero y es cerrado bajo escalares, pero \((1,0)+(0,1)=(1,1)\) queda fuera. |
| \(\{(x,y,z):z=0\}\) | Sí: el cero, las sumas y todos los múltiplos siguen teniendo tercera coordenada cero. |
| \(\{(x,y,z):z=1\}\) | No: no contiene al cero. |

**Aplicación breve:** una plataforma solo admite velocidades \(v=(v_x,v_y,v_z)\) que satisfacen \(v_x+v_y-v_z=0\). ¿Combinar dos velocidades admisibles mantiene la restricción? ¿Y duplicar o invertir una? Justificar algebraicamente y explicar el resultado en el plano \(P\).

**Salida individual:** «Todo subconjunto de \(\mathbb R^2\) que contiene al origen es un espacio vectorial». Refutar usando la unión de los ejes o el primer cuadrante.

## Trabajo autónomo y alcance de los apuntes

Para después de la clase 1, dejar una aplicación de orden dos por Cramer y una pregunta sobre sus hipótesis; después de la clase 2, dos clasificaciones geométricas con justificación. Evitar listas largas de determinantes.

Los futuros apuntes pueden organizarse en `Semana05_clase01.tex` y `Semana05_clase02.tex`, con la plantilla actual, ejemplos resueltos breves, preguntas para completar y figuras en TikZ. Mantener esta propuesta y sus claves docentes separadas del material estudiantil. Como apertura a la abstracción, mencionar al cierre que matrices y polinomios también pueden ser vectores; desarrollar esos ejemplos en la siguiente semana.

Si aparecen dificultades aritméticas en la clase 1, proporcionar los determinantes del ejercicio de orden tres para completar y comprobar la solución; conservar el énfasis en el planteamiento y la interpretación. La clase 2 se dedica íntegramente a espacios vectoriales, sin trasladar a ella ejercicios pendientes de Cramer.

