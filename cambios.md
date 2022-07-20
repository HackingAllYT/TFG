# General

- [ ] Texto descolocado en la pantalla de inicio.
- [x] Al buscar el fichero sería mejor que se empezase en la última carpeta desde la cual se ha abierto el último fichero o, por defecto, en el home del usuario.
- [x] Botón para acceder a las opciones desde el inicio.
- [x] Cerrar el diálogo modal de "Xerando gráfica" automáticamente una vez se genere la gráfica.
- [ ] El cuadro de texto para el título de la gráfica no tiene la apariencia de cuadro de texto modificable.
- [ ] El cuadro de texto para el título de la gráfica debería aparecer arriba a la izquierda, separado visualmente del resto de opciones.
- [x] En el menú superior, solamente la opción de "nova gráfica" reacciona al hover y tiene un tamaño diferente al resto de opciones.
- [x] Cuando se genera una gráfica, ¿se calculan los valores Z para todas las columnas, o solamente para la que se va a representar? En la consola aparece un mensaje que da a entender lo último. ----> Estás no correcto, só na especificada cambiar o print
- [ ] Deberíamos corregir la fórmula de detección de outliers. Sugiero utilizar rangos intercuartílicos como en los boxplot (<https://en.wikipedia.org/wiki/Box_plot#Elements>).


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
- [ ] Na x fijo temporal
- [ ] Na y glfops por ex, comprobando que se vexa ben
- [ ] Permitir seleccion entre enteiros e punto flotante


# Roofline

- [ ] No se genera ninguna gráfica.


# Opciones

- [x] Los cambios no funcionan hasta matar por completo el proceso y volver a abrirlo. El diálogo modal no cumple su objetivo.
- [ ] No se resaltan las opciones seleccionadas y activas respecto al idioma o esquema de color.
- [x] Los esquemas de colores están rotos, se mezclan distintos esquemas.
- [x] La selección de idioma no funciona correctamente, se mezclan distintos idiomas.
- [x] Sobra la "X" para cerrar la ventana de opciones.


# Notas reunion

- [ ] Crear unha de temporal

# Para un futuro
- [ ] Coller o do diagrama de vigotes, que dan cota maxima e minima, e cun rango intercuartilico, e eliminalos