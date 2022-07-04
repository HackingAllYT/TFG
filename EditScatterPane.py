import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry, StringVar, IntVar, ttk, Checkbutton, Frame, BOTH
from pathlib import Path
import configparser
from text import TEXT
from checkBoxTreeview import CheckboxTreeview

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ScatterPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
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
            30.0,
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
            outline=""
        )

        self.canvas.create_text(
            396.0,
            3.0,
            anchor="nw",
            text="Y:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            725.0,
            0.0,
            975.0,
            75.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            746.0,
            4.0,
            anchor="nw",
            text="Z:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            725.0,
            95.0,
            975.0,
            170.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_rectangle(
            725.0,
            317.0,
            975.0,
            392.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            745.0,
            328.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Nome da gráfica:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        self.canvas.create_text(
            746.0,
            99.0,
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
            command=lambda: controller.xerarNovoScatter(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_5.place(
            x=625.0,
            y=571.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_rectangle(
            24.0,
            113.0,
            694.0,
            563.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            725.0,
            207.0,
            anchor="nw",
            text="Outliers:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.minOutlier_entry = IntVar()

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_1 = self.canvas.create_image(
            841.0,
            216.5,
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
            x=805.0 + 5.0,
            y=199.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.maxOutlier_entry = IntVar()

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            938.0,
            216.5,
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
            x=902.0 + 5.0,
            y=199.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.canvas.create_rectangle(
            886.0,
            216.0,
            897.0,
            218.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            751.0,
            276.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            819.0,
            235.0,
            anchor="nw",
            text="μ - 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            914.0,
            236.0,
            anchor="nw",
            text="μ + 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            45.0,
            91.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Seleccione PIDs e TIDs a empregar:"],
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=819.0,
            y=571.0,
            width=180.0,
            height=55.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            850.5,
            367.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=745.0,
            y=353.0,
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
            y=390.0 - 120.0,
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

        self.zData = StringVar()
        self.zData_cb = ttk.Combobox(
            self,
            textvariable=self.zData,
            width=28
        )

        # prevent typing a value
        self.zData_cb['state'] = 'readonly'

        # place the widget
        self.zData_cb.place(
            x=745.0,
            y=165.0 - 120.0,
            width=170.0,
            height=20.0
        )

        self.colors = StringVar()
        self.colors_cb = ttk.Combobox(
            self,
            textvariable=self.colors,
            width=28
        )

        # prevent typing a value
        self.colors_cb['state'] = 'readonly'

        # place the widget
        self.colors_cb.place(
            x=745.0,
            y=265.0 - 120.0,
            width=170.0,
            height=20.0
        )

        self.treeFrame = Frame(
            self,
            width=660.0,
            height=440.0
        )

        self.treeFrame.place(
            x=30.0,
            y=118.0,
            width=660.0,
            height=440.0
        )

        self.t = CheckboxTreeview(self.treeFrame, show="tree")
        self.t.place(
            x=0.0,
            y=0.0,
            width=660.0,
            height=440.0
        )

        self.loadDataItems()

    def loadDataItems(self):
        columns = self.controller.getColumnsFile()
        self.xData_cb['values'] = list(columns)
        self.xData_cb.current(0)
        self.yData_cb['values'] = list(columns)
        self.yData_cb.current(1)
        self.zData_cb['values'] = list(columns)
        self.zData_cb.current(5)
        info = self.controller.getPidsTids()
        self.t.insertElements(info)

    def deleteOutliers_changed(self):
        print('het')

    def getDataCollected(self):
        info = {}
        info['name'] = self.entry_3.get()
        info['xRow'] = self.xData.get()
        info['yRow'] = self.yData.get()
        info['zRow'] = self.zData.get()

        if self.entry_3.get():
            self.classParent.changeName(self.entry_3.get())
        else:
            info['name'] = 'Scatter: ' + self.zData.get()
        # self.t.on_tree_select(None)
        return info
