# TFG - Aplicación para a visualización de datos de servidores NUMA


Neste arquivo resúmese a finalidade, o contido e un manual do funcionamento da aplicación, para que esta poida ser executada e testeada baixo a licenza ca que se publica este proxecto.


## Resumo do Traballo Fin de Grao

Neste traballo fin de grao realizouse unha análise de diferentes solucións ca finalidade de atopar a mellor tecnoloxía existente entre as múltiples alternativas para crear unha aplicación que sirva para ler e procesar trazas de arquivos que conteñen información sobre o rendemento extraído da execución de diferentes programas en servidores NUMA. Esta información extráese na súa meirande parte dos contadores hardware do servidor e mostrarase como diferentes saídas dependendo da información lida do arquivo e das necesidades do usuario, permitíndolle a este seleccionar que tipo de gráfica e que datos desexa visualizar.

Na primeira fase do proxecto realizouse unha investigación de diferentes alternativas para poder atopar a tecnoloxía que mellor se podía adaptar aos nosos requisitos para realizar o proxecto, as tecnoloxías exploradas para realizar o proxecto foron varias; primeiro estudouse unha integración de Grafana con Docker para xerar as gráficas, que non funcionou por diferentes razóns que se especifican na memoria. Posteriormente dese˜nouse e realizouse unha serie de probas das mellores librarías de Python para crear gráficas, descartando aquelas que presentaban problemas de rendemento ou que non se adaptaban aos nosos requisitos, ata quedarnos con aquela que mellor se adaptou.

Unha vez escollida a tecnoloxía a empregar realizouse unha aplicación de escritorio, escrita en Python, permitindo así que sexa multiplataforma, con posibilidade de editar idioma, cores e resolucións. Esta interface gráfica permite ao usuario incluir o arquivo a procesar e escoller o tipo de gráfica a xerar, permitindo ao usuario xerar diferentes gráficas á vez a partir do mesmo arquivo de datos.

## Contido deste repositorio

Este repositorio contén o código fonte da aplicación final realizada para satisfacer as necesidades expresadas polo equipo de traballo no que se integrou o proxecto respecto á visualización de datos extraídos dos contadores hardware dos servidores HPC, concretamente de aqueles que contan con arquitectura NUMA.

## Funcionamento

Nesta sección explícase o funcionamento e os requisitos precisos para a execución do programa.

### Requisitos para a execución

Para poder executar a aplicación é preciso ter instalado no equipo unha versión de ``Python3`` igual ou superior á ``3.10.6``, así como un sistema operativo que conte con interface gráfica para ser quen de interpretar o programa.

### Execución do programa

Para a execución do programa é preciso realizar a instalación das dependencias que se atopan indicadas dentro do arquivo de texto ```requeriments.txt```, estas poden ser instaladas dun xeito moi doado executando o comando ```pip3 install requeriments.txt```, xa que este comando encárgase de realizar a instalación de cada unha das que se atopan indicadas neste arquivo de texto.

Unha vez instalados as librerías necesarias indicadas no arquivo de texto temos que abrir un terminal dentro da carpeta indicada para poder realizar a execución do programa. Para realizar esta acción temos que executar o seguinte comando: ```python3 gui.py```.

### Arquivos de entrada

O programa acepta como arquivos de entrada aqueles que contan con formato ```.csv```, xa que este está deseñado para ler os datos que conteñen este arquivos de tal xeito que cada columna representa un tipo de dato que ven determinado polo nome da columna. Por defecto o programa espera as seguintes columnas, ainda que pode traballar con diversas columnas:

- <b>Timestamp</b>: Esta columna contén información sobre o tempo no que se tomou a mostra.
- <b>TID</b>: Esta columna mostra cal é o TID do fío do que se extrae a información.
- <b>PID</b>: Esta columna mostra cal é o PID do fío do que se extrae a información.
- <b>CMDLINE</b>: Esta columna mostra cal é o comando que está executando o proceso.
- <b>State</b>: Esta columna mostra cal é o estado no que se atopa actuamente o fío, que pode ser R (Running) ou S (Sleeping).
- <b>CPU</b>: Esta columna mostra cal é a CPU na que se está a executar o fío.
- <b>Node</b>: Esta columna mostra cal é o nodo do servidor no que se está a executar o fío.
- <b>PrefNode</b>: Esta columna mostra cal é o nodo no que se aloxan a maioría dos datos lidos en memoria. Considérase o “nodo preferido” do fío en cuestión.
- <b>InPrefNode</b>: Esta columna indícanos se o nodo se atopa nese intre dentro do nodo preferido.
- <b>Perf</b>: Esta columna mostra o rendemendo do fío según o cálculo do algoritmo de migración de fíos do GAC (Grupo de Arquitectura de Computadores da USC).
- <b>CPU %</b>: Esta columna mostra o uso de CPU do programa nese intre temporal.
- <b>RelPerf</b>: Esta columna mostra o rendemento relativo do fío según o cálculo do algoritmo de migración de fíos do GAC, escalado según o rendemento de todos os fíos do mesmo proceso.
- <b>Ops</b>: Esta columna mostra as operacións realizadas por segundo.
- <b>OpIntensity</b>: Esta columna, Intensidade operacional, operacións realizadas por acceso de memoria.
- <b>AvLat</b>: Esta columna mostra a latencia media de acceso á memoria


## Gráficas implementadas

O programa conta cunha serie de gráficas que se poden xerar empregando a ferramenta, entre as que se atopan o Scatter e o Heatmap, sendo esta a base do programa.
