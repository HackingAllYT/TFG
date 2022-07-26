import tkinter as tk

from tkinter import ttk, Button, Canvas, PhotoImage
from pathlib import Path

from StartPage import StartPage
from text import TEXT, RESOLU


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, background='#FFFFFF')
        self.controller = controller
        self.config = self.controller.getConfig()

        self.__initialize_custom_style()
        kwargs["style"] = "CustomNotebook"

        self.auxRoute = self.config["INITIAL"]['RESOLU'] + '/' + self.config['INITIAL']['COLOR'] + \
            '/' + self.config['INITIAL']['idioma'] + '/'

        self.controller = controller
        self.pageTwoFrames = []
        self.im_checked = tk.PhotoImage(
            file=relative_to_assets('checked_18x18.png'))
        self.im_unchecked = tk.PhotoImage(
            file=relative_to_assets('unchecked_18x18.png'))

        if self.config["INITIAL"]['RESOLU'] == RESOLU['1']:
            self.__init_HD__(controller, args, kwargs)

    def __init_HD__(self, controller, *args, **kwargs):
        self.notebook = ttk.Notebook(self, *args, **kwargs)
        self.notebook.place(
            x=0.0,
            y=60.0,
            width=1024.0,
            height=660.0
        )

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=55,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            55.0,
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        aux = self.auxRoute + 'sair.png'
        self.button_image_1 = PhotoImage(
            file=relative_to_assets(aux))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=controller.confirmExit,
            relief="flat"
        )
        self.button_1.place(
            x=637.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'configuracion.png'
        self.button_image_2 = PhotoImage(
            file=relative_to_assets(aux))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openConfigurationModal,
            relief="flat"
        )
        self.button_2.place(
            x=70.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'nova_grafica.png'
        self.button_image_3 = PhotoImage(
            file=relative_to_assets(aux))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.openSelectFigureModal,
            relief="flat"
        )
        self.button_3.place(
            x=448.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'cargar_arquivo.png'
        self.button_image_4 = PhotoImage(
            file=relative_to_assets(aux))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.selectNewFile,
            relief="flat"
        )
        self.button_4.place(
            x=259.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'home_over.png'
        self.button_image_6 = PhotoImage(
            file=relative_to_assets(aux))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_home,
            relief="flat"
        )
        self.button_6.place(
            x=2.0,
            y=1.0,
            width=51.0,
            height=51.0
        )

        self.notebook.bind("<ButtonPress-1>", self.on_close_press, True)
        self.notebook.bind("<ButtonRelease-1>", self.on_close_release)

        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_4.bind('<Enter>', self.button_4_enter)
        self.button_4.bind('<Leave>', self.button_4_leave)

        self.button_6.bind('<Enter>', self.button_6_enter)
        self.button_6.bind('<Leave>', self.button_6_leave)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.notebook.identify(event.x, event.y)

        if "close" in element:
            index = self.notebook.index("@%d,%d" % (event.x, event.y))
            self.notebook.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.notebook.instate(['pressed']):
            return

        element = self.notebook.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index = self.notebook.index("@%d,%d" % (event.x, event.y))

        if self._active == index:
            self.notebook.forget(index)
            self.notebook.event_generate("<<NotebookTabClosed>>")

        self.notebook.state(["!pressed"])
        self._active = None

        if not self.notebook.select():
            self.controller.show_frame(StartPage)

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [
                     ("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {
                                     "side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {
                                     "side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])

        style.configure("CustomNotebook",
                        highlightbackground="#848a98", background='#FFFFFF')

    def addFrame(self, frameType, name: str):
        self.aux = frameType(self.notebook, self.controller, self)
        self.pageTwoFrames.append(self.aux)
        self.notebook.add(self.aux, text=name, padding=5)
        self.notebook.place(
            x=0.0,
            y=60.0,
            width=1024.0,
            height=699.0
        )
        self.notebook.select(self.aux)

    def selectNewFile(self):
        self.controller.select_path_2()

    '''
    *******************************************************************************
    ****************** Funcións para obter información (getters) ******************
    *******************************************************************************
    '''

    def getCheckedImage(self):
        return self.im_checked

    def getUnCheckedImage(self):
        return self.im_unchecked

    '''
    *******************************************************************************
    ****************** Funcións para xogar cos efectos das fotos ******************
    *******************************************************************************
    '''

    def button_1_enter(self, e):
        route = self.auxRoute + 'sair_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

    def button_2_enter(self, e):
        route = self.auxRoute + 'configuracion_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        self.button_2["image"] = self.button_image_2

    def button_3_enter(self, e):
        route = self.auxRoute + 'nova_grafica_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_3["image"] = aux
        self.button_3.image = aux

    def button_3_leave(self, e):
        self.button_3["image"] = self.button_image_3

    def button_4_enter(self, e):
        route = self.auxRoute + 'cargar_arquivo_over.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_4["image"] = aux
        self.button_4.image = aux

    def button_4_leave(self, e):
        self.button_4["image"] = self.button_image_4

    def button_6_enter(self, e):
        route = self.auxRoute + 'home.png'
        aux = PhotoImage(
            file=relative_to_assets(route)
        )
        self.button_6["image"] = aux
        self.button_6.image = aux

    def button_6_leave(self, e):
        self.button_6["image"] = self.button_image_6

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame Two ************************
    *******************************************************************************
    '''

    def go_home(self):
        self.controller.show_frame(StartPage)

    def changeName(self, name):
        self.notebook.tab("current", text=name)
