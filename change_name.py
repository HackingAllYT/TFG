import glob
import os

listNames = glob.glob('*.png')

newNames = [
    'xerar.png',
    'editar_over.png',
    'cargar_arquivo.png',
    'cargar_arquivo_over.png',
    'home.png',
    'home_over.png',
    'vista_rapida.png',
    'vista_rapida_over.png',
    'nova_grafica.png',
    'nova_grafica_over.png',
    'detallar_datos.png',
    'xerar_over.png',
    'detallar_datos_over.png',
    'seleccionar_grafica.png',
    'seleccionar_grafica_over.png',
    'gardar_saida.png',
    'gardar_saida_over.png',
    'sair.png',
    'sair_over.png',
    'configuracion.png',
    'configuracion_over.png',
    'editar.png'
]

print(listNames)

for i in range(len(listNames)):
    os.rename(listNames[i], newNames[i])

print("Done!")
print(glob.glob('*.png'))
