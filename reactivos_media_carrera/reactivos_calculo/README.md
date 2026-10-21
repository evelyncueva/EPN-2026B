# Reactivos de Cálculo Diferencial — MATD124

## Archivos

- `propuesta_reactivos_MATD124.tex`: fuente de las diez preguntas, clave y justificaciones.
- `ReactivosCalculoMoodle.tex`: versión con los entornos `quiz` y `multi`, siguiendo el modelo `ReactivosAL2024B.tex`.
- `ReactivosCalculoMoodle.xml`: exportación directa para importar las diez preguntas a Moodle; incluye las justificaciones como retroalimentación general.
- `moodle.sty`: copia sin modificaciones del paquete instalado (versión 1.0); se conserva su licencia y autoría.
- `aleph-comandos.sty`: copia del paquete de Álgebra Lineal. Se carga en el mismo orden que en el modelo de 2024B.
- `generar_moodle.cjs`: regenera el `.tex` de Moodle y el XML desde la propuesta. No requiere dependencias de npm.

## Compilar el PDF de revisión

Se utilizan los mismos paquetes, opciones y orden de carga que en `ReactivosAL2024B.tex`: `inputenc`, `fontenc`, `babel`, `aleph-comandos`, `moodle`, `amssymb`, `mathpazo` y `geometry`.

El paquete estándar `moodle.sty` está incluido en esta carpeta. Si MiKTeX solicita alguna dependencia, instálela mediante MiKTeX Console. `aleph-moodle.sty` y `moodleEPN.sty` son extensiones y no sustituyen a `moodle`. Fuente oficial: [CTAN — moodle](https://ctan.org/pkg/moodle).

Desde `reactivos_calculo`, ejecute:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error ReactivosCalculoMoodle.tex
```

El paquete `moodle` produce un PDF para revisión y un archivo `ReactivosCalculoMoodle-moodle.xml`. El PDF de revisión muestra las respuestas correctas: no es la versión estudiantil del examen. Para esta última, utilice la propuesta con `\solucionesfalse`.

Si una compilación anterior permanece ejecutándose, deténgala en el editor antes de volver a compilar. Se retiró la carga manual de `supp-pdf.mkii` y se igualaron los paquetes al modelo de Álgebra que compila en Overleaf. La causa del bloqueo no está confirmada mediante una compilación controlada. Consulte `comparacion_formato.md` para conocer las diferencias y cómo aislarlas.

La compilación no pudo verificarse en el entorno del agente: MiKTeX no pudo inicializar su configuración en este entorno. La instalación del usuario sí ha generado el PDF de la propuesta original.

### Localizar un bloqueo sin mensaje de error

El documento actualizado escribe marcas `MATD124:` en el registro: carga de paquetes, inicio del documento, título y comienzo/final de cada pregunta. Si se bloquea, abra el registro completo (en Overleaf: **Logs and output files → Raw logs**) y busque la última marca `MATD124:`. Conserve también las líneas inmediatamente posteriores. Las marcas no aparecen en el PDF ni en las preguntas exportadas.

Como prueba adicional, seleccione `diagnostico_Moodle_PDF.tex` como documento principal. Carga las mismas preguntas y el paquete `moodle` en modo `draft`, que compone el PDF sin exportar XML. Si esta prueba finaliza y el documento normal no, se acota el problema a la ruta de exportación. Esta prueba no sustituye al archivo que debe entregarse para Moodle.

## Importar las preguntas a Moodle

Para revisar la traducción sin compilar LaTeX, abra `revision_Moodle.html` en el navegador. Esta vista extrae el contenido del XML real y muestra las respuestas correctas y las justificaciones. Necesita conexión a Internet para cargar MathJax y renderizar las fórmulas. Puede imprimirla o guardarla como PDF desde el navegador. Para actualizarla después de regenerar el XML, ejecute `node revisar_xml.cjs`.

En **Banco de preguntas → Importar**, seleccione **Formato Moodle XML** y cargue `ReactivosCalculoMoodle.xml`. Este archivo ya está generado y no requiere compilar LaTeX. También puede usar el XML producido por el paquete al compilar; importe uno de los dos para evitar duplicados.

Cada pregunta tiene cuatro opciones, selección única y una respuesta con calificación del 100 %. Se conserva el orden de las alternativas. Las fórmulas usan delimitadores LaTeX compatibles con MathJax; compruebe su visualización en la vista previa de Moodle.

## Actualizar los reactivos

Edite la propuesta y ejecute:

```powershell
node generar_moodle.cjs
```

Si cambia la respuesta correcta, actualice también la justificación y la entrada correspondiente del arreglo `keys` del generador. Este comprueba que la clave coincida con las justificaciones. Los cambios directos en los archivos generados se reemplazan al regenerarlos.
