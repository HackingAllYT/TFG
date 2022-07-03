from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, BOTH, Button, PhotoImage, filedialog, ttk, Toplevel, Frame, Radiobutton, StringVar

import tkinter as tk
import configparser

from text import TEXT


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


config = configparser.ConfigParser()
config.read('config.ini')


class gardarImaxeModal(tk.Toplevel):
    def __init__(self, parent, graphType):
        super().__init__(parent)

        self.parent = parent
        self.graphType = graphType
        self.title("Gardar imaxe como")
        self.geometry("557x575")
        self.resizable(False, False)

        self.idioma = config['INITIAL']['IDIOMA']
        self.color = config['INITIAL']['COLOR']

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=575,
            width=557,
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
            fill=TEXT[config['INITIAL']['COLOR-BG']],
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("cross.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.cancel,
            relief="flat"
        )
        self.button_1.place(
            x=489.0,
            y=11.0,
            width=58.0,
            height=58.0
        )

        self.canvas.create_text(
            106.0,
            28.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Seleccione tipo de arquivo de saída"],
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("ok_button.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.okey,
            relief="flat"
        )
        self.button_2.place(
            x=65.0,
            y=465.0,
            width=180.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("cancelar_button.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.cancel,
            relief="flat"
        )
        self.button_3.place(
            x=313.0,
            y=465.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_rectangle(
            95.0,
            139.0,
            463.0,
            214.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            106.0,
            147.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']]["Escolla o formato:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_rectangle(
            95.0,
            260.0,
            463.0,
            335.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            106.0,
            268.0,
            anchor="nw",
            text=TEXT[config['INITIAL']['IDIOMA']
                      ]["Escolla a carpeta destino:"],
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("folder.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.selectDirectory,
            relief="flat"
        )
        self.button_4.place(
            x=407.0,
            y=287.0,
            width=24.0,
            height=22.0
        )

        self.fileFormat = StringVar()
        self.fileFormat_cb = ttk.Combobox(
            self,
            textvariable=self.fileFormat,
            width=28
        )

        self.fileFormat_cb['values'] = [
            'png', 'jpg', 'jpeg', 'webp', 'svg', 'pdf'
        ]

        # prevent typing a value
        self.fileFormat_cb['state'] = 'readonly'

        # place the widget
        self.fileFormat_cb.place(
            x=106.0,
            y=182.5,
            width=300.0,
            height=25.0
        )
        self.fileFormat_cb.current(0)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_witdhXheight.png"))
        self.entry_bg_1 = self.canvas.create_image(
            155.0,
            408.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=95.0,
            y=388.0,
            width=120.0,
            height=38.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_folder.png"))
        self.entry_bg_2 = self.canvas.create_image(
            229.0,
            310.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=106.0,
            y=294.0,
            width=246.0,
            height=30.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_witdhXheight.png"))
        self.entry_bg_3 = self.canvas.create_image(
            403.0,
            408.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=343.0,
            y=388.0,
            width=120.0,
            height=38.0
        )

        self.canvas.create_text(
            105.0,
            364.0,
            anchor="nw",
            text="Ancho:",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            357.0,
            365.0,
            anchor="nw",
            text="Alto:",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.format = 'png'
        self.dir = '/'
        self.result = {}
        self.result['do'] = False
        self.isAskDirectory = False

    def select(self):
        selection = self.listbox.curselection()
        if selection:
            self.selection = self.listbox.get(selection[0])
        self.destroy()

    def show(self):
        self.deiconify()
        self.transient(self.parent)
        self.wm_protocol("WM_DELETE_WINDOW", self.destroyPop)
        self.center()
        self.wait_window(self)
        self.result['dir'] = self.dir
        self.result['format'] = self.format
        self.result['type'] = self.graphType

        try:
            self.result['w'] = float(self.entry_1.get())
        except:
            self.result['w'] = config['FIGURE-DEFAULT']['width']
        try:
            self.result['h'] = float(self.entry_3.get())
        except:
            self.result['h'] = config['FIGURE-DEFAULT']['height']
        return self.result

    def destroyPop(self, event=None):
        if not self.isAskDirectory:
            self.destroy()

    def okey(self, event=None):
        self.format = self.fileFormat.get()
        self.result['do'] = True
        self.destroy()

    def cancel(self, event=None):
        self.destroy()

    def selectDirectory(self):
        self.isAskDirectory = True
        self.dir = filedialog.askdirectory()
        self.entry_2.delete(0, tk.END)
        self.entry_2.insert(0, self.dir)
        self.isAskDirectory = False

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

    def button_1_enter(self, e):
        aux = PhotoImage(
            file=relative_to_assets("cross_62x62.png")
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

    def button_2_enter(self, e):
        ""

    def button_2_leave(self, e):
        ""

    def button_3_enter(self, e):
        ""

    def button_3_leave(self, e):
        ""
