# General

- [ ] Texto descolocado en la pantalla de inicio.
- [x] Al buscar el fichero sería mejor que se empezase en la última carpeta desde la cual se ha abierto el último fichero o, por defecto, en el home del usuario.
- [x] Botón para acceder a las opciones desde el inicio.
- [x] Cerrar el diálogo modal de "Xerando gráfica" automáticamente una vez se genere la gráfica.
- [x] El cuadro de texto para el título de la gráfica no tiene la apariencia de cuadro de texto modificable.
- [x] El cuadro de texto para el título de la gráfica debería aparecer arriba a la izquierda, separado visualmente del resto de opciones.
- [x] En el menú superior, solamente la opción de "nova gráfica" reacciona al hover y tiene un tamaño diferente al resto de opciones.
- [x] Cuando se genera una gráfica, ¿se calculan los valores Z para todas las columnas, o solamente para la que se va a representar? En la consola aparece un mensaje que da a entender lo último. ----> Estás no correcto, só na especificada cambiar o print
- [ ] Deberíamos corregir la fórmula de detección de outliers. Sugiero utilizar rangos intercuartílicos como en los boxplot (<https://en.wikipedia.org/wiki/Box_plot#Elements>).
- [x] Gardar imaxe sempre na mesma ruta


# Heatmap

- [x] Seleccionar el tipo de dato no cambia la gráfica a generar. Al seleccionar el tipo de dato del eje Z, se deberían convertir todos los datos al tipo seleccionado. Por ejemplo, si una columna se selecciona como booleana, se deberían convertir a valures 'true'/'false', pero si se selecciona como strings se tienen que convertir a los string "1" / "0" o lo que corresponda. ---> Bool ex: InPrefNode
- [ ] Refacer HeatMap de ints
- [x] Activar la eliminación de outliers no cambia la gráfica a generar.
- [x] Primeiro valor máximo e valor mínimo e se queres cambialo que o cambie o usuario


# Scatter

- [x] Activar la opción de unir puntos de la gráfica bloque la selección del esquema de colores. ¿Es un bug o hay alguna razón por la que tenga que ser así? image.png Fallo ao extraer as cores, non permite esa selección
- [x] ¿Tiene sentido poder definir el tipo de dato del eje Z? A discutir en la próxima reunión.  ----> Cambiar nome por cor, xa que é un pouco confuso
- [x] Al unir puntos de la gráfica, los puntos se unen de manera arbitraria en lugar de ordenarse según el eje X o timestamp.
- [x] Activar la eliminación de outliers no cambia la gráfica a generar.
- [x] Cambiar o z por cor en scatter
- [x] Outliers igual que no heatmap
- [x] Xuntar a opcion de Z (ahora con outro nome) e a de tipo de cor

# Temporal
- [x] Na x fijo temporal
- [ ] Na y glfops por ex, comprobando que se vexa ben
- [ ] Permitir seleccion entre enteiros e punto flotante


# Roofline

- [ ] No se genera ninguna gráfica.


# Opciones

- [x] Los cambios no funcionan hasta matar por completo el proceso y volver a abrirlo. El diálogo modal no cumple su objetivo.
- [x] No se resaltan las opciones seleccionadas y activas respecto al idioma o esquema de color.
- [x] Los esquemas de colores están rotos, se mezclan distintos esquemas.
- [x] La selección de idioma no funciona correctamente, se mezclan distintos idiomas.
- [x] Sobra la "X" para cerrar la ventana de opciones.


# Notas reunion

- [x] Crear unha de temporal
- [x] Ops fagao suma e para a latencia a media

# Para un futuro
- [ ] Coller o do diagrama de vigotes, que dan cota maxima e minima, e cun rango intercuartilico, e eliminalos



# Memoria:
- [ ] La primera frase del resumen hay que reescribirla mejor.

- [ ] Hablar de información del rendimiento, no solo de información. Y comentar que esa información se obtiene en su mayor parte de los contadores hardware.

- [ ] En el segundo párrafo cambiar programa por proxecto.

- [ ] La última frase del segundo párrafo hay que reescribrila bien.

- [ ] En el capítulo 1,

- [ ] En el capítulo 2, no empezar hablando de etapa sino de capítulo.

- [x] Antes de enumerar los 5 puntos de la página 4, decir que aunque Grafana cumple una buena parte de los requisitos establecidos, tiene una serie de limitaciónes ....

- [ ] Hacer algo más grandes las figuras del capítulo 2 para que los fonts que aparezcan en allas sean lo más legibles posible.

- [ ] En la especificación de requisitos quitaría las listas enumeradas de rquisitos que luego se repiten en las tablas.

- [ ] Aunque no lo pide expresamente la plantilla del proyecto, yo añadiría al final del capítulo 3 un apartado sobre planificación temporal, en el que diría que ha habido un reajuste respecto a la planificacion inicial dado que se ha descratado Grafana ya que .... Muy breve. Poner una tabla con el reparto temporal o un Gant ¿Quizás no haga falta?

- [ ] Quitaría el apartado 4.2.

- [ ] En el apartado 4.4 yo pondría al final, en particular el desarrollo del proyecto y las pruebas se han realizado en un computador .......

- [x] En el punto 5.1 yo no hablaría de profesorado sino del grupo de investigación.

- [ ] La figura 5.1 no se ve nada bien. Propongo hacerla más grande.

- [x] Títulos de las secciones del capítulo 5 que propongo: "Recopilación de recomendacións", "Máquetas interactivas", "Aplicación de melloras", "Repetición iterativa". Faltarían las dos últimas: "Codificación" y "Probas".

- [x] Las figuras del capítulo 6 más grande para que se lea mejor, salvo las que ya se leen sin problema, por ejemplo la 6.9.

- [x] En las conclusiones decir que se han analizado con detalle un buen número de posibles herramientas y se ha optado por .... ya que  ....
  
- [ ] Insertar figuras na memoria
- [ ] Para separar parágrafos non hai que usar o comando \newpara, que causa erros no formateo. Hai que deixar unha liña en branco entre os parágrafos en cuestión.
- [ ] Importante, fai a bibliografía con bibtex. Os bibitems levan a erros no formato da bibliografía, e o tribunal sempre resta moito nesas cuestións formais. https://es.overleaf.com/learn/latex/Bibliography_management_with_bibtex 
- [x] Os comando \hline non emprega {} ao final. Conleva erros no formateo dos cadros, polo que tes que buscar os {} e eliminalos.
- [ ] Segundo a documentación do paquete Babel, en galego débese utilizar cadro, xa que táboa é un falso amigo (http://ctan.math.utah.edu/ctan/tex-archive/macros/latex/contrib/babel-contrib/galician/galician.pdf). 
- [x] As figuras non deberían colocarse con [H]. É mellor utilizar [htbp]. Pode ser que LaTeX non as coloque onde ti queiras, pero esa vai ser a forma correcta. Deste xeito tamén tes que evitar referirte ás figuras con "a seguinte figura" ou "esta figura", hai que referirse a elas como "a Figura~\cite{label}".
- [ ] Para engadir unha figura é mellor que evites utilizar \centerline e a opción width en centímetros. Podes utilizar este código de exemplo:
