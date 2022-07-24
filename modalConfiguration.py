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
        self.title(TEXT[config['INITIAL']['IDIOMA']]["Configuración"])
        self.geometry("700x900")
        self.resizable(False, False)

        self.config = self.controller.getConfig()

        self.idioma = self.config['INITIAL']['IDIOMA']
        self.color = self.config['INITIAL']['COLOR']
        self.colorBg = self.config['INITIAL']['COLOR-BG']

        self.auxRoute = 'cores/' + self.config['INITIAL']['idioma'] + '/'

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
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        self.canvas.create_text(
            251.0,
            28.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Configuración xeral:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            177.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Idioma:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            312.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Resolución:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            64.0,
            447.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Cores:"],
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
            x=259.0,
            y=152.0,
            width=83.0,
            height=76.760009765625
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
            x=375.0,
            y=152.0,
            width=76.0,
            height=76.0
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
            x=482.0,
            y=152.0,
            width=75.1099853515625,
            height=76.0
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

        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'aplicar.png'
        self.button_image_5 = PhotoImage(
            file=relative_to_assets(name))
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

        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'gardar.png'
        self.button_image_6 = PhotoImage(
            file=relative_to_assets(name))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.gardar,
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

        self.setSelectedItems()

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
    **************** Funcións de control de seleccións dos botóns  ****************
    *******************************************************************************
    '''

    def setSelectedItems(self, value: str = None, valueType: str = 'color'):
        aux = {
            'gal': [self.button_2, 'galicia_over.png', self.button_image_2],
            'es': [self.button_3, 'spain_over.png', self.button_image_3],
            'en': [self.button_4, 'uk_over.png', self.button_image_4],
            'blue': [self.button_7, self.auxRoute + 'azul_over.png', self.button_image_7],
            'green': [self.button_8, self.auxRoute + 'verde_over.png', self.button_image_8],
            'orange': [self.button_9, self.auxRoute + 'laranxa_over.png', self.button_image_9],
            'light-blue': [self.button_10, self.auxRoute + 'azul_claro_over.png', self.button_image_10]
        }
        if value:
            if valueType == 'color':
                aux[self.color][0]["image"] = aux[self.color][2]
            elif valueType == 'lang':
                aux[self.idioma][0]["image"] = aux[self.idioma][2]
            img = PhotoImage(
                file=relative_to_assets(aux[value][1])
            )
            aux[value][0]["image"] = img
            aux[value][0].image = img
        else:
            img = PhotoImage(
                file=relative_to_assets(aux[self.color][1])
            )
            aux[self.color][0]["image"] = img
            aux[self.color][0].image = img

            img = PhotoImage(
                file=relative_to_assets(aux[self.idioma][1])
            )
            aux[self.idioma][0]["image"] = img
            aux[self.idioma][0].image = img

    '''
    *******************************************************************************
    **************** Funcións de control de pulsacións nos botóns  ****************
    *******************************************************************************
    '''

    def languageColorClicked(self, value):
        if type(value) == tuple:
            self.setSelectedItems(value[0], 'color')
            self.color = value[0]
            self.colorBg = value[1]
        else:
            self.setSelectedItems(value, 'lang')
            self.idioma = value
        self.changes = True

    def gardar(self):
        self.aplicar()
        self.controller.showMessage(
            TEXT[self.config['INITIAL']['IDIOMA']]['info-reload'],
            TEXT[self.config['INITIAL']['IDIOMA']]['info-reload-text']
        )

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
        name = 'galicia_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        if self.idioma != GAL:
            self.button_2["image"] = self.button_image_2

    def button_3_enter(self, e):
        name = 'spain_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_3["image"] = aux
        self.button_3.image = aux

    def button_3_leave(self, e):
        if self.idioma != CAS:
            self.button_3["image"] = self.button_image_3

    def button_4_enter(self, e):
        name = 'uk_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_4["image"] = aux
        self.button_4.image = aux

    def button_4_leave(self, e):
        if self.idioma != ENG:
            self.button_4["image"] = self.button_image_4

    def button_7_enter(self, e):
        name = self.auxRoute + 'azul_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_7["image"] = aux
        self.button_7.image = aux

    def button_7_leave(self, e):
        if self.color != BLUE[0]:
            self.button_7["image"] = self.button_image_7

    def button_8_enter(self, e):
        name = self.auxRoute + 'verde_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_8["image"] = aux
        self.button_8.image = aux

    def button_8_leave(self, e):
        if self.color != GREEN[0]:
            self.button_8["image"] = self.button_image_8

    def button_9_enter(self, e):
        name = self.auxRoute + 'laranxa_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_9["image"] = aux
        self.button_9.image = aux

    def button_9_leave(self, e):
        if self.color != ORANGE[0]:
            self.button_9["image"] = self.button_image_9

    def button_10_enter(self, e):
        name = self.auxRoute + 'azul_claro_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_10["image"] = aux
        self.button_10.image = aux

    def button_10_leave(self, e):
        if self.color != LIGHT_BLUE[0]:
            self.button_10["image"] = self.button_image_10

    def button_5_enter(self, e):
        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'aplicar_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_5["image"] = aux
        self.button_5.image = aux

    def button_5_leave(self, e):
        self.button_5["image"] = self.button_image_5

    def button_6_enter(self, e):
        name = self.auxRoute + \
            self.config['INITIAL']['COLOR'] + '/' + 'gardar_over.png'
        aux = PhotoImage(
            file=relative_to_assets(name)
        )
        self.button_6["image"] = aux
        self.button_6.image = aux

    def button_6_leave(self, e):
        self.button_6["image"] = self.button_image_6
