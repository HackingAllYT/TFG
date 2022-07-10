import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry
from pathlib import Path
import configparser
from text import TEXT, RESOLU


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        if config["INITIAL"]['RESOLU'] == 'HD':
            self.__init_HD__(controller)

    def __init_HD__(self, controller):
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.saida_image_1 = PhotoImage(
            file=relative_to_assets("saida.png"))
        self.saida = self.canvas.create_image(
            512.0,
            410.0,
            image=self.saida_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            55.0,
            fill=TEXT[config['INITIAL']['COLOR-BG']],
            outline="")

        self.button_image_1_PhotoFrame = PhotoImage(
            file=relative_to_assets("configuration.png"))
        self.button_1_PhotoFrame = Button(
            self,
            image=self.button_image_1_PhotoFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openConfigurationModal,
            relief="flat"
        )
        self.button_1_PhotoFrame.place(
            x=70.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        self.button_image_2_PhotoFrame = PhotoImage(
            file=relative_to_assets("select_datos.png"))
        self.button_2_PhotoFrame = Button(
            self,
            image=self.button_image_2_PhotoFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openSelectFigureModal,
            relief="flat"
        )
        self.button_2_PhotoFrame.place(
            x=267.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        self.canvas.create_text(
            259.0,
            80.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Nome do gráfico:"],
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.button_image_3_PhotoFrame = PhotoImage(
            file=relative_to_assets("home.png"))
        self.button_3_PhotoFrame = Button(
            self,
            image=self.button_image_3_PhotoFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.mostrarHomedendeImaxe,
            relief="flat"
        )
        self.button_3_PhotoFrame.place(
            x=2.0,
            y=2.0,
            width=51.0,
            height=51.0
        )
