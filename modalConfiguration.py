from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Button, PhotoImage, ttk, StringVar

import tkinter as tk
import configparser

from text import TEXT, RESOLU


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


GAL = 'gal'
CAS = 'es'
ENG = 'en'

BLUE = ('blue', 'blue-bg')
LIGHT_BLUE = ('light-blue', 'light-blue-bg')
GREEN = ('green', 'green-bg')
ORANGE = ('orange', 'orange-bg')


class configurationModal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = parent
        self.title("Configuración")
        self.geometry("700x900")
        self.resizable(False, False)

        self.idioma = config['INITIAL']['IDIOMA']
        self.color = config['INITIAL']['COLOR']
        self.colorBg = config['INITIAL']['COLOR-BG']

        self.auxRoute = 'cores/' + config['INITIAL']['idioma'] + '/'

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=900,
            width=700,
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
            fill=TEXT[config['INITIAL']['COLOR-BG']],
            outline="")

        self.canvas.create_text(
            251.0,
            28.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Configuración xeral:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            177.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Idioma:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            312.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Resolución:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            447.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Cores:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_rectangle(
            483.0,
            153.0,
            554.1099853515625,
            225.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            376.0,
            153.0,
            448.0,
            225.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            260.0,
            153.0,
            339.0,
            225.760009765625,
            fill="#D9D9D9",
            outline="")

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("galicia.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(GAL),
            relief="flat"
        )
        self.button_2.place(
            x=261.0,
            y=154.0,
            width=77.0,
            height=70.75677490234375
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("spain.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(CAS),
            relief="flat"
        )
        self.button_3.place(
            x=377.0,
            y=154.0,
            width=70.0,
            height=70.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("uk.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(ENG),
            relief="flat"
        )
        self.button_4.place(
            x=484.0,
            y=154.0,
            width=69.1064453125,
            height=70.0
        )

        self.canvas.create_text(
            260.0,
            312.0,
            anchor="nw",
            text="HD",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            351.0,
            312.0,
            anchor="nw",
            text="FullHD",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            476.0,
            312.0,
            anchor="nw",
            text="2K",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            564.0,
            312.0,
            anchor="nw",
            text="4K",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        # Tkinter string variable
        # able to store any string value
        self.screenResolution = StringVar(self, "1")

        # Dictionary to create multiple buttons
        values = {
            "RadioButton 1": "1",
            "RadioButton 2": "2",
            "RadioButton 3": "3",
            "RadioButton 4": "4"
        }
        s = ttk.Style()                     # Creating style element
        s.configure(
            # First argument is the name of style. Needs to end with: .TRadiobutton
            'Wild.TRadiobutton',
            background="#FFFFFF",         # Setting background to our specified color above
            foreground='black'
        )         # You can define colors like this also

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        aux = 0
        for (text, value) in values.items():
            ttk.Radiobutton(
                self,
                text="",
                variable=self.screenResolution,
                value=value,
                style='Wild.TRadiobutton'
            ).place(
                x=260 + aux,
                y=342,
                width=30,
                height=30
            )
            aux += 100

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("aplicar.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.reiniciarApp,
            relief="flat"
        )
        self.button_5.place(
            x=450.0,
            y=828.0,
            width=180.0,
            height=55.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("gardar_button.png"))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.aplicar,
            relief="flat"
        )
        self.button_6.place(
            x=160.0,
            y=828.0,
            width=180.0,
            height=55.0
        )

        # Azul claro
        name = self.auxRoute + 'azul_claro.png'
        self.button_image_10 = PhotoImage(
            file=relative_to_assets(name))
        self.button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(LIGHT_BLUE),
            relief="flat"
        )
        self.button_10.place(
            x=415.0,
            y=633.0,
            width=212.0,
            height=163.0
        )

        # Azul
        name = self.auxRoute + 'azul.png'
        self.button_image_7 = PhotoImage(
            file=relative_to_assets(name))
        self.button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(BLUE),
            relief="flat"
        )
        self.button_7.place(
            x=160.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        # Verde
        name = self.auxRoute + 'verde.png'
        self.button_image_8 = PhotoImage(
            file=relative_to_assets(name))
        self.button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(GREEN),
            relief="flat"
        )
        self.button_8.place(
            x=415.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        # Laranxa
        name = self.auxRoute + 'laranxa.png'
        self.button_image_9 = PhotoImage(
            file=relative_to_assets(name))
        self.button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.languageColorClicked(ORANGE),
            relief="flat"
        )
        self.button_9.place(
            x=160.0,
            y=633.0,
            width=212.0,
            height=163.0
        )

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_4.bind('<Enter>', self.button_4_enter)
        self.button_4.bind('<Leave>', self.button_4_leave)

        self.button_5.bind('<Enter>', self.button_5_enter)
        self.button_5.bind('<Leave>', self.button_5_leave)

        self.button_6.bind('<Enter>', self.button_6_enter)
        self.button_6.bind('<Leave>', self.button_6_leave)

        self.button_7.bind('<Enter>', self.button_7_enter)
        self.button_7.bind('<Leave>', self.button_7_leave)

        self.button_8.bind('<Enter>', self.button_8_enter)
        self.button_8.bind('<Leave>', self.button_8_leave)

        self.button_9.bind('<Enter>', self.button_9_enter)
        self.button_9.bind('<Leave>', self.button_9_leave)

        self.button_10.bind('<Enter>', self.button_10_enter)
        self.button_10.bind('<Leave>', self.button_10_leave)

        self.changes = False

    '''
    *******************************************************************************
    ******************* Funcións de control do modal en xeral  ********************
    *******************************************************************************
    '''

    def show(self):
        self.deiconify()
        self.transient(self.controller)
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        # self.parent.eval(f'tk::PlaceWindow {str(self)} center')
        self.center()
        self.wait_window(self)
        return self.changes

    def ok(self, event=None):
        # self.valor.set(self.e.get())
        self.destroy()

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

    def languageColorClicked(self, value):
        if type(value) == tuple:
            self.color = value[0]
            self.colorBg = value[1]
        else:
            self.idioma = value
        self.changes = True

    def aplicar(self, event=None):
        config.set('INITIAL', 'IDIOMA', self.idioma)
        config.set('INITIAL', 'COLOR', self.color)
        config.set('INITIAL', 'COLOR-BG', self.colorBg)
        config.set('INITIAL', 'RESOLU',
                   RESOLU[self.screenResolution.get()])

        # save to a file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def reiniciarApp(self, event=None):
        self.aplicar()
        self.controller.askReloadApp()

    '''
    *******************************************************************************
    ******************* Funcións para facer efectos nos botóns  *******************
    *******************************************************************************
    '''

    def button_2_enter(self, e):
        ""

    def button_2_leave(self, e):
        ""

    def button_3_enter(self, e):
        ""

    def button_3_leave(self, e):
        ""

    def button_4_enter(self, e):
        ""

    def button_4_leave(self, e):
        ""

    def button_5_enter(self, e):
        '''name = self.auxRoute + 'folder_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_5["image"] = aux
        self.button_5.image = aux'''

    def button_5_leave(self, e):
        self.button_5["image"] = self.button_image_5

    def button_6_enter(self, e):
        '''name = self.auxRoute + 'folder_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_6["image"] = aux
        self.button_6.image = aux'''

    def button_6_leave(self, e):
        self.button_6["image"] = self.button_image_6

    def button_7_enter(self, e):
        name = self.auxRoute + 'azul_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_7["image"] = aux
        self.button_7.image = aux

    def button_7_leave(self, e):
        self.button_7["image"] = self.button_image_7

    def button_8_enter(self, e):
        name = self.auxRoute + 'verde_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_8["image"] = aux
        self.button_8.image = aux

    def button_8_leave(self, e):
        self.button_8["image"] = self.button_image_8

    def button_9_enter(self, e):
        name = self.auxRoute + 'laranxa_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_9["image"] = aux
        self.button_9.image = aux

    def button_9_leave(self, e):
        self.button_9["image"] = self.button_image_9

    def button_10_enter(self, e):
        name = self.auxRoute + 'azul_claro_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_10["image"] = aux
        self.button_10.image = aux

    def button_10_leave(self, e):
        self.button_10["image"] = self.button_image_10
