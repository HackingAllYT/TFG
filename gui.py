#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, OptionMenu, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk, BOTH, Toplevel, Checkbutton, IntVar

import tkinter as tk
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno
import modalSelectFigure as msf


from migplot import parse_file, initial_chart

from checkBoxTreeview import CheckboxTreeview, loadPids

from modalConfiguration import configurationModal

from initialFrame import intitilizateInitialFrame, destroyInitialFrame

from threading import *
import configparser

from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

arquivos = []

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def reload():
    window.update()


def select_path():
    filetypes = (
        ('Comma-separated values', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        showinfo(
            title=TEXT[config['INITIAL']['IDIOMA']]['Arquivo seleccionado:'],
            message=filename
        )


def openConfigurationModal():
    global conModal
    conModal = configurationModal(window)
    # window.wait_window(conModal.top)


def openSelectFigureModal():
    global figModal
    sugges = ((0, 'Item 0'), (1, 'Item 1'))
    figModal = msf.SuggestionPopup(window, suggestions=sugges)
    result = figModal.show()
    if result == 'heatmap':
        mostrarEdicion()


def confirmExit():
    answer = askyesno(title=TEXT[config['INITIAL']['IDIOMA']]['Saír?'],
                      message=TEXT[config['INITIAL']['IDIOMA']]['Está seguro que quere pechar?'])
    if answer:
        window.destroy()


def display_selected(choice):
    choice = variable.get()
    print(choice)


def edit_button():
    global arquivos
    # d = MyDialog(window, arquivos, "Probando Dialogo", "Dame valor")
    # window.wait_window(d.top)


def mostrar_imaxe():
    initialFrame.destroy()
    photoFrame.pack(fill=BOTH, expand=1)


def mostrarEdicion():
    photoFrame.destroy()
    # button_7.destroy()
    button_1_PhotoFrame.destroy()
    button_2_PhotoFrame.destroy()
    button_3_PhotoFrame.destroy()
    # Destruimos o modal
    # destroyPop()
    # Da un fallo se xa existe o frame e se volve a pintar
    t.insertElements(info)
    # Insertamos os tipos de datos
    xData_cb['values'] = list(infoData[0][1].columns)
    xData_cb.current(0)
    yData_cb['values'] = list(infoData[0][1].columns)
    yData_cb.current(1)
    zData_cb['values'] = list(infoData[0][1].columns)
    zData_cb.current(5)
    z_tipoDatos_cb['values'] = list(infoData[0][1].columns)
    z_tipoDatos_cb.current(0)

    editFrame.pack(fill=BOTH, expand=1)


def mostrarHomedendeEdicion():
    ""


def mostrarHomedendeImaxe():
    initialFrame.pack(fill=BOTH, expand=1)


'''
class MyDialog:
    def __init__(self, parent, valor, title, labeltext=''):
        self.valor = valor

        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(title) > 0:
            self.top.title(title)
        if len(labeltext) == 0:
            labeltext = 'Valor'
        tk.Label(self.top, text=labeltext).pack()
        self.top.bind("<Return>", self.ok)
        # TODO: non existe o get para os arrays, mirar como gardar os arquivos
        self.e = Entry(self.top, text=valor.get())
        self.e.bind("<Return>", self.ok)
        self.e.bind("<Escape>", self.cancel)
        self.e.pack(padx=15)
        self.e.focus_set()
        b = Button(self.top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self, event=None):
        print("Has escrito ...", self.e.get())
        self.valor.set(self.e.get())
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()
'''

window = Tk()

window.title('Aplicación para a visualización de datos de servidores NUMA')
# window.iconbitmap('assets/citius.ico')
#window.wm_attributes('-toolwindow', 'True')

window.geometry("1024x720")
window.configure(bg="#FFFFFF")

'''
**************************************************************************
******************************* EDIT FRAME *******************************
'''

editFrame = Frame(window, width=1024, height=720)
#editFrame.pack(fill=BOTH, expand=1)

t = CheckboxTreeview(window, show="tree")
t.place(
    x=42.0,
    y=240.0,
    width=660.0,
    height=440.0
)

canvas = Canvas(
    editFrame,
    bg="#FFFFFF",
    height=720,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    55.0,
    fill=TEXT[config['INITIAL']['COLOR']],
    outline="")

canvas.create_rectangle(
    36.0,
    121.0,
    286.0,
    196.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    57.0,
    125.0,
    anchor="nw",
    text="X:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    384.0,
    121.0,
    634.0,
    196.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    408.0,
    124.0,
    anchor="nw",
    text="Y:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    737.0,
    121.0,
    987.0,
    196.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    758.0,
    125.0,
    anchor="nw",
    text="Z:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    737.0,
    216.0,
    987.0,
    291.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    758.0,
    220.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Tipo dato Z:"],
    fill="#000000",
    font=("Inter", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("sair_button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=confirmExit,
    relief="flat"
)
button_1.place(
    x=637.0,
    y=2.0,
    width=180.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("configuration_button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=openConfigurationModal,
    relief="flat"
)
button_2.place(
    x=70.0,
    y=2.0,
    width=180.0,
    height=53.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("edit_buttom.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=448.0,
    y=2.0,
    width=180.0,
    height=53.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("loadFile_button.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=259.0,
    y=2.0,
    width=180.0,
    height=53.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("xerar_button.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=787.0,
    y=608.0,
    width=180.0,
    height=55.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("home.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=2.0,
    y=2.0,
    width=51.0,
    height=51.0
)

canvas.create_rectangle(
    36.0,
    234.0,
    706.0,
    684.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    737.0,
    328.0,
    anchor="nw",
    text="Outliers:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    853.0,
    337.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=817.0,
    y=320.0,
    width=72.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    945.0,
    336.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.place(
    x=909.0,
    y=319.0,
    width=72.0,
    height=33.0
)

canvas.create_rectangle(
    893.0,
    336.0,
    904.0,
    338.0,
    fill="#000000",
    outline="")

canvas.create_text(
    763.0,
    397.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    831.0,
    356.0,
    anchor="nw",
    text="μ - 2σ",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    921.0,
    356.0,
    anchor="nw",
    text="μ + 2σ",
    fill="#000000",
    font=("Inter", 15 * -1)
)

deleteOutliers = IntVar()


def deleteOutliers_changed():
    print('het')


checkButton = Checkbutton(
    editFrame,
    text='',
    command=deleteOutliers_changed,
    variable=deleteOutliers,
    onvalue=1,
    offvalue=0,
    background='#FFFFFF'
)

checkButton.place(
    x=909.0,
    y=390.0,
    width=72.0,
    height=33.0
)


'''
***************************************************************************
'''
'''aux = StringVar()
aux_cb = ttk.Combobox(window, textvariable=aux, width=28)

# get first 3 letters of every month name
aux_cb['values'] = [countries[m][0:3] for m in range(4)]

# prevent typing a value
aux_cb['state'] = 'readonly'

# place the widget
#columnas_cb.pack(fill=None, side=LEFT, padx=0, pady=110)
aux_cb.grid(column=0, row=0, padx=0, pady=40)
aux_cb.current()
aux_cb.grid_forget()'''


'''
***************************************************************************
'''

xData = StringVar()
xData_cb = ttk.Combobox(
    editFrame,
    textvariable=xData,
    width=28
)

# prevent typing a value
xData_cb['state'] = 'readonly'

# place the widget
#columnas_cb.pack(fill=None, side=LEFT, padx=0, pady=110)
xData_cb.place(
    x=50.0,
    y=165.0,
    width=170.0,
    height=20.0
)

yData = StringVar()
yData_cb = ttk.Combobox(
    editFrame,
    textvariable=yData,
    width=28
)


# prevent typing a value
yData_cb['state'] = 'readonly'

# place the widget
yData_cb.place(
    x=400.0,
    y=165.0,
    width=170.0,
    height=20.0
)

zData = StringVar()
zData_cb = ttk.Combobox(
    editFrame,
    textvariable=zData,
    width=28
)

# get first 3 letters of every month name
# zData_cb['values'] = [countries[m][0:4] for m in range(4)]

# prevent typing a value
zData_cb['state'] = 'readonly'

# place the widget
zData_cb.place(
    x=750.0,
    y=165.0,
    width=170.0,
    height=20.0
)
# zData_cb.current()

z_tipoDatos = StringVar()
z_tipoDatos_cb = ttk.Combobox(
    editFrame,
    textvariable=z_tipoDatos,
    width=28
)

# get first 3 letters of every month name
# z_tipoDatos_cb['values'] = [countries[m][0:3] for m in range(4)]

# prevent typing a value
z_tipoDatos_cb['state'] = 'readonly'

# place the widget
z_tipoDatos_cb.place(
    x=750.0,
    y=265.0,
    width=170.0,
    height=20.0
)
z_tipoDatos_cb.current()


'''
**************************************************************************

'''

'''
def destroyPop():
    pop.destroy()
    pop.update()


def selectionGrafica():
    global pop
    pop = Toplevel(window)
    pop.title("Selección gráfica")
    pop.geometry("700x900")
    pop.grab_set()
    # pop.overrideredirect(True) # para que non teña os bordes de windows
    modalFrame = Frame(pop, width=700, height=900)

    canvas = Canvas(
        modalFrame,
        bg="#FFFFFF",
        height=900,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        80.0,
        fill=TEXT[config['INITIAL']['COLOR']],
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("cross.png"))
    button_1 = Button(
        pop,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=destroyPop,
        relief="flat"
    )
    button_1.place(
        x=630.0,
        y=9.0,
        width=58.0,
        height=58.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_heatmap.png"))
    button_2 = Button(
        pop,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=mostrarEdicion,
        relief="flat"
    )
    button_2.place(
        x=20.0,
        y=123.0,
        width=312.0,
        height=248.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_scatter.png"))
    button_3 = Button(
        pop,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=368.0,
        y=123.0,
        width=312.0,
        height=248.0
    )

    canvas.create_text(
        220.0,
        28.0,
        anchor="nw",
        text=TEXT[config['INITIAL']['IDIOMA']]["Seleccione tipo de gráfica:"],
        fill="#000000",
        font=("Inter Bold", 20 * -1)
    )

    modalFrame.pack(fill=BOTH, expand=1)
    window.wait_window()  # pop.top
'''

'''
**************************************************************************
****************************** PHOTO FRAME *******************************
'''


photoFrame = Frame(window, width=1024, height=720)
canvas = Canvas(
    photoFrame,
    bg="#FFFFFF",
    height=720,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
saida_image_1 = PhotoImage(
    file=relative_to_assets("saida.png"))
saida = canvas.create_image(
    512.0,
    410.0,
    image=saida_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    55.0,
    fill=TEXT[config['INITIAL']['COLOR']],
    outline="")

button_image_1_PhotoFrame = PhotoImage(
    file=relative_to_assets("configuration.png"))
button_1_PhotoFrame = Button(
    image=button_image_1_PhotoFrame,
    borderwidth=0,
    highlightthickness=0,
    command=openConfigurationModal,
    relief="flat"
)
button_1_PhotoFrame.place(
    x=70.0,
    y=1.0,
    width=180.0,
    height=53.0
)

button_image_2_PhotoFrame = PhotoImage(
    file=relative_to_assets("select_datos.png"))
button_2_PhotoFrame = Button(
    image=button_image_2_PhotoFrame,
    borderwidth=0,
    highlightthickness=0,
    command=openSelectFigureModal,
    relief="flat"
)
button_2_PhotoFrame.place(
    x=267.0,
    y=1.0,
    width=180.0,
    height=53.0
)

canvas.create_text(
    259.0,
    80.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Nome do gráfico:"],
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)

button_image_3_PhotoFrame = PhotoImage(
    file=relative_to_assets("home.png"))
button_3_PhotoFrame = Button(
    image=button_image_3_PhotoFrame,
    borderwidth=0,
    highlightthickness=0,
    command=mostrarHomedendeImaxe,
    relief="flat"
)
button_3_PhotoFrame.place(
    x=2.0,
    y=2.0,
    width=51.0,
    height=51.0
)


'''
**************************************************************************
***************************** INITIAL FRAME ******************************
'''

initialFrame = Frame(window, width=1024, height=720)
# intitilizateInitialFrame(initialFrame)
initialFrame.pack(fill=BOTH, expand=1)


def clear_entry():
    initialFrame.destroy()
    # destroyInitialFrame()
    button_5_initialFrame.destroy()
    button_6_initialFrame.destroy()
    button_7_initialFrame.destroy()
    entry_1.destroy()
    mostrar_imaxe()


def loadFileThread():
    global infoData, info
    infoData = []
    showinfo(
        title=TEXT[config['INITIAL']['IDIOMA']]['Arquivo seleccionado:'],
        message=filename
    )
    if type(filename) == str:
        data = parse_file(file=filename)
        info = loadPids(data=data)
        infoData.append([filename, data])
        initial_chart(data=data)
    else:
        for x in filename:
            data = parse_file(file=x)
            info = loadPids(data=data)
            infoData.append([x, data])
            initial_chart(data=data)


def select_path_2():
    global filename
    filetypes = (
        ('Comma-separated values', '*.csv'),
        ('All files', '*.*')
    )

    # Se queremos obter máis dun arquivo temos que modificar a función e
    # chamar a: fd.askopenfilenames
    filename = fd.askopenfilename(
        title=TEXT[config['INITIAL']['IDIOMA']]['Escolla un arquivo:'],
        initialdir='/',
        filetypes=filetypes)

    if filename:
        print(filename, type(filename))
        entry_1.delete(0, tk.END)
        entry_1.insert(0, filename)
        # creating a thread
        Thread_loadFile = Thread(target=loadFileThread)

        # change T to daemon
        Thread_loadFile.daemon = True
        Thread_loadFile.start()
        button_6_initialFrame["state"] = tk.NORMAL
        button_7_initialFrame["state"] = tk.NORMAL


canvas = Canvas(
    initialFrame,
    bg="#3A7FF6",  # 3A7FF6
    height=720,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    513.0,
    0.0,
    1025.0,
    720.0,
    fill="#FCFCFC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    763.5,
    488.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=603.0,
    y=475.0,
    width=321.0,
    height=45.0
)


canvas.create_text(
    608.0,
    466.0,
    text=TEXT[config['INITIAL']['IDIOMA']]["Ruta do arquivo"],
    fill="#515486",
    font=("Inter Regular", int(13.0)),
    anchor="w")

button_image_5_initialFrame = PhotoImage(
    file=relative_to_assets("folder.png"))
button_5_initialFrame = Button(
    image=button_image_5_initialFrame,
    borderwidth=0,
    highlightthickness=0,
    command=select_path_2,
    relief="flat"
)
button_5_initialFrame.place(
    x=897.0,
    y=477.0,
    width=24.0,
    height=22.0
)

button_image_6_initialFrame = PhotoImage(
    file=relative_to_assets("vista_rapida.png"))
button_6_initialFrame = Button(
    image=button_image_6_initialFrame,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry,
    relief="flat",
    disabledforeground='#3A7FF6'
)
button_6_initialFrame.place(
    x=795.0,
    y=600.0,
    width=180.0,
    height=55.0
)

button_image_7_initialFrame = PhotoImage(
    file=relative_to_assets("detallar_datos.png"))
button_7_initialFrame = Button(
    image=button_image_7_initialFrame,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked detallar datos"),
    relief="flat",
    disabledforeground='#3A7FF6'
)
button_7_initialFrame.place(
    x=596.0,
    y=600.0,
    width=180.0,
    height=55.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("citius.png"))
image_1 = canvas.create_image(
    783.0,
    86.0,
    image=image_image_1
)

canvas.create_rectangle(
    40.0,
    160.0,
    100.0,
    165.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    40.0,
    127.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Benvid@ á aplicación"],
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    40.0,
    197.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Esta ferramenta permite crear"],
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    234.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["gráficas para a visualización de"],
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    270.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["datos obtidos dos contadores"],
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    306.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["hardware de servidores NUMA"],
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    169.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Para comezar seleccione o"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    209.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["arquivo que quere procesar no"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    249.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["cadro que aparece a continuación"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    289.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["Este arquivo será procesado pola"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    329.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["aplicación e mostrará un pequeno"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    369.0,
    anchor="nw",
    text=TEXT[config['INITIAL']['IDIOMA']]["resumo do seu contido"],
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)
button_6_initialFrame["state"] = tk.DISABLED
button_7_initialFrame["state"] = tk.DISABLED


window.resizable(False, False)
window.mainloop()

# print(help(OptionMenu))
