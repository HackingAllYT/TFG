from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, BOTH, Button, PhotoImage, ttk, Toplevel, Frame, Radiobutton, StringVar

import tkinter as tk
import configparser

from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


config = configparser.ConfigParser()
config.read('config.ini')


class configurationModal:
    def __init__(self, parent):

        self.top = Toplevel(parent)
        # self.top.transient(parent)
        self.top.title("Configuración")
        self.top.geometry("700x900")
        self.top.resizable(False, False)
        # self.top.overrideredirect(True) # para que non teña os bordes de windows
        self.frame = Frame(self.top, width=700, height=900)

        self.idioma = config['INITIAL']['IDIOMA']
        self.color = config['INITIAL']['COLOR']

        canvas = Canvas(
            self.frame,
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
            fill=TEXT[self.color],
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("cross.png"))
        button_1 = Button(
            self.top,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.ok,
            relief="flat"
        )
        button_1.place(
            x=630.0,
            y=9.0,
            width=58.0,
            height=58.0
        )

        canvas.create_text(
            251.0,
            28.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Configuración xeral:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            64.0,
            177.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Idioma:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            64.0,
            312.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Resolución:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            64.0,
            447.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Cores:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_rectangle(
            483.0,
            153.0,
            554.1099853515625,
            225.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            376.0,
            153.0,
            448.0,
            225.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            260.0,
            153.0,
            339.0,
            225.760009765625,
            fill="#D9D9D9",
            outline="")

        button_image_2 = PhotoImage(
            file=relative_to_assets("galicia.png"))
        button_2 = Button(
            self.top,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.idiomaGalego,
            relief="flat"
        )
        button_2.place(
            x=261.0,
            y=154.0,
            width=77.0,
            height=70.75677490234375
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("spain.png"))
        button_3 = Button(
            self.top,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.idiomaEspanol,
            relief="flat"
        )
        button_3.place(
            x=377.0,
            y=154.0,
            width=70.0,
            height=70.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("uk.png"))
        button_4 = Button(
            self.top,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.idiomaEnglish,
            relief="flat"
        )
        button_4.place(
            x=484.0,
            y=154.0,
            width=69.1064453125,
            height=70.0
        )

        canvas.create_text(
            260.0,
            312.0,
            anchor="nw",
            text="HD",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            351.0,
            312.0,
            anchor="nw",
            text="FullHD",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            476.0,
            312.0,
            anchor="nw",
            text="2K",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            564.0,
            312.0,
            anchor="nw",
            text="4K",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        # Tkinter string variable
        # able to store any string value
        self.resolution = StringVar(self.frame, "1")

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
                self.frame,
                text="",
                variable=self.resolution,
                value=value,
                style='Wild.TRadiobutton'
            ).place(
                x=260 + aux,
                y=342,
                width=30,
                height=30
            )
            aux += 100
        button_image_5 = PhotoImage(
            file=relative_to_assets("aplicar.png"))
        button_5 = Button(
            self.top,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.aplicar,
            relief="flat"
        )
        button_5.place(
            x=508.0,
            y=836.0,
            width=180.0,
            height=55.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("cores/blue_gui.png"))
        button_6 = Button(
            self.top,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorBlue,
            relief="flat"
        )
        button_6.place(
            x=160.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("cores/orange_gui.png"))
        button_7 = Button(
            self.top,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorOrange,
            relief="flat"
        )
        button_7.place(
            x=415.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("cores/green_gui.png"))
        button_8 = Button(
            self.top,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorGreen,
            relief="flat"
        )
        button_8.place(
            x=160.0,
            y=633.0,
            width=212.0,
            height=163.0
        )

        self.frame.pack(fill=BOTH, expand=1)
        self.top.grab_set()
        parent.wait_window()

    def ok(self, event=None):
        # self.valor.set(self.e.get())
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()

    def idiomaGalego(self, event=None):
        self.idioma = 'gal'

    def idiomaEspanol(self, event=None):
        self.idioma = 'es'

    def idiomaEnglish(self, event=None):
        self.idioma = 'en'

    def colorOrange(self, event=None):
        self.color = 'orange'

    def colorGreen(self, event=None):
        self.color = 'green'

    def colorBlue(self, event=None):
        self.color = 'blue'

    def aplicar(self, event=None):
        config.set('INITIAL', 'IDIOMA', self.idioma)
        config.set('INITIAL', 'COLOR', self.color)

        # save to a file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
