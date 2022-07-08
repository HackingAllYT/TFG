import tkinter as tk

from tkinter import BOTTOM, Canvas, Button, PhotoImage, Entry, Frame, ttk, NONE, END, X
from pathlib import Path
import configparser
from text import TEXT, TREETYPE_TIDs_PIDs, TREETYPE_CPUs
from checkBoxTreeview import CheckboxTreeview

import platform

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class TraceRooflineContainer(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent, background='#FFFFFF')

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=100,
            width=380,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.scroll_y = tk.Scrollbar(
            parent, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set)

        '''self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        self.vsb.pack(side='right', fill='y')
        self.configure(yscrollcommand=self.vsb.set)'''

        self.controller = controller
        self.classParent = classParent

        self.frames = []

        self.canvas.update_idletasks()

        # self.insertFrame(None)

    def insertFrame(self, newFrame: Frame):
        t = tk.Text(self, width=15, height=15, wrap=NONE,
                    xscrollcommand=self.vsb.set,
                    yscrollcommand=self.vsb.set)
        t.insert(END, "this is some text\n")

        # attach Text widget to root window at top
        t.pack(side=BOTTOM, fill=X)
        self.frames.append(newFrame)


class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, controller, classParent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller
        self.classParent = classParent

        # place canvas on self
        self.canvas = tk.Canvas(
            self,
            borderwidth=0,
            background="#ffffff",
            width=370.0,
            height=100.0
        )

        # Create A Main Frame
        # main_frame = Frame(root)
        # main_frame.pack(fill=BOTH, expand=1)
        self.pack(fill=tk.BOTH, expand=1)

        # Create A Canvas
        # my_canvas = Canvas(main_frame)
        # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        # my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        # my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure The Canvas
        # my_canvas.configure(yscrollcommand=my_scrollbar.set)
        # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        self.canvas.configure(yscrollcommand=my_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        # second_frame = Frame(canvas)
        self.second_frame = Frame(self.canvas)

        # Add that New frame To a Window In The Canvas
        # my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        self.canvas.create_window(
            (0, 0), window=self.second_frame, anchor="nw")

        self.frames = []

        self.addFrame()

    def addFrame(self):
        aux = TraceRoofline(self.second_frame,
                            self.controller, self.classParent)
        self.frames.append(aux)


class TraceRoofline(tk.Frame):

    def __init__(self, parent, controller, classParent):
        tk.Frame.__init__(self, parent, background='#FFFFFF')

        self.controller = controller
        self.classParent = classParent
        self.parent = parent

        self.canvas = Canvas(
            self.parent,
            bg="#FFFFFF",
            height=100,
            width=370,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            10.0,
            10.0,
            135.0,
            45.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            13.0,
            20.0,
            anchor="nw",
            text="GFLOPs:",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            154.0,
            10.0,
            314.0,
            45.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            157.0,
            20.0,
            anchor="nw",
            text="Nome:",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            10.0,
            55.0,
            135.0,
            90.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            13.0,
            65.0,
            anchor="nw",
            text="IOPs:",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            154.0,
            55.0,
            314.0,
            90.0,
            fill="#F1F5FF",
            outline="")

        self.canvas.create_text(
            157.0,
            65.0,
            anchor="nw",
            text="Cor:",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("add.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=322.0,
            y=25.0,
            width=50.0,
            height=50.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_roofline_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            101.5,
            27.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=73.0,
            y=20.0,
            width=57.0,
            height=13.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_roofline_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            255.5,
            27.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=205.0,
            y=20.0,
            width=101.0,
            height=13.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_roofline_1.png"))
        self.entry_bg_3 = self.canvas.create_image(
            101.5,
            72.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=73.0,
            y=65.0,
            width=57.0,
            height=13.0
        )

        self.canvas.create_rectangle(
            -1.0,
            99.0,
            380.0,
            100.0,
            fill="#000000",
            outline="")


class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollableFrame(self)  # add a new scrollable frame.

        # Now add some controls to the scrollframe.
        # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
        for row in range(100):
            a = row
            tk.Label(self.scrollFrame.viewPort, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t = "this is the second column for row %s" % row
            tk.Button(self.scrollFrame.viewPort, text=t, command=lambda x=a: self.printMsg(
                "Hello " + str(x))).grid(row=row, column=1)
            TraceRoofline(self.scrollFrame.viewPort, self,
                          self).grid(row=row, column=2)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.place(
            x=0.0,
            y=0.0,
            width=1000.0,
            height=1000.0
        )

    def printMsg(self, msg):
        print(msg)


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).place(
        x=0.0,
        y=0.0,
        width=1000.0,
        height=1000.0
    )
    root.mainloop()

'''
if __name__ == '__main__':
    root = tk.Tk()

    frame = ScrollableFrame(root)

    for i in range(50):
        ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

    frame.pack()
    root.mainloop()
'''
