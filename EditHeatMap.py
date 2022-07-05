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


class HeatMapPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent)
        '''
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        '''
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
            text=TEXT[config['INITIAL']['IDIOMA']]["Tipo dato Z:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        self.canvas.create_rectangle(
            737.0,
            245.0,
            987.0,
            320.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            758.0,
            250.0,
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
            command=lambda: controller.xerarNovoHeatmap(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_1.place(
            x=602.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        # Treeview rectangle
        self.canvas.create_rectangle(
            36.0,
            132.0,
            286.0,
            582.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            387.0,
            281.0,
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
            289.5,
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
            y=272.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.maxOutlier_entry = IntVar()

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            601.0,
            289.5,
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
            y=272.0 + 1.0,
            width=72.0 - 7.0,
            height=33.0
        )

        self.canvas.create_rectangle(
            547.0,
            289.0,
            558.0,
            291.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            387.0,
            246.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            482.0,
            308.0,
            anchor="nw",
            text="μ - 2σ",
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            577.0,
            309.0,
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
            command=lambda: controller.gardarNovoHeatMap(
                self.getDataCollected()),
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

        self.z_tipoDatos = StringVar()
        self.z_tipoDatos_cb = ttk.Combobox(
            self,
            textvariable=self.z_tipoDatos,
            width=28
        )

        # prevent typing a value
        self.z_tipoDatos_cb['state'] = 'readonly'

        # place the widget
        self.z_tipoDatos_cb.place(
            x=758.0,
            y=265.0 - 90.0,
            width=170.0,
            height=20.0
        )
        self.z_tipoDatos_cb.current()

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
            y=455.0,
            width=170.0,
            height=20.0
        )

        self.treeFrame = Frame(
            self,
            width=235.0,
            height=440.0
        )
        # self.treeFrame.pack(fill=BOTH, expand=1)
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
        self.t.bind('<ButtonRelease-1>', self.selectItem)

        self.loadDataItems()

    def loadDataItems(self):
        columns = self.controller.getColumnsFile()
        self.xData_cb['values'] = list(columns)
        self.xData_cb.current(0)
        self.yData_cb['values'] = list(columns)
        self.yData_cb.current(1)
        self.zData_cb['values'] = list(columns)
        self.zData_cb.current(5)
        self.z_tipoDatos_cb['values'] = [
            "Enteiros", "Flotantes", "Booleans", "String"]
        self.z_tipoDatos_cb.current(0)
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

    def getDataCollected(self):
        info = {}
        info['name'] = self.entry_3.get()
        info['xRow'] = self.xData.get()
        info['yRow'] = self.yData.get()
        info['zRow'] = self.zData.get()
        if self.entry_3.get():
            self.classParent.changeName(self.entry_3.get())
        else:
            info['name'] = 'Heatmap: ' + self.zData.get()

        # get Info selected items
        # self.getInfoTreeview()
        return info

    '''
    *******************************************************************************
    ************** Funcións de proba para conseguir info do treeview **************
    *******************************************************************************
    '''

    def getInfoTreeview(self):
        self.info = self.t.get_children()
        self.list = ''
        for i in self.info:
            self.info2 = self.t.set(i)
            for a in self.info2:
                print(a, ":", self.info2[a])
                self.list = self.list + a + ": " + self.info2[a]+'\n'

        self.msg = "{} \n" .format(self.list)
        print("Message:", self.msg)

    def selectItem(self, e):
        curItem = self.t.focus()
        item = self.t.item(curItem)
        if item['text'] == 'Todos':
            parent = self.t.parent(self.t.selection()[0])
            if item['tags'][0] == 'checked':
                self.t.check_descendant(parent)
            elif item['tags'][0] == 'unchecked':
                self.t.uncheck_descendant(parent)
            # print(self.t.item(curItem), parent)
