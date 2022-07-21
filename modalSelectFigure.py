from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Button, PhotoImage, Frame

import tkinter as tk

from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class selectFigureModal(tk.Toplevel):
    def __init__(self, parent, suggestions):
        super().__init__(parent)

        self.parent = parent
        self.title("Selección de figura a xerar")
        self.geometry("700x900")
        self.resizable(False, False)
        self.config = self.parent.getConfig()

        self.frame = Frame(self, width=700, height=900)

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=900,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            80.0,
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_heatmap.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.addHeatmap,
            relief="flat"
        )
        self.button_2.place(
            x=20.0,
            y=123.0,
            width=312.0,
            height=248.0
        )
        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_scatter.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.addScatter,
            relief="flat"
        )
        self.button_3.place(
            x=368.0,
            y=123.0,
            width=312.0,
            height=248.0
        )
        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("roofline_model.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.addRoofline,
            relief="flat"
        )
        self.button_4.place(
            x=20.0,
            y=394.0,
            width=312.0,
            height=248.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_scatter_temporal.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.addRooflineTemporal,
            relief="flat"
        )
        self.button_5.place(
            x=368.0,
            y=394.0,
            width=312.0,
            height=248.0
        )

        self.canvas.create_text(
            220.0,
            28.0,
            anchor="nw",
            text=TEXT[self.config['INITIAL']['IDIOMA']
                      ]["Seleccione tipo de gráfica:"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.selection = None

    def select(self):
        selection = self.listbox.curselection()
        if selection:
            self.selection = self.listbox.get(selection[0])
        self.destroy()

    def show(self):
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.center()
        self.wait_window(self)
        return self.selection

    def destroyPop(self, event=None):
        self.destroy()

    def center(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

    '''
    *******************************************************************************
    ******************** Funcións para engadir novas gráficas *********************
    *******************************************************************************
    '''

    def addHeatmap(self, evente=None):
        self.selection = "heatmap"
        self.destroy()

    def addScatter(self, evente=None):
        self.selection = "scatter"
        self.destroy()

    def addRoofline(self, event=None):
        self.selection = "roofline"
        self.destroy()

    def addRooflineTemporal(self, event=None):
        self.selection = "roofline-temporal"
        self.destroy()

    '''
    *******************************************************************************
    ******************* Funcións para facer efectos nos botóns  *******************
    *******************************************************************************
    '''

    def button_2_enter(self, e):
        ""

    def button_2_leave(self, e):
        ""

    def button_3_enter(self, e):
        ""

    def button_3_leave(self, e):
        ""
