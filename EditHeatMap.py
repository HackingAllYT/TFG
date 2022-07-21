import tkinter as tk

from tkinter import Canvas, Button, DoubleVar, PhotoImage, Entry, StringVar, IntVar, ttk, Checkbutton, Frame
from pathlib import Path
from text import TEXT, TREETYPE_TIDs_PIDs, TIPODATOS
from checkBoxTreeview import CheckboxTreeview

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class HeatMapPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.classParent = classParent
        self.config = self.controller.getConfig()

        self.auxRoute = self.config["INITIAL"]['RESOLU'] + '/' + self.config['INITIAL']['COLOR'] + \
            '/' + self.config['INITIAL']['idioma'] + '/'

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
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Nome da gráfica:"],  # "X:",
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
            text="X:",  # Antes era Y:
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
            # TEXT[self.config['INITIAL']['IDIOMA']]["Nome da gráfica:"]
            text='Y:',
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        self.canvas.create_text(
            758.0,
            141.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Tipo dato Z:"],
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
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Cores:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        aux = self.auxRoute + 'xerar.png'
        self.button_image_1 = PhotoImage(
            file=relative_to_assets(aux))
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

        self.minOutlier_entry = DoubleVar()

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

        self.maxOutlier_entry = DoubleVar()

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
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Eliminar Outliers:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        '''self.canvas.create_text(
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
        )'''

        self.canvas.create_text(
            54.0,
            110.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Seleccione PIDs e TIDs a empregar:"],
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        aux = self.auxRoute + 'gardar_saida.png'
        self.button_image_2 = PhotoImage(
            file=relative_to_assets(aux))
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

        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=57.0,
            y=57.0,
            width=211.0,
            height=27.0
        )
        ''' # Antes era
            x=411.0,
            y=168.0,
            width=211.0,
            height=27.0
        '''

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
            x=411.0,
            y=57.0,
            width=170.0,
            height=20.0
        )
        ''' # Antes era:
            x=57.0,
            y=57.0,
            width=170.0,
            height=20.0
        '''

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
            y=168.0,
            width=170.0,
            height=20.0
        )
        ''' # Antes era
            x=411.0,
            y=57.0,
            width=170.0,
            height=20.0
        '''

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
            y=57.0,
            width=170.0,
            height=20.0
        )
        self.zData_cb.bind('<<ComboboxSelected>>', self.zDataCallback)

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
            y=175.0,
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
            x=758.0,
            y=284.0,
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

        self.t = CheckboxTreeview(
            master=self.treeFrame, treeType=TREETYPE_TIDs_PIDs, show="tree", editClass=self)
        self.t.place(
            x=0.0,
            y=0.0,
            width=335.0,  # 235
            height=440.0
        )

        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)
        self.loadDataItems()

    def loadDataItems(self):
        columns = self.controller.getColumnsFile()
        self.xData_cb['values'] = list(columns)
        self.xData_cb.current(0)
        self.yData_cb['values'] = list(columns)
        self.yData_cb.current(1)
        self.zData_cb['values'] = list(columns)
        self.zData_cb.current(5)
        aux = TIPODATOS[self.config['INITIAL']['IDIOMA']].copy()
        aux.pop(0)
        self.z_tipoDatos_cb['values'] = aux
        self.z_tipoDatos_cb.current(0)
        info = self.controller.getPidsTids()
        self.t.insertElements(info, TREETYPE_TIDs_PIDs)

        self.colors_cb['values'] = self.controller.getColors()
        self.colors_cb.current(self.controller.getColors().index('default'))

        self.entry_1.config(
            state=tk.DISABLED, disabledbackground="#F1F5FF")
        self.entry_2.config(
            state=tk.DISABLED, disabledbackground="#F1F5FF")
        self.entry_3.delete(0, tk.END)
        self.entry_3.insert(0, 'Heatmap: ' + self.zData.get())

        self.zDataCallback(None)

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
        info['colors'] = self.colors.get()
        info['zMin'] = self.minOutlier_entry.get()
        info['zMax'] = self.maxOutlier_entry.get()
        info['zType'] = TIPODATOS[self.config['INITIAL']['IDIOMA']].index(
            self.z_tipoDatos.get())
        info['delOut'] = bool(self.deleteOutliers.get())

        if self.entry_3.get():
            self.classParent.changeName(self.entry_3.get())
        else:
            info['name'] = 'Heatmap: ' + self.zData.get()

        # get Info selected items
        info['PIDsTIDs'] = self.t.getSelectedItemsPIDsTIDs()

        return info

    def zDataCallback(self, e):
        aux = self.controller.getCalcularOutliers(
            self.zData.get(), self.t.getSelectedItemsPIDsTIDs())
        self.minOutlier_entry.set(aux[0])
        self.maxOutlier_entry.set(aux[1])

    '''
    *******************************************************************************
    ****************** Funcións para xogar cos efectos das fotos ******************
    *******************************************************************************
    '''

    def button_1_enter(self, e):
        route = self.auxRoute + 'xerar_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

    def button_2_enter(self, e):
        route = self.auxRoute + 'gardar_saida_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        self.button_2["image"] = self.button_image_2
