# Propuesta de material — Semana 06, semestre 2026-B

Una clase de 120 minutos dedicada a subespacios vectoriales. Los apuntes estudiantiles están en `Semana06_clase01.tex`. Este archivo contiene la secuencia y las claves para el docente. La compilación y la revisión visual del PDF quedan a cargo del docente, conforme a lo acordado.

## Referencias y adaptación de 2025A

La fuente principal es `Apuntes 2025-A/Primer bimestre/Semana 07 Clase 02.tex`: definición de subespacio, criterio de cerradura, recta y=2x, ejemplos que no son subespacios, e intersección de dos planos. Se conserva la plantilla de `Apuntes2026B/` y se enlaza con los espacios y operaciones de la semana 05.

La adaptación empieza con movimientos en una recta, antes de formalizar. Se explican por separado las dos cerraduras y se contrastan con una semirrecta y una unión de ejes. Los ejemplos numéricos motivan; la verificación con parámetros arbitrarios demuestra. El ejemplo desarrollado del plano, su figura y el ejercicio de intersección se reservan para la semana 07 en `Reserva_semana07_planos.md`. No se incorporan el bloque de propiedades abstractas de 2025A ni combinación lineal, cápsula, base o dimensión.

## Resultados de aprendizaje

- Interpretar la suma como composición de desplazamientos y el producto por escalar como cambio de magnitud y sentido.
- Reconocer que un subespacio usa las operaciones y los escalares del espacio ambiente.
- Verificar cero y ambas cerraduras con vectores arbitrarios, o rechazar mediante un contraejemplo.
- Aplicar el mismo criterio a subconjuntos de matrices y polinomios, identificando qué condición conservan sus operaciones.

## Secuencia de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
|---|---|---|
| 0–15 | Movimientos sobre L={t(1,2):t real}; figura y preguntas sobre invertir el sentido. | Distinguir recta completa de semirrecta. |
| 15–40 | Definición, criterio y verificación general de la recta por componentes. | Precisar qué significa que una operación permanezca en W. |
| 40–65 | Recta trasladada y unión de ejes. | Identificar fallos de cerradura; contener al cero no basta. |
| 65–90 | Ejemplos resueltos de matrices diagonales y polinomios que se anulan en 1. | Transferir el criterio a otros tipos de vectores. |
| 90–110 | Clasificación del ejercicio 1, incluida la semirrecta, en parejas y puesta en común. | Dar argumentos generales para aceptar y contraejemplos para rechazar. |
| 110–120 | Salida individual y cierre. | Detectar que la cerradura bajo escalares no garantiza la suma. |

Dejar el ejercicio de velocidades como práctica adicional, junto con el ejercicio de matrices y polinomios. La intersección se estudiará la semana siguiente. Priorizar el significado y la verificación de las cerraduras.

## Lectura geométrica que conviene enfatizar

En una recta por el origen, sumar dos desplazamientos conserva la dirección. Permitir todo escalar real obliga a incluir ambos sentidos, todas las magnitudes y el cero. Después de introducir el criterio, demostrar por componentes que ambas operaciones conservan la relación y=2x.

Una recta trasladada puede describir posiciones físicas, pero el conjunto no es un subespacio con las operaciones usuales. No confundir posiciones con desplazamientos. La semirrecta aísla el fallo del producto por escalares negativos; los dos ejes aíslan el fallo de la suma. Dibujar ejemplos ayuda a comprender, pero no reemplaza una prueba para todos los vectores.

El criterio utiliza explícitamente 0_V en W. Es equivalente a pedir W no vacío y las dos cerraduras, como en 2025A: el escalar cero garantiza que el cero ambiente está en W. Así se evita omitir la no vacuidad y se explica por qué no hay que verificar ocho axiomas nuevos.

## Transición a matrices y polinomios

La sección de sistemas homogéneos se sustituye por dos ejemplos resueltos antes de los ejercicios. Las matrices diagonales conservan los ceros fuera de la diagonal al sumar y escalar. En W={p en P₂:p(1)=0}, escribir p(t)=a₀+a₁t+a₂t² y q(t)=b₀+b₁t+b₂t², con a₀+a₁+a₂=b₀+b₁+b₂=0. Desarrollar la suma y el producto por escalar y evaluar en 1 para verificar las cerraduras. Las gráficas siguen pasando por (1,0). Contrastar brevemente con p(1)=1, que excluye al polinomio cero y no conserva la suma.

Los ejemplos preparan el trabajo autónomo sin resolverlo de forma idéntica: allí se pide analizar matrices simétricas y polinomios con condición en 0. Enfatizar que la condición cambia, pero el procedimiento de cero, suma y producto por escalar es el mismo.

## Claves de ejercicios

1. **Clasificación:** W₁ sí: (s,−s)+(t,−t)=(s+t,−(s+t)); los múltiplos conservan esa forma. W₂ no: (1,0) pertenece, pero su múltiplo por −1 no. W₃ sí: sumar o escalar conserva la tercera coordenada cero. W₄ no: no contiene al cero; también falla la suma de (0,0,1) consigo mismo. W₅ no: contiene al cero y es cerrado bajo suma porque s+t≥0 si s,t≥0, pero (1,2) pertenece y su múltiplo por −1 no. La semirrecta se deja como ejercicio, sin desarrollar su solución en los apuntes.
2. **Velocidades:** W es el plano z=x+y. Se obtiene 2a−b=(2,−1,1), que satisface 2−1−1=0. Se combinan un producto por escalar y una suma con el inverso de b; el cálculo solo ilustra, no prueba las cerraduras generales. Con la condición adicional z≥0, a sigue permitido, pero −a=(−1,0,−1) queda fuera.
3. **Salida:** falta la cerradura bajo suma; usar la unión de los ejes y (1,0)+(0,1)=(1,1).
4. **Trabajo posterior:** U sí: la igualdad de las dos entradas se conserva al sumar y escalar. T sí: (p+q)(0)=0 y (αp)(0)=0. S no: excluye al polinomio cero; también sumar dos polinomios con valor 1 en cero produce valor 2.

## Revisión pendiente de compilación

No se cargan `nicematrix` ni paquetes nuevos respecto a la clase 2 de la semana 05. Las figuras están en TikZ y respetan el ancho compacto de la plantilla. Al compilar, revisar referencias, cortes de recuadros, etiquetas de las figuras y saltos de página; no se ha generado un PDF para esta clase.
