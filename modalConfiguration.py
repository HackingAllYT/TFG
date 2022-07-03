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


class configurationModal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.title("Configuración")
        self.geometry("700x900")
        self.resizable(False, False)

        self.idioma = config['INITIAL']['IDIOMA']
        self.color = config['INITIAL']['COLOR']

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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("cross.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.ok,
            relief="flat"
        )
        self.button_1.place(
            x=630.0,
            y=9.0,
            width=58.0,
            height=58.0
        )

        self.canvas.create_text(
            251.0,
            28.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Configuración xeral:"],
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
            command=self.idiomaGalego,
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
            command=self.idiomaEspanol,
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
            command=self.idiomaEnglish,
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
            command=self.aplicar,
            relief="flat"
        )
        self.button_5.place(
            x=508.0,
            y=836.0,
            width=180.0,
            height=55.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("cores/blue_gui.png"))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorBlue,
            relief="flat"
        )
        self.button_6.place(
            x=160.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("cores/orange_gui.png"))
        self.button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorOrange,
            relief="flat"
        )
        self.button_7.place(
            x=415.0,
            y=443.0,
            width=212.0,
            height=163.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("cores/green_gui.png"))
        self.button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.colorGreen,
            relief="flat"
        )
        self.button_8.place(
            x=160.0,
            y=633.0,
            width=212.0,
            height=163.0
        )
        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

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

        self.changes = False

    def select(self):
        selection = self.listbox.curselection()
        if selection:
            self.selection = self.listbox.get(selection[0])
        self.destroy()

    def show(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.parent.eval(f'tk::PlaceWindow {str(self)} center')
        self.wait_window(self)
        return self.changes

    def destroyPop(self, event=None):
        self.destroy()

    def ok(self, event=None):
        # self.valor.set(self.e.get())
        self.destroy()

    def cancel(self, event=None):
        self.destroy()

    def idiomaGalego(self, event=None):
        self.idioma = 'gal'
        self.changes = True

    def idiomaEspanol(self, event=None):
        self.idioma = 'es'
        self.changes = True

    def idiomaEnglish(self, event=None):
        self.idioma = 'en'
        self.changes = True

    def colorOrange(self, event=None):
        self.color = 'orange'
        self.changes = True

    def colorGreen(self, event=None):
        self.color = 'green'
        self.changes = True

    def colorBlue(self, event=None):
        self.color = 'blue'
        self.changes = True

    def aplicar(self, event=None):
        config.set('INITIAL', 'IDIOMA', self.idioma)
        config.set('INITIAL', 'COLOR', self.color)

        # save to a file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def button_1_enter(self, e):
        aux = PhotoImage(
            file=relative_to_assets("cross_62x62.png")
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

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
        ""

    def button_5_leave(self, e):
        ""

    def button_6_enter(self, e):
        ""

    def button_6_leave(self, e):
        ""

    def button_7_enter(self, e):
        ""

    def button_7_leave(self, e):
        ""

    def button_8_enter(self, e):
        ""

    def button_8_leave(self, e):
        ""
