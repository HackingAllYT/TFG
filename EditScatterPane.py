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
            height=650,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            36.0,
            19.0,
            286.0,
            94.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            57.0,
            23.0,
            anchor="nw",
            text="X:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            387.0,
            19.0,
            637.0,
            94.0,
            fill="#F1F5FF",
            outline=""
        )

        self.canvas.create_text(
            411.0,
            22.0,
            anchor="nw",
            text="Y:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            737.0,
            19.0,
            987.0,
            94.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            758.0,
            23.0,
            anchor="nw",
            text="Z:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_rectangle(
            737.0,
            132.0,
            987.0,
            207.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_rectangle(
            387.0,
            132.0,
            637.0,
            207.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            411.0,
            141.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Nome da gráfica:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            758.0,
            141.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Cores:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("xerar_button.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.xerarNovoScatter(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_1.place(
            x=602.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_rectangle(
            36.0,
            132.0,
            286.0,
            582.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            387.0,
            282.0,
            anchor="nw",
            text="Outliers:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.minOutlier_entry = IntVar()

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_1 = self.canvas.create_image(
            504.0,
            290.5,
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
            x=468.0 + 5.0,
            y=273.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.maxOutlier_entry = IntVar()

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            601.0,
            290.5,
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
            x=565.0 + 5.0,
            y=273.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.canvas.create_rectangle(
            547.0,
            290.0,
            558.0,
            292.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            387.0,
            249.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            758.0,
            249.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Unir puntos plot:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            482.0,
            309.0,
            anchor="nw",
            text="μ - 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            577.0,
            310.0,
            anchor="nw",
            text="μ + 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            54.0,
            110.0,
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
            x=807.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            506.5,
            182.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=401.0,
            y=168.0,
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
            background='#FFFFFF',
            image=self.classParent.getUnCheckedImage(),
            selectimage=self.classParent.getCheckedImage(),
            indicatoron=False,
            highlightthickness=0,
            borderwidth=0
        )

        self.checkButton.place(
            x=585.0,
            y=249.0,
            width=20.0,
            height=20.0
        )

        self.unirPuntos = IntVar()

        self.unirPuntos_CB = Checkbutton(
            self,
            text='',
            command=self.unirPuntos_changed,
            variable=self.unirPuntos,
            onvalue=1,
            offvalue=0,
            background='#FFFFFF',
            image=self.classParent.getUnCheckedImage(),
            selectimage=self.classParent.getCheckedImage(),
            indicatoron=False,
            highlightthickness=0,
            borderwidth=0
        )

        self.unirPuntos_CB.place(
            x=912.0,
            y=249.0,
            width=20.0,
            height=20.0
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
            x=57.0,
            y=165.0 - 110.0,
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
            x=411.0,
            y=165.0 - 110.0,
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
            x=758.0,
            y=165.0 - 110.0,
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
            x=758.0,
            y=265.0 - 90.0,
            width=170.0,
            height=20.0
        )

        self.treeFrame = Frame(
            self,
            width=235.0,
            height=440.0
        )

        self.treeFrame.place(
            x=42.0,
            y=140.0,
            width=235.0,
            height=440.0
        )

        self.t = CheckboxTreeview(self.treeFrame, show="tree")
        self.t.place(
            x=0.0,
            y=0.0,
            width=235.0,
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

        self.entry_1.config(state=tk.DISABLED, disabledbackground="#F1F5FF")
        self.entry_2.config(state=tk.DISABLED, disabledbackground="#F1F5FF")

    def deleteOutliers_changed(self):
        if self.deleteOutliers.get():
            self.entry_1.config(state=tk.NORMAL)
            self.entry_2.config(state=tk.NORMAL)
        else:
            self.entry_1.config(state=tk.DISABLED)
            self.entry_2.config(state=tk.DISABLED)

    def unirPuntos_changed(self):
        ""

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
