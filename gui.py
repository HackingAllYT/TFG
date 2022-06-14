from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, OptionMenu, Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, ttk, LEFT, BOTH

import tkinter as tk
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno


from migplot import parse_file, initial_chart


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

arquivos = []


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
            title='Selected File',
            message=filename
        )


def confirmExit():
    answer = askyesno(title='Saír?',
                      message='Está seguro que quere pechar?')
    if answer:
        window.destroy()


def display_selected(choice):
    choice = variable.get()
    print(choice)


def edit_button():
    global arquivos
    d = MyDialog(window, arquivos, "Probando Dialogo", "Dame valor")
    window.wait_window(d.top)


def mostrar_imaxe():
    initialFrame.destroy()
    photoFrame.pack(fill=BOTH, expand=1)


def mostrarEdicion():
    photoFrame.destroy()
    button_7.destroy()
    editFrame.pack(fill=BOTH, expand=1)


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


window = Tk()

window.title('Aplicación para a visualización de datos de servidores NUMA')
# window.iconbitmap('assets/citius.ico')
window.wm_attributes('-toolwindow', 'True')

window.geometry("1024x720")
window.configure(bg="#FFFFFF")

editFrame = Frame(window, width=1024, height=720)
#editFrame.pack(fill=BOTH, expand=1)

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
    fill="#7CAEFF",
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
    text="Columnas:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    36.0,
    453.0,
    286.0,
    528.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    57.0,
    460.0,
    anchor="nw",
    text="G-FLOPS:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    384.0,
    453.0,
    634.0,
    528.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    408.0,
    460.0,
    anchor="nw",
    text="Rango inicial:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    737.0,
    453.0,
    987.0,
    528.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    758.0,
    460.0,
    anchor="nw",
    text="Rango final:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    384.0,
    285.0,
    634.0,
    360.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    405.0,
    289.0,
    anchor="nw",
    text="PIDs:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    36.0,
    285.0,
    286.0,
    360.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    57.0,
    289.0,
    anchor="nw",
    text="CPUs:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_rectangle(
    737.0,
    285.0,
    987.0,
    360.0,
    fill="#F1F5FF",
    outline="")

