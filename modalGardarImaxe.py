from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Entry, Button, PhotoImage, filedialog, ttk, StringVar, IntVar

import tkinter as tk

from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class gardarImaxeModal(tk.Toplevel):
    def __init__(self, parent, info):
        super().__init__(parent)

        self.parent = parent

        self.config = self.parent.getConfig()

        self.auxRoute = 'cores/gal/'

        self.graphType = info['graphType']
        self.title(TEXT[self.config['INITIAL']['IDIOMA']]['Gardar imaxe como'])
        self.geometry("557x650")
        self.resizable(False, False)

        self.idioma = self.config['INITIAL']['IDIOMA']
        self.color = self.config['INITIAL']['COLOR']

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=650,
            width=557,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            80.0,
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        self.canvas.create_text(
            106.0,
            28.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Seleccione tipo de arquivo de saída"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'okey.png'
        self.button_image_2 = PhotoImage(
            file=relative_to_assets(name))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.okey,
            relief="flat"
        )
        self.button_2.place(
            x=65.0,
            y=557.0,
            width=180.0,
            height=55.0
        )

        name = self.auxRoute + 'cancelar.png'
        self.button_image_3 = PhotoImage(
            file=relative_to_assets(name))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.cancel,
            relief="flat"
        )
        self.button_3.place(
            x=313.0,
            y=557.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_rectangle(
            95.0,
            139.0,
            463.0,
            214.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            106.0,
            147.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Escolla o formato:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_rectangle(
            95.0,
            241.0,
            463.0,
            316.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            106.0,
            249.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Escolla a carpeta destino:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("folder.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.selectDirectory,
            relief="flat"
        )
        self.button_4.place(
            x=407.0,
            y=262.0,
            width=24.0,
            height=22.0
        )

        self.fileFormat = StringVar()
        self.fileFormat_cb = ttk.Combobox(
            self,
            textvariable=self.fileFormat,
            width=28
        )

        self.fileFormat_cb['values'] = [
            'png', 'jpg', 'jpeg', 'webp', 'svg', 'pdf'
        ]

        # prevent typing a value
        self.fileFormat_cb['state'] = 'readonly'

        # place the widget
        self.fileFormat_cb.place(
            x=106.0,
            y=182.5,
            width=300.0,
            height=25.0
        )
        self.fileFormat_cb.current(0)

        self.width_entry = IntVar()
        self.height_entry = IntVar()

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_witdhXheight.png"))
        self.entry_bg_1 = self.canvas.create_image(
            155.0,
            389.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            textvariable=self.width_entry
        )
        self.entry_1.place(
            x=100.0,
            y=369.0,
            width=110.0,
            height=38.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_folder.png"))
        self.entry_bg_2 = self.canvas.create_image(
            229.0,
            291.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=106.0,
            y=275.0,
            width=246.0,
            height=30.0
        )

        self.plotName_entry = StringVar()

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_folder.png"))
        self.entry_bg_3 = self.canvas.create_image(
            229.0,
            486.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            textvariable=self.plotName_entry
        )
        self.entry_3.place(
            x=106.0,
            y=470.0,
            width=260.0,
            height=30.0
        )

        self.canvas.create_text(
            105.0,
            345.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Ancho:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            357.0,
            346.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Alto:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_rectangle(
            95.0,
            436.0,
            463.0,
            511.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            106.0,
            444.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Introduza o nome da gráfica:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_witdhXheight.png"))
        self.entry_bg_4 = self.canvas.create_image(
            403.0,
            389.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            textvariable=self.height_entry
        )
        self.entry_4.place(
            x=348.0,
            y=369.0,
            width=110.0,
            height=38.0
        )

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.format = 'png'
        self.dir = '/'
        self.result = {}
        self.result['do'] = False
        self.isAskDirectory = False

        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, info['name'])

        self.width_entry.set(self.config['FIGURE-DEFAULT']['width'])
        self.height_entry.set(self.config['FIGURE-DEFAULT']['height'])

    def show(self):
        self.deiconify()
        self.transient(self.parent)
        self.wm_protocol("WM_DELETE_WINDOW", self.destroyPop)
        self.center()
        self.wait_window(self)
        self.result['dir'] = self.dir
        self.result['format'] = self.format
        self.result['type'] = self.graphType
        self.result['name'] = self.plotName_entry.get()

        try:
            self.result['w'] = int(self.width_entry.get())
        except:
            self.result['w'] = self.config['FIGURE-DEFAULT']['width']
        try:
            self.result['h'] = int(self.height_entry.get())
        except:
            self.result['h'] = self.config['FIGURE-DEFAULT']['height']

        self.result['wc'] = int(self.config['FIGURE-DEFAULT']['width'])
        self.result['hc'] = int(self.config['FIGURE-DEFAULT']['height'])
        return self.result

    def center(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

    '''
    *******************************************************************************
    **************** Funcións de control de pulsacións nos botóns  ****************
    *******************************************************************************
    '''

    def okey(self, event=None):
        self.format = self.fileFormat.get()
        self.result['do'] = True
        self.destroy()

    def cancel(self, event=None):
        self.destroy()

    def selectDirectory(self):
        self.isAskDirectory = True
        self.dir = filedialog.askdirectory()
        self.entry_2.delete(0, tk.END)
        self.entry_2.insert(0, self.dir)
        self.isAskDirectory = False

    def destroyPop(self, event=None):
        if not self.isAskDirectory:
            self.destroy()

    '''
    *******************************************************************************
    ******************* Funcións para facer efectos nos botóns  *******************
    *******************************************************************************
    '''

    def button_2_enter(self, e):
        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'okey_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        self.button_2["image"] = self.button_image_2

    def button_3_enter(self, e):
        name = self.auxRoute + 'cancelar_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_3["image"] = aux
        self.button_3.image = aux

    def button_3_leave(self, e):
        self.button_3["image"] = self.button_image_3
