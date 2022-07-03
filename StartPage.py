import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry
from pathlib import Path
import configparser
from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        '''
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        '''

        self.canvas = Canvas(
            self,
            bg="#3A7FF6",  # 3A7FF6
            height=720,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            513.0,
            0.0,
            1025.0,
            720.0,
            fill="#FCFCFC",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            763.5,
            488.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=603.0,
            y=475.0,
            width=321.0,
            height=45.0
        )

        self.canvas.create_text(
            608.0,
            466.0,
            text=TEXT[config['INITIAL']['IDIOMA']]["Ruta do arquivo"],
            fill="#515486",
            font=("Inter Regular", int(13.0)),
            anchor="w")

        self.button_image_5_initialFrame = PhotoImage(
            file=relative_to_assets("folder.png"))
        self.button_5_initialFrame = Button(
            self,
            image=self.button_image_5_initialFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.select_path_2,
            relief="flat"
        )
        self.button_5_initialFrame.place(
            x=897.0,
            y=477.0,
            width=24.0,
            height=22.0
        )

        self.button_image_6_initialFrame = PhotoImage(
            file=relative_to_assets("vista_rapida.png"))
        self.button_6_initialFrame = Button(
            self,
            image=self.button_image_6_initialFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.clear_entry,
            relief="flat",
            disabledforeground='#3A7FF6'
        )
        self.button_6_initialFrame.place(
            x=795.0,
            y=600.0,
            width=180.0,
            height=55.0
        )

        self.button_image_7_initialFrame = PhotoImage(
            file=relative_to_assets("detallar_datos.png"))
        self.button_7_initialFrame = Button(
            self,
            image=self.button_image_7_initialFrame,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openSelectFigureModal,
            relief="flat",
            disabledforeground='#3A7FF6'
        )
        self.button_7_initialFrame.place(
            x=596.0,
            y=600.0,
            width=180.0,
            height=55.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("citius.png"))
        self.image_1 = self.canvas.create_image(
            783.0,
            86.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            40.0,
            160.0,
            100.0,
            165.0,
            fill="#FCFCFC",
            outline="")

        self.canvas.create_text(
            40.0,
            127.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Benvid@ á aplicación"],
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        self.canvas.create_text(
            40.0,
            197.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Esta ferramenta permite crear"],
            fill="#FCFCFC",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            40.0,
            234.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["gráficas para a visualización de"],
            fill="#FCFCFC",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            40.0,
            270.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["datos obtidos dos contadores"],
            fill="#FCFCFC",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            40.0,
            306.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["hardware de servidores NUMA"],
            fill="#FCFCFC",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            169.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Para comezar seleccione o"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            209.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["arquivo que quere procesar no"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            249.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["cadro que aparece a continuación"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            289.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Este arquivo será procesado pola"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            329.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["aplicación e mostrará un pequeno"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        self.canvas.create_text(
            591.0,
            369.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["resumo do seu contido"],
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )
        self.button_6_initialFrame["state"] = tk.DISABLED
        self.button_7_initialFrame["state"] = tk.DISABLED

    def setButtonsEnabled(self):
        self.button_6_initialFrame["state"] = tk.NORMAL
        self.button_7_initialFrame["state"] = tk.NORMAL

    def setEntryName(self, filename):
        self.entry_1.delete(0, tk.END)
        self.entry_1.insert(0, filename)