canvas.create_text(
    755.0,
    289.0,
    anchor="nw",
    text="TIDs:",
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
    text="Tipo de datos:",
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
    757.7142944335938,
    125.0,
    anchor="nw",
    text="Outliers:",
    fill="#000000",
    font=("Inter", 15 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=787.0,
    y=608.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=confirmExit,
    relief="flat"
)
button_2.place(
    x=390.0,
    y=1.0,
    width=180.0,
    height=53.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=edit_button,
    relief="flat"
)
button_3.place(
    x=200.0,
    y=1.0,
    width=180.0,
    height=53.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
button_4.place(
    x=10.0,
    y=1.0,
    width=180.0,
    height=53.0
)


countries = ['Bahamas', 'Canada', 'Cuba', 'United States']


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

columnas = StringVar()
columnas_cb = ttk.Combobox(editFrame, textvariable=columnas, width=28)

# get first 3 letters of every month name
columnas_cb['values'] = [countries[m][0:1] for m in range(4)]

# prevent typing a value
columnas_cb['state'] = 'readonly'

# place the widget
#columnas_cb.pack(fill=None, side=LEFT, padx=0, pady=110)
columnas_cb.grid(column=5, row=5, padx=53, pady=145)
columnas_cb.current()


tipo_datos = StringVar()
tipoDatos_cb = ttk.Combobox(editFrame, textvariable=tipo_datos, width=28)

# get first 3 letters of every month name
tipoDatos_cb['values'] = [countries[m][0:2] for m in range(4)]

# prevent typing a value
tipoDatos_cb['state'] = 'readonly'

# place the widget
tipoDatos_cb.grid(column=20, row=5, padx=110, pady=145)
tipoDatos_cb.current()


outliers = StringVar()
outliers_cb = ttk.Combobox(editFrame, textvariable=outliers, width=28)

# get first 3 letters of every month name
outliers_cb['values'] = [countries[m][0:3] for m in range(4)]

# prevent typing a value
outliers_cb['state'] = 'readonly'

# place the widget
outliers_cb.grid(column=35, row=5, padx=45, pady=150)
outliers_cb.current()

'''
***************************************************************************
'''
cpu_columns = StringVar()
cpu_cb = ttk.Combobox(editFrame, textvariable=cpu_columns, width=28)

# get first 3 letters of every month name
cpu_cb['values'] = [countries[m][0:4] for m in range(4)]

# prevent typing a value
cpu_cb['state'] = 'readonly'

# place the widget
cpu_cb.grid(column=5, row=6, padx=0, pady=0)
cpu_cb.current()


pid = StringVar()
pid_cb = ttk.Combobox(editFrame, textvariable=pid, width=28)

# get first 3 letters of every month name
pid_cb['values'] = [countries[m][0:5] for m in range(4)]

# prevent typing a value
pid_cb['state'] = 'readonly'

# place the widget
pid_cb.grid(column=20, row=6, padx=0, pady=0)
pid_cb.current()

tid = StringVar()
tid_cb = ttk.Combobox(editFrame, textvariable=tid, width=28)

# get first 3 letters of every month name
tid_cb['values'] = [countries[m][0:6] for m in range(4)]

# prevent typing a value
tid_cb['state'] = 'readonly'

# place the widget
tid_cb.grid(column=35, row=6, padx=45, pady=0)
tid_cb.current()


'''
***************************************************************************
'''
g_flops = StringVar()
gflops_cb = ttk.Combobox(editFrame, textvariable=g_flops, width=28)

# get first 3 letters of every month name
gflops_cb['values'] = [countries[m][0:7] for m in range(4)]

# prevent typing a value
gflops_cb['state'] = 'readonly'

# place the widget
gflops_cb.grid(column=5, row=7, padx=0, pady=150)
gflops_cb.current()


rang_inicial = StringVar()
rangInicial_cb = ttk.Combobox(editFrame, textvariable=rang_inicial, width=28)

# get first 3 letters of every month name
rangInicial_cb['values'] = [countries[m][0:8] for m in range(4)]

# prevent typing a value
rangInicial_cb['state'] = 'readonly'

# place the widget
rangInicial_cb.grid(column=20, row=7, padx=0, pady=150)
rangInicial_cb.current()

rang_final = StringVar()
rangFinal_cb = ttk.Combobox(editFrame, textvariable=rang_final, width=28)

# get first 3 letters of every month name
rangFinal_cb['values'] = [countries[m][0:9] for m in range(4)]

# prevent typing a value
rangFinal_cb['state'] = 'readonly'

# place the widget
rangFinal_cb.grid(column=35, row=7, padx=45, pady=150)
rangFinal_cb.current()

'''
# Choosing selectmode as multiple
# for selecting multiple options
list = tk.Listbox(window, selectmode="multiple")

# Widget expands horizontally and
# vertically by assigning both to
# fill option
list.grid(column=21, row=7, padx=0, pady=150)

# Taking a list 'x' with the items
# as languages
x = ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby", "JavaScript", "Swift"]

for each_item in range(len(x)):

    list.insert(tk.END, x[each_item])

    # coloring alternative lines of listbox
    list.itemconfig(each_item,
                    bg="yellow" if each_item % 2 == 0 else "cyan")
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
    403.0,
    image=saida_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    55.0,
    fill="#7CAEFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    55.0,
    fill="#7CAEFF",
    outline="")

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=mostrarEdicion,
    relief="flat"
)
button_7.place(
    x=0.0,
    y=2.0,
    width=180.0,
    height=53.0
)

canvas.create_text(
    259.0,
    80.0,
    anchor="nw",
    text="Nome do gráfico:",
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)

#############################

initialFrame = Frame(window, width=1024, height=720)
initialFrame.pack(fill=BOTH, expand=1)


def clear_entry():
    initialFrame.destroy()
    button_5.destroy()
    button_6.destroy()
    entry_1.destroy()
    # editFrame.pack(fill=BOTH, expand=1)
    mostrar_imaxe()


def select_path_2():
    filetypes = (
        ('Comma-separated values', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        print(filename, type(filename))
        entry_1.delete(0, tk.END)
        entry_1.insert(0, filename)
        for x in filename:
            data = parse_file(file=x)
            initial_chart(data=data)
            showinfo(
                title='Selected File',
                message=filename
            )


canvas = Canvas(
    initialFrame,
    bg="#3A7FF6",
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
    768.5,
    457.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=608.0,
    y=427.0 + 19,
    width=280.0,
    height=40.0
)


canvas.create_text(
    608.0,
    435.0,
    text="Ruta do arquivo",
    fill="#515486",
    font=("Inter Regular", int(13.0)),
    anchor="w")

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=select_path_2,
    relief="flat"
)
button_5.place(
    x=902.0,
    y=446.0,
    width=24.0,
    height=22.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry,
    relief="flat"
)
button_6.place(
    x=795.0,
    y=600.0,
    width=180.0,
    height=55.0
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
    text="Benvid@ á aplicación",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    40.0,
    197.0,
    anchor="nw",
    text="Esta ferramenta permite crear",
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    234.0,
    anchor="nw",
    text="gráficas para a visualización de",
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    270.0,
    anchor="nw",
    text="datos obtidos dos contadores",
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    40.0,
    306.0,
    anchor="nw",
    text="hardware de servidores NUMA",
    fill="#FCFCFC",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    125.0,
    anchor="nw",
    text="Para comezar seleccione o",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    165.0,
    anchor="nw",
    text="arquivo que quere procesar no",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    205.0,
    anchor="nw",
    text="cadro que aparece a continuación",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    245.0,
    anchor="nw",
    text="Este arquivo serrá procesado pola",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    285.0,
    anchor="nw",
    text="aplicación e mostrará un pequeno",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    591.0,
    325.0,
    anchor="nw",
    text="resumo do seu contido",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)


window.resizable(False, False)
window.mainloop()

# print(help(OptionMenu))
