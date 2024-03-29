
import tkinter as tk

from pathlib import Path

import configparser

import pandas as pd
from src.config.text import TEXT, RESOLU
from src.Pages.StartPage import StartPage
from src.Pages.PageOne import PageOne
from src.Pages.PageTwo import PageTwo
from threading import *
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno, askyesnocancel
from src.Plot.migplot import (
    parse_file,
    initial_chart,
    interactive_chart_plot,
    interactive_scatter,
    interactive_time_scatter,
    getColors,
    getColorsContinuos,
    getColorsLines,
    calcularOutliers
)
import src.Modals.modalConfiguration as cm
import src.Modals.modalSelectFigure as msf
import src.Modals.modalGardarImaxe as sim
from src.EditPane.EditHeatMap import HeatMapPane
from src.EditPane.EditScatterPane import ScatterPane
from src.EditPane.EditScatterPaneTemporal import ScatterPaneTemporal
from src.EditPane.EditRooflineModel import RooflineModelPane

import os
import sys


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

askExit = True


LARGE_FONT = ("Verdana", 12)


class AppController(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.config = configparser.ConfigParser()
        self.config.read('src/config/config.ini')

        self.geometry(RESOLU[self.config['INITIAL']['RESOLU']])
        self.resizable(False, False)
        self.center()
        self.iconphoto(False, tk.PhotoImage(
            file=self.relative_to_assets('icon/icon.png')))
        self.title(TEXT[self.config['INITIAL']['IDIOMA']]['title'])
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pidsTids, self.infoData = [], []

        # Variables que nos serven para coñecer a cantidade de gráficas xeradas
        self.numHeatmap = 0
        self.numScatter = 0
        self.numRoofMod = 0
        self.numRoofCol = 0
        self.numRoofM3D = 0
        self.numScattTem = 0

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        global askExit
        askExit = False

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.activateFrame = cont

    def center(self):
        """
        centers a tkinter window
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

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)
    '''
    *******************************************************************************
    ********************** Funcións propias do Frame Inicial **********************
    *******************************************************************************
    '''

    def select_path_2(self):
        global filename
        filetypes = (
            ('Comma-separated values', '*.csv'),
            ('All files', '*.*')
        )

        # Se queremos obter máis dun arquivo temos que modificar a función e
        # chamar a: fd.askopenfilenames
        filename = fd.askopenfilename(
            title=TEXT[self.config['INITIAL']
                       ['IDIOMA']]['Escolla un arquivo:'],
            initialdir=Path.home(),
            filetypes=filetypes)

        if filename:
            # print(filename, type(filename))
            self.frames[StartPage].setEntryName(filename)
            # creating a thread
            Thread_loadFile = Thread(target=self.loadFileThread)

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()

    def showPaxResumoArquivo(self):
        self.show_frame(PageOne)

    '''
    *******************************************************************************
    ******************** Funcións auxiliares do Frame Inicial *********************
    *******************************************************************************
    '''

    def auxLoadFile(self, name):
        data = parse_file(
            file=name, separator=self.config['READ-FILE']['SEPARATOR'])
        if type(data) != str and type(data) != type(None):
            self.frames[PageOne].setNamePicture(filename)
            self.pidsTids = self.loadPids(data=data)
            self.infoData.append([name, data])
            self.frames[StartPage].setButtonsEnabled()
            initial_chart(data=data)
        else:
            if data == None:
                self.showMessage(
                    TEXT[self.config['INITIAL']['IDIOMA']
                         ]['Erro procesando o arquivo'],
                    TEXT[self.config['INITIAL']['IDIOMA']]['erro-processing'], 'warning')
            elif type(data) == str:
                self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['Erro procesando o arquivo'],
                                 TEXT[self.config['INITIAL']['IDIOMA']]['erro-processing-col'] + data, 'warning')

    def loadFileThread(self):
        self.infoData = []
        showinfo(
            title=TEXT[self.config['INITIAL']
                       ['IDIOMA']]['Arquivo seleccionado:'],
            message=filename
        )
        if type(filename) == str:
            self.auxLoadFile(filename)
        else:
            for x in filename:
                self.auxLoadFile(x)

        self.update()
        self.update_idletasks()

    def setFilename(self, fileName):
        global filename
        filename = fileName
        # creating a thread
        Thread_loadFile = Thread(target=self.loadFileThread)

        # change T to daemon
        Thread_loadFile.daemon = True
        Thread_loadFile.start()

    def xerarNovaHeatMapThread(self, info, save: dict = None):
        aux = (self.infoData[0][1].columns.get_loc(info['xRow']),
               self.infoData[0][1].columns.get_loc(info['yRow']),
               info['zRow'], info['zMin'], info['zMax'], info['zType'], info['delOut'])

        result = interactive_chart_plot(
            index=aux,
            plotName=info['name'],
            data=self.infoData[0][1],
            save=save,
            infoData=info['PIDsTIDs'],
            colors=info['colors']
        )
        if result == None and save == None:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-grafica'],
                             TEXT[self.config['INITIAL']
                                  ['IDIOMA']]['erro-grafica-text'],
                             type='warning')
        elif result == None and save:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-gardar-imaxe'],
                             TEXT[self.config['INITIAL']['IDIOMA']
                                  ]['erro-gardar-imaxe-text'],
                             type='warning')
        # self.root.destroy()
        # self.root.after(0, self.root.destroy)

    def xerarNovoScatterThread(self, info, save: dict = None):
        aux = (self.infoData[0][1].columns.get_loc(info['xRow']),
               self.infoData[0][1].columns.get_loc(info['yRow']),
               info['zRow'], info['zMin'], info['zMax'], info['delOut'])

        result = interactive_scatter(
            index=aux,
            plotName=info['name'],
            data=self.infoData[0][1],
            save=save,
            lines=info['unir'],
            infoData=info['PIDsTIDs'],
            colors=info['colors']
        )
        if result == None and save == None:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-grafica'],
                             TEXT[self.config['INITIAL']
                                  ['IDIOMA']]['erro-grafica-text'],
                             type='warning')
        elif result == None and save:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-gardar-imaxe'],
                             TEXT[self.config['INITIAL']['IDIOMA']
                                  ]['erro-gardar-imaxe-text'],
                             type='warning')
        # self.root.destroy()
        # self.root.after(0, self.root.destroy)

    def xerarNovoRooflineThread(self, info, save: dict = None):
        ''
        # self.root.destroy()
        # self.root.after(0, self.root.destroy)

    def xerarNovoScatterTemporalThread(self, info, save: dict = None):
        aux = (self.infoData[0][1].columns.get_loc(info['yRow']),
               info['zRow'], info['zMin'], info['zMax'], info['delOut'], info['varGraphs'])

        result = interactive_time_scatter(
            index=aux,
            plotName=info['name'],
            data=self.infoData[0][1],
            save=save,
            infoData=info['PIDsTIDs']
        )
        if result == None and save == None:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-grafica'],
                             TEXT[self.config['INITIAL']
                                  ['IDIOMA']]['erro-grafica-text'],
                             type='warning')
        elif result == None and save:
            self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['erro-gardar-imaxe'],
                             TEXT[self.config['INITIAL']['IDIOMA']
                                  ]['erro-gardar-imaxe-text'],
                             type='warning')

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame One ************************
    *******************************************************************************
    '''

    def openConfigurationModal(self):
        conModal = cm.configurationModal(self)
        result = conModal.show()
        if result == True:
            self.update()
            self.update_idletasks()

    def openSelectFigureModal(self):
        sugges = ((0, 'Item 0'), (1, 'Item 1'))
        figModal = msf.selectFigureModal(self, suggestions=sugges)
        result = figModal.show()
        if result == 'heatmap':
            self.frames[PageTwo].addFrame(
                HeatMapPane, 'HeatMap - ' + str(self.numHeatmap))
            self.show_frame(PageTwo)
            self.numHeatmap += 1
        elif result == 'scatter':
            self.frames[PageTwo].addFrame(
                ScatterPane, 'Scatter - ' + str(self.numScatter))
            self.show_frame(PageTwo)
            self.numScatter += 1
        elif result == 'roofline':
            self.frames[PageTwo].addFrame(
                RooflineModelPane, 'Roofline - ' + str(self.numRoofMod))
            self.show_frame(PageTwo)
            self.numRoofMod += 1
        elif result == 'scatter-temporal':
            self.frames[PageTwo].addFrame(
                ScatterPaneTemporal, 'Scatter Temporal - ' + str(self.numScattTem))
            self.show_frame(PageTwo)
            self.numScattTem += 1

    def mostrarHomedendeImaxe(self):
        self.show_frame(StartPage)

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame Two ************************
    *******************************************************************************
    '''

    def confirmExit(self):
        answer = askyesno(
            title=TEXT[self.config['INITIAL']['IDIOMA']]['Saír?'],
            message=TEXT[self.config['INITIAL']['IDIOMA']
                         ]['Está seguro que quere pechar?']
        )
        if answer:
            self.destroy()

    '''
    *******************************************************************************
    **************** Funcións para xerar as gráficas do Frame Two *****************
    *******************************************************************************
    '''

    def xerarNovoHeatmap(self, info):
        if not info['PIDsTIDs']:
            self.showMessage(
                TEXT[self.config['INITIAL']['IDIOMA']]['Seleccione datos'],
                TEXT[self.config['INITIAL']['IDIOMA']]['erro-sin-seleccion'], 'warning')
        else:
            # creating a thread
            Thread_loadFile = Thread(
                target=lambda: self.xerarNovaHeatMapThread(info))

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()

            self.showNewGraphic()

    def xerarNovoScatter(self, info):
        if not info['PIDsTIDs']:
            self.showMessage(
                TEXT[self.config['INITIAL']['IDIOMA']]['Seleccione datos'],
                TEXT[self.config['INITIAL']['IDIOMA']]['erro-sin-seleccion'], 'warning')
        else:
            # creating a thread
            Thread_loadFile = Thread(
                target=lambda: self.xerarNovoScatterThread(info))

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()

            self.showNewGraphic()

    def xerarNovoRooflineModel(self, info):
        if not info['PIDsTIDs']:
            self.showMessage(
                TEXT[self.config['INITIAL']['IDIOMA']]['Seleccione datos'],
                TEXT[self.config['INITIAL']['IDIOMA']]['erro-sin-seleccion'], 'warning')
        else:
            # creating a thread
            Thread_loadFile = Thread(
                target=lambda: self.xerarNovoRooflineThread(info))

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()

            self.showNewGraphic()

    def xerarNovoScatterTemporal(self, info):
        if not info['PIDsTIDs']:
            self.showMessage(
                TEXT[self.config['INITIAL']['IDIOMA']]['Seleccione datos'],
                TEXT[self.config['INITIAL']['IDIOMA']]['erro-sin-seleccion'], 'warning')
        else:
            # creating a thread
            Thread_loadFile = Thread(
                target=lambda: self.xerarNovoScatterTemporalThread(info))

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()

            self.showNewGraphic()

    '''
    *******************************************************************************
    ************* Funcións xerais para gardar as imaxes das gráficas **************
    *******************************************************************************
    '''

    def gardarNovoHeatMap(self, info):
        self.openSaveAsDialog(info=info, graphType='heatmap')

    def gardarNovoScatter(self, info):
        self.openSaveAsDialog(info=info, graphType='scatter')

    def gardarNovoRooflineModel(self, info):
        self.openSaveAsDialog(info=info, graphType='roofline')

    def gardarNovoScatterTemporal(self, info):
        self.openSaveAsDialog(info=info, graphType='scatter-temporal')

    def openSaveAsDialog(self, info, graphType):
        info['graphType'] = graphType
        saveImaxeDialog = sim.gardarImaxeModal(self, info)
        result = saveImaxeDialog.show()
        if result['do']:
            if not info['PIDsTIDs']:
                self.showMessage(
                    TEXT[self.config['INITIAL']
                         ['IDIOMA']]['Seleccione datos'],
                    TEXT[self.config['INITIAL']['IDIOMA']]['erro-sin-seleccion'], 'warning')
            elif result['type'] == 'heatmap':
                # creating a thread
                Thread_loadFile = Thread(
                    target=lambda: self.xerarNovaHeatMapThread(info, result))

                # change T to daemon
                Thread_loadFile.daemon = True
                Thread_loadFile.start()
            elif result['type'] == 'scatter':
                # creating a thread
                Thread_loadFile = Thread(
                    target=lambda: self.xerarNovoScatterThread(info, result))

                # change T to daemon
                Thread_loadFile.daemon = True
                Thread_loadFile.start()
            elif result['type'] == 'roofline':
                # creating a thread
                Thread_loadFile = Thread(
                    target=lambda: self.xerarNovoRooflineThread(info, result))

                # change T to daemon
                Thread_loadFile.daemon = True
                Thread_loadFile.start()
            elif result['type'] == 'scatter-temporal':
                # creating a thread
                Thread_loadFile = Thread(
                    target=lambda: self.xerarNovoScatterTemporalThread(info, result))

                # change T to daemon
                Thread_loadFile.daemon = True
                Thread_loadFile.start()

    '''
    *******************************************************************************
    ********* Funcións xerais para mostrar que se está a xerar a gráfica **********
    *******************************************************************************
    '''

    def showNewGraphic(self):

        self.showMessage(TEXT[self.config['INITIAL']['IDIOMA']]['Xerando gráfica'],
                         TEXT[self.config['INITIAL']['IDIOMA']]['info-creating-graph'])
        '''showinfo(
            title=TEXT[config['INITIAL']['IDIOMA']]['Xerando gráfica'],
            message=TEXT[config['INITIAL']['IDIOMA']]['info-creating-graph']
        )'''

    def showMessage(self, title, message, type='info'):
        from tkinter import messagebox as msgb

        self.root = tk.Tk()
        self.root.withdraw()
        self.root.after(8000, self.root.destroy)
        try:
            if type == 'info':
                msgb.showinfo(title, message, master=self.root)
            elif type == 'warning':
                msgb.showwarning(title, message, master=self.root)
            elif type == 'error':
                msgb.showerror('Error', message, master=self.root)
        except:
            pass

    '''
    *******************************************************************************
    ******************* Funcións xerais para obter información ********************
    *******************************************************************************
    '''

    def getDataFile(self):
        '''
        Devolve unha variable ca información lida do arquivo
        '''
        return self.infoData[0][1]

    def getColumnsFile(self):
        '''
        Devolve unha lista cas columnas que contén o dataFrame
        '''
        return self.infoData[0][1].columns

    def getPidsTids(self):
        return self.pidsTids

    def getCPUs(self):
        aux = {}
        aux['cpus'] = list(range(max(self.infoData[0][1].CPU) + 1))
        return aux

    def getColors(self):
        return getColors()

    def getColorsContinuos(self):
        return getColorsContinuos()

    def getColorsLines(self):
        return getColorsLines()

    def getCalcularOutliers(self, zName, info):
        return calcularOutliers(self.infoData[0][1], zName, info)

    def askReloadApp(self):
        global askExit
        answer = askyesnocancel(
            title=TEXT[self.config['INITIAL']['IDIOMA']]['Reiniciar?'],
            message=TEXT[self.config['INITIAL']['IDIOMA']]['text-ask-reload']
        )
        # true = si
        # false = non
        # cancel = None
        if answer:
            askExit = True
            self.destroy()

    def getConfig(self):
        return self.config

    def editConfig(self):
        ''

    '''
    *******************************************************************************
    *********** Función auxiliar para devolver un diccionario cos PIDs ************
    *******************************************************************************
    '''

    def loadPids(self, data: pd.DataFrame):
        dataNoRepeat = data.drop_duplicates(subset=["PID"], keep='first')
        # Create an empty list
        infoAux = {}

        # Iterate over each row
        for rows in dataNoRepeat.itertuples():

            item = data.loc[data['PID'] == rows.PID]
            if rows.PID in infoAux:
                aux = infoAux[rows.PID]
                for it in item.itertuples():
                    aux.append(it.TID)
                aux = list(set(aux))
                infoAux[rows.PID] = aux
            else:
                aux = []
                for it in item.itertuples():
                    aux.append(str(it.TID) + '&&&' + it.CMDLINE)
                aux = list(set(aux))
                infoAux[rows.PID] = aux

        return infoAux


if __name__ == '__main__':
    app = AppController(className="NUMA data visualization")
    app.mainloop()
    if askExit:
        os.execl(sys.executable, sys.executable, *sys.argv)
