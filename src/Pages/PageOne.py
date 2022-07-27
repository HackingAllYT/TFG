import tkinter as tk

from tkinter import Canvas, Button, PhotoImage

from src.config.text import TEXT, RESOLU


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config = self.controller.getConfig()

        self.relative_to_assets = self.controller.relative_to_assets

        self.auxRoute = self.config["INITIAL"]['RESOLU'] + '/' + self.config['INITIAL']['COLOR'] + \
            '/' + self.config['INITIAL']['idioma'] + '/'

        if self.config["INITIAL"]['RESOLU'] == RESOLU['1']:
            self.__init_HD__(controller)
        elif self.config["INITIAL"]['RESOLU'] == RESOLU['2']:
            self.__init_FullHD__(controller)

        self.button_1.bind('<Enter>', self.button_1_enter)
        self.button_1.bind('<Leave>', self.button_1_leave)

        self.button_2.bind('<Enter>', self.button_2_enter)
        self.button_2.bind('<Leave>', self.button_2_leave)

        self.button_3.bind('<Enter>', self.button_3_enter)
        self.button_3.bind('<Leave>', self.button_3_leave)

    def __init_HD__(self, controller):
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.saida_image_1 = PhotoImage(
            file=self.relative_to_assets("saida.png"))
        self.saida = self.canvas.create_image(
            512.0,
            410.0,
            image=self.saida_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            55.0,
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        aux = self.auxRoute + 'configuracion.png'
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openConfigurationModal,
            relief="flat"
        )
        self.button_1.place(
            x=70.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'seleccionar_grafica.png'
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openSelectFigureModal,
            relief="flat"
        )
        self.button_2.place(
            x=267.0,
            y=1.0,
            width=180.0,
            height=53.0
        )

        aux = self.auxRoute + 'home_over.png'
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=controller.mostrarHomedendeImaxe,
            relief="flat"
        )
        self.button_3.place(
            x=2.0,
            y=2.0,
            width=51.0,
            height=51.0
        )

    def __init_FullHD__(self, controller):

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1000,
            width=1900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("saida.png"))
        self.image_1 = self.canvas.create_image(
            950.0,
            585.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            100.0,
            fill=TEXT[self.config['INITIAL']['COLOR-BG']],
            outline="")

        aux = self.auxRoute + 'configuracion.png'
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openConfigurationModal,
            relief="flat"
        )
        self.button_1.place(
            x=96.0,
            y=9.0,
            width=288.2099914550781,
            height=82.5
        )

        aux = self.auxRoute + 'seleccionar_grafica.png'
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=controller.openSelectFigureModal,
            relief="flat"
        )
        self.button_2.place(
            x=403.0,
            y=9.0,
            width=288.2099609375,
            height=82.5
        )

        aux = self.auxRoute + 'home_over.png'
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets(aux))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=controller.mostrarHomedendeImaxe,
            relief="flat"
        )
        self.button_3.place(
            x=7.0,
            y=15.0,
            width=70.0,
            height=70.0
        )

    '''
    *******************************************************************************
    ****************** Función para actualizar o resumo da foto *******************
    *******************************************************************************
    '''

    def setNamePicture(self, name: str):
        if self.config["INITIAL"]['RESOLU'] == RESOLU['1']:
            self.canvas.create_text(
                259.0,
                80.0,
                anchor="nw",
                text=TEXT[self.config['INITIAL']['IDIOMA']]["Nome do gráfico:"] +
                '"' + name + '"' + '. Timestamp: x; TID: y; CPU: z',
                fill="#000000",
                font=("Inter Bold", 15 * -1)
            )
        elif self.config["INITIAL"]['RESOLU'] == RESOLU['2']:
            self.canvas.create_text(
                262.0,
                125.0,
                anchor="nw",
                text=TEXT[self.config['INITIAL']['IDIOMA']]["Nome do gráfico:"] +
                '"' + name + '"' + '. Timestamp: x; TID: y; CPU: z',
                fill="#000000",
                font=("Inter Bold", 15 * -1)
            )

    '''
    *******************************************************************************
    ****************** Funcións para xogar cos efectos das fotos ******************
    *******************************************************************************
    '''

    def button_1_enter(self, e):
        name = self.auxRoute + 'configuracion_over.png'
        aux = PhotoImage(
            file=self.relative_to_assets(name)
        )
        self.button_1["image"] = aux
        self.button_1.image = aux

    def button_1_leave(self, e):
        self.button_1["image"] = self.button_image_1

    def button_2_enter(self, e):
        name = self.auxRoute + 'seleccionar_grafica_over.png'
        aux = PhotoImage(
            file=self.relative_to_assets(name)
        )
        self.button_2["image"] = aux
        self.button_2.image = aux

    def button_2_leave(self, e):
        self.button_2["image"] = self.button_image_2

    def button_3_enter(self, e):
        name = self.auxRoute + 'home.png'
        aux = PhotoImage(
            file=self.relative_to_assets(name)
        )
        self.button_3["image"] = aux
        self.button_3.image = aux

    def button_3_leave(self, e):
        self.button_3["image"] = self.button_image_3
