import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry, Frame, IntVar, Checkbutton

from src.config.text import TEXT, TREETYPE_TIDs_PIDs, TREETYPE_CPUs, RESOLU
from src.Elements.checkBoxTreeview import CheckboxTreeview
from src.Elements.addTraceRoofline import TraceRooflineContainer, TraceRoofline, ScrollableFrame
from src.Elements.scrollbarFrame import ScrolledFrame


class RooflineModelPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent, background='#FFFFFF')

        self.controller = controller
        self.classParent = classParent
        self.config = self.controller.getConfig()

        self.auxRoute = self.config["INITIAL"]['RESOLU'] + '/' + self.config['INITIAL']['COLOR'] + \
            '/' + self.config['INITIAL']['idioma'] + '/'

        self.relative_to_assets = self.controller.relative_to_assets

        if self.config["INITIAL"]['RESOLU'] == RESOLU['1']:
            self.__init_HD__(controller)

    def __init_HD__(self, controller):
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
            60.0,
            23.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Nome da gráfica:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        aux = self.auxRoute + 'xerar.png'
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.xerarNovoRooflineModel(
                self.getDataCollected()),
            relief="flat"
        )
        self.button_1.place(
            x=602.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        aux = self.auxRoute + 'gardar_saida.png'
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets(aux))
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
            x=807.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=60.0,
            y=55.0,
            width=202.0,
            height=29.0
        )

        self.canvas.create_rectangle(
            36.0,
            132.0,
            286.0,
            582.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            54.0,
            110.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Seleccione PIDs e TIDs a empregar:"],
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            319.0,
            131.0,
            569.0,
            581.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            337.0,
            109.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Seleccione os CPUs a empregar:"],
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            602.0,
            132.0,
            987.0,
            494.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            620.0,
            110.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Engadir liñas:"],
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            337.0,
            27.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Eixe X logarítmico:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            337.0,
            68.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']]["Eixe Y logarítmico:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.eixoX = IntVar()

        self.eixoX_CB = Checkbutton(
            self,
            text='',
            variable=self.eixoX,
            onvalue=1,
            offvalue=0,
            background='#FFFFFF',
            image=self.classParent.getUnCheckedImage(),
            selectimage=self.classParent.getCheckedImage(),
            indicatoron=False,
            highlightthickness=0,
            borderwidth=0
        )

        self.eixoX_CB.place(
            x=534.0,
            y=27.0,
            width=20.0,
            height=20.0
        )

        self.eixoY = IntVar()

        self.eixoY_CB = Checkbutton(
            self,
            text='',
            variable=self.eixoY,
            onvalue=1,
            offvalue=0,
            background='#FFFFFF',
            image=self.classParent.getUnCheckedImage(),
            selectimage=self.classParent.getCheckedImage(),
            indicatoron=False,
            highlightthickness=0,
            borderwidth=0
        )

        self.eixoY_CB.place(
            x=534.0,
            y=68.0,
            width=20.0,
            height=20.0
        )

        self.treeFramePidTid = Frame(
            self,
            width=235.0,
            height=440.0
        )

        self.treeFramePidTid.place(
            x=42.0,
            y=140.0,
            width=235.0,
            height=440.0
        )

        self.tPidTid = CheckboxTreeview(
            master=self.treeFramePidTid, treeType=TREETYPE_TIDs_PIDs, show="tree", controller=self.controller)
        self.tPidTid.place(
            x=0.0,
            y=0.0,
            width=235.0,
            height=440.0
        )

        self.treeFrameCpu = Frame(
            self,
            width=235.0,
            height=440.0
        )

        self.treeFrameCpu.place(
            x=325.0,
            y=140.0,
            width=235.0,
            height=440.0
        )

        self.tCpu = CheckboxTreeview(
            master=self.treeFrameCpu, treeType=TREETYPE_CPUs, show="tree", controller=self.controller)
        self.tCpu.place(
            x=0.0,
            y=0.0,
            width=235.0,
            height=440.0
        )

        '''self.linhasFrame = ScrolledFrame(
            parent=self, controller=self.controller, classParent=self.classParent
        )'''
        '''self.linhasFrame = ScrolledFrame(
            master=self
        )'''
        self.linhasFrame = ScrollableFrame(
            parent=self, controller=self.controller, classParent=self.classParent
        )
        self.linhasFrame.place(
            x=604.5,
            y=133.0,
            width=380,
            height=358
        )

        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)
        self.loadDataItems()

    def loadDataItems(self):
        self.entry_1.delete(0, tk.END)
        self.entry_1.insert(0, 'Roofline Model')
        infoTIDs = self.controller.getPidsTids()
        infoCpus = self.controller.getCPUs()
        self.tPidTid.insertElements(infoTIDs, TREETYPE_TIDs_PIDs)
        self.tCpu.insertElements(infoCpus, TREETYPE_CPUs)

        ''' aux = TraceRoofline(
            self.linhasFrame.interior, self.controller, self.classParent).grid(row=0, column=0)
        aux = TraceRoofline(
            self.linhasFrame.interior, self.controller, self.classParent).grid(row=1, column=0)
        aux = TraceRoofline(
            self.linhasFrame.interior, self.controller, self.classParent).grid(row=2, column=0)
        aux = TraceRoofline(
            self.linhasFrame.interior, self.controller, self.classParent).grid(row=3, column=0)
        for i in range(20):
            tk.ttk.Label(self.linhasFrame.interior, text='Label %i' % i).pack()'''

        for i in range(50):
            tk.ttk.Label(self.linhasFrame.canvas,
                         text="Sample scrolling label").pack()
        '''aux = TraceRoofline(
            self.linhasFrame.canvas, self.controller, self.classParent).pack()'''

        self.linhasFrame.addFrame()

        # self.linhasFrame.addFrame(aux)

    def getDataCollected(self):
        info = {}
        info['name'] = self.entry_1.get()
        info['logX'] = bool(self.eixoX.get())
        info['logY'] = bool(self.eixoY.get())

        if self.entry_1.get():
            self.classParent.changeName(self.entry_1.get())

        info['PIDsTIDs'] = self.tPidTid.getSelectedItemsPIDsTIDs()
        info['CPUs'] = self.tCpu.getSelectedItemsCPUs()
        return info

    '''
    *******************************************************************************
    ****************** Funcións para xogar cos efectos das fotos ******************
    *******************************************************************************
    '''

    def button_1_enter(self, e):
        route = self.auxRoute + 'xerar_over.png'
        aux = PhotoImage(
            file=self.relative_to_assets(route)
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

    def button_2_enter(self, e):
        route = self.auxRoute + 'gardar_saida_over.png'
        aux = PhotoImage(
            file=self.relative_to_assets(route)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        self.button_2["image"] = self.button_image_2
