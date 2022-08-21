# TFG - Aplicación para a visualización de 


Neste arquivo resúmese a finalidade, o contido e un manual do funcionamento da aplicación, para que esta poida ser executada e testeada baixo a licenza ca que se publica este proxecto.


## Resumo do Traballo Fin de Grao

Neste traballo fin de grao realizouse unha análise de diferentes solucións ca finalidade de atopar a mellor tecnoloxía existente entre as múltiples alternativas para crear unha aplicación que sirva para ler e procesar trazas de arquivos que conteñen información sobre o rendemento extraído da execución de diferentes programas en servidores NUMA. Esta información extráese na súa meirande parte dos contadores hardware do servidor e mostrarase como diferentes saídas dependendo da información lida do arquivo e das necesidades do usuario, permitíndolle a este seleccionar que tipo de gráfica e que datos desexa visualizar.

Na primeira fase do proxecto realizouse unha investigación de diferentes alternativas para poder atopar a tecnoloxía que mellor se podía adaptar aos nosos requisitos para realizar o proxecto, as tecnolox´ıas exploradas para realizar o proxecto foron varias; primeiro estudouse unha integración de Grafana con Docker para xerar as gráficas, que non funcionou por diferentes razóns que se especifican na memoria. Posteriormente dese˜nouse e realizouse unha serie de probas das mellores librarías de Python para crear gráficas, descartando aquelas que presentaban problemas de rendemento ou que non se adaptaban aos nosos requisitos, ata quedarnos con aquela que mellor se adaptou.

Unha vez escollida a tecnoloxía a empregar realizouse unha aplicación de escritorio, escrita en Python, permitindo así que sexa multiplataforma, con posibilidade de editar idioma, cores e resolucións. Esta interface gráfica permite ao usuario incluir o arquivo a procesar e escoller o tipo de gráfica a xerar, permitindo ao usuario xerar diferentes gráficas á vez a partir do mesmo arquivo de datos.

## Contido deste repositorio

Este repositorio contén o código fonte da aplicación final realizada para satisfacer as necesidades expresadas polo equipo de traballo no que se integrou o proxecto respecto á visualización

## Funcionamento

### Requisitos para a execución

Para poder executar a aplicación é preciso ter instalado no equipo unha versión de ``Python3`` igual ou superior 

### Execución do programa

Para a execución do programa é preciso realizar a instalación 