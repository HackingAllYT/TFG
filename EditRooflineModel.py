import tkinter as tk

from tkinter import Canvas, Button, PhotoImage, Entry, Frame, IntVar, Checkbutton
from pathlib import Path
import configparser
from text import TEXT, TREETYPE_TIDs_PIDs, TREETYPE_CPUs
from checkBoxTreeview import CheckboxTreeview
from addTraceRoofline import TraceRooflineContainer, TraceRoofline, ScrollableFrame
from scrollbarFrame import ScrolledFrame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class RooflineModelPane(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent, background='#FFFFFF')

        self.controller = controller
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
            60.0,
            23.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Nome da gráfica:"],
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
            x=807.0,
            y=527.0,
            width=180.0,
            height=55.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_1 = self.canvas.create_image(
            165.5,
            69.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=60.0,
            y=55.0,
            width=211.0,
            height=27.0
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
            text=TEXT[config['INITIAL']['IDIOMA']
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
            text=TEXT[config['INITIAL']['IDIOMA']
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
            text="Engadir liñas:",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            337.0,
            27.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eixe X logarítmico:"],
            fill="#000000",
            font=("Inter", 15 * -1)
        )

        self.canvas.create_text(
            337.0,
            68.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Eixe Y logarítmico:"],
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
            master=self.treeFramePidTid, treeType=TREETYPE_TIDs_PIDs, show="tree")
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
            master=self.treeFrameCpu, treeType=TREETYPE_CPUs, show="tree")
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
