import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry, StringVar, IntVar, ttk, Checkbutton
from pathlib import Path
import configparser
from text import TEXT

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class RooflineModelPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.classParent = classParent

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=625,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            24.0,
            0.0,
            274.0,
            75.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            45.0,
            4.0,
            anchor="nw",
            text="X:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            372.0,
            0.0,
            622.0,
            75.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            396.0,
            3.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Tipo de gráfica:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            24.0,
            148.0,
            274.0,
            223.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            44.0,
            159.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Nome da gráfica:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        self.canvas.create_rectangle(
            372.0,
            144.0,
            622.0,
            219.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            393.0,
            148.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Cores:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("xerar_button.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.xerarNovoRooflineModel(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_5.place(
            x=592.0,
            y=454.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_text(
            699.0,
            127.0,
            anchor="nw",
            text="Outliers:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.minOutlier_entry = IntVar()

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_1 = self.canvas.create_image(
            815.0,
            136.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            textvariable=self.minOutlier_entry
        )
        self.entry_1.place(
            x=779.0 + 5.0,
            y=119.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.maxOutlier_entry = IntVar()

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            912.0,
            136.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0,
            textvariable=self.maxOutlier_entry
        )
        self.entry_2.place(
            x=876.0 + 5.0,
            y=119.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.canvas.create_rectangle(
            860.0,
            136.0,
            871.0,
            138.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            725.0,
            196.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            793.0,
            155.0,
            anchor="nw",
            text="μ - 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            888.0,
            156.0,
            anchor="nw",
            text="μ + 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.gardarNovoRooflineModel(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_2.place(
            x=786.0,
            y=454.0,
            width=180.0,
            height=55.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            149.5,
            198.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=44.0,
            y=184.0,
            width=211.0,
            height=27.0
        )

        self.deleteOutliers = IntVar()

        self.checkButton = Checkbutton(
            self,
            text='',
            command=self.deleteOutliers_changed,
            variable=self.deleteOutliers,
            onvalue=1,
            offvalue=0,
            background='#FFFFFF'
        )

        self.checkButton.place(
            x=909.0,
            y=390.0 - 200.0,
            width=72.0,
            height=33.0
        )

        self.xData = StringVar()
        self.xData_cb = ttk.Combobox(
            self,
            textvariable=self.xData,
            width=28
        )

        # prevent typing a value
        self.xData_cb['state'] = 'readonly'

        # place the widget
        # columnas_cb.pack(fill=None, side=LEFT, padx=0, pady=110)
        self.xData_cb.place(
            x=45.0,
            y=165.0 - 120.0,
            width=170.0,
            height=20.0
        )

        self.yData = StringVar()
        self.yData_cb = ttk.Combobox(
            self,
            textvariable=self.yData,
            width=28
        )

        # prevent typing a value
        self.yData_cb['state'] = 'readonly'

        # place the widget
        self.yData_cb.place(
            x=395.0,
            y=165.0 - 120.0,
            width=170.0,
            height=20.0
        )

        self.loadDataItems()

    def loadDataItems(self):
        columns = self.controller.getColumnsFile()
        self.xData_cb['values'] = list(columns)
        self.xData_cb.current(0)
        self.yData_cb['values'] = list(columns)
        self.yData_cb.current(1)

    def deleteOutliers_changed(self):
        print('het')

    def getDataCollected(self):
        ""
        info = {}
        info['name'] = self.entry_3.get()
        info['xRow'] = self.xData.get()
        info['yRow'] = self.yData.get()
        # self.t.on_tree_select(None)
        if self.entry_3.get():
            self.classParent.changeName(self.entry_3.get())
        else:
            info['name'] = 'Roofline Model: ' + self.xData.get()
        return info
