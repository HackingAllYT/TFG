
import tkinter as tk

from pathlib import Path
import configparser
from text import TEXT, RESOLU
from StartPage import StartPage
from PageOne import PageOne
from PageTwo import PageTwo
from threading import *
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno, askyesnocancel
from migplot import (
    parse_file,
    initial_chart,
    interactive_chart_plot,
    interactive_scatter,
    getColors,
    getColorsContinuos,
    calcularOutliers
)
from checkBoxTreeview import loadPids
import modalConfiguration as cm
import modalSelectFigure as msf
from EditHeatMap import HeatMapPane
from EditScatterPane import ScatterPane
from EditRooflineModel import RooflineModelPane
import modalGardarImaxe as sim


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')

askExit = True


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


LARGE_FONT = ("Verdana", 12)


class AppController(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(RESOLU[config['INITIAL']['RESOLU']])
        self.resizable(False, False)
        self.center()
        self.iconphoto(False, tk.PhotoImage(
            file=relative_to_assets('icon/icon.png')))
        self.title('Aplicación para a visualización de datos de servidores NUMA')
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Variables que nos serven para coñecer a cantidade de gráficas xeradas
        self.numHeatmap = 0
        self.numScatter = 0
        self.numRoofMod = 0
        self.numRoofCol = 0
        self.numRoofM3D = 0

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
            title=TEXT[config['INITIAL']['IDIOMA']]['Escolla un arquivo:'],
            initialdir='/',
            filetypes=filetypes)

        if filename:
            print(filename, type(filename))
            self.frames[StartPage].setEntryName(filename)
            # creating a thread
            Thread_loadFile = Thread(target=self.loadFileThread)

            # change T to daemon
            Thread_loadFile.daemon = True
            Thread_loadFile.start()
            self.frames[StartPage].setButtonsEnabled()

    def showPaxResumoArquivo(self):
        self.show_frame(PageOne)

    '''
    *******************************************************************************
    ******************** Funcións auxiliares do Frame Inicial *********************
    *******************************************************************************
    '''

    def loadFileThread(self):
        global infoData, info
        infoData = []
        showinfo(
            title=TEXT[config['INITIAL']['IDIOMA']]['Arquivo seleccionado:'],
            message=filename
        )
        if type(filename) == str:
            data = parse_file(file=filename)
            info = loadPids(data=data)
            infoData.append([filename, data])
            initial_chart(data=data)
        else:
            for x in filename:
                data = parse_file(file=x)
                info = loadPids(data=data)
                infoData.append([x, data])
                initial_chart(data=data)

    def xerarNovaHeatMapThread(self, info):
        global infoData
        aux = (infoData[0][1].columns.get_loc(info['xRow']),
               infoData[0][1].columns.get_loc(info['yRow']), info['zRow'])

        interactive_chart_plot(
            index=aux,
            plotName=info['name'],
            data=infoData[0][1],
            save=None,
            infoData=info['PIDsTIDs'],
            colors=info['colors']
        )

    def xerarNovoScatterThread(self, info):
        global infoData
        aux = (infoData[0][1].columns.get_loc(info['xRow']),
               infoData[0][1].columns.get_loc(info['yRow']), info['zRow'])

        interactive_scatter(
            index=aux,
            plotName=info['name'],
            data=infoData[0][1],
            save=None,
            lines=info['unir'],
            infoData=info['PIDsTIDs'],
            colors=info['colors']
        )

    def xerarNovoRooflineThread(self, info):
        ''

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame One ************************
    *******************************************************************************
    '''

    def openConfigurationModal(self):
        global conModal

        conModal = cm.configurationModal(self)
        result = conModal.show()
        if result == True:
            self.update()
            self.update_idletasks()

    def openSelectFigureModal(self):
        global figModal
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

    def mostrarHomedendeImaxe(self):
        self.show_frame(StartPage)

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame Two ************************
    *******************************************************************************
    '''

    def confirmExit(self):
        answer = askyesno(
            title=TEXT[config['INITIAL']['IDIOMA']]['Saír?'],
            message=TEXT[config['INITIAL']['IDIOMA']
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
        # creating a thread
        Thread_loadFile = Thread(
            target=lambda: self.xerarNovaHeatMapThread(info))

        # change T to daemon
        Thread_loadFile.daemon = True
        Thread_loadFile.start()

        self.showNewGraphic()

    def xerarNovoScatter(self, info):
        # creating a thread
        Thread_loadFile = Thread(
            target=lambda: self.xerarNovoScatterThread(info))

        # change T to daemon
        Thread_loadFile.daemon = True
        Thread_loadFile.start()

        self.showNewGraphic()

    def xerarNovoRooflineModel(self, info):
        # creating a thread
        Thread_loadFile = Thread(
            target=lambda: self.xerarNovoRooflineThread(info))

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

    def openSaveAsDialog(self, info, graphType):
        info['graphType'] = graphType
        saveImaxeDialog = sim.gardarImaxeModal(self, info)
        result = saveImaxeDialog.show()
        if result['do']:
            if result['type'] == 'heatmap':
                interactive_chart_plot(
                    x_index=infoData[0][1].columns.get_loc(info['xRow']),
                    y_index=infoData[0][1].columns.get_loc(info['yRow']),
                    zName=info['zRow'],
                    plotName=info['name'],
                    data=infoData[0][1],
                    save=result
                )
    '''
    *******************************************************************************
    ********* Funcións xerais para mostrar que se está a xerar a gráfica **********
    *******************************************************************************
    '''

    def showNewGraphic(self):
        showinfo(
            title=TEXT[config['INITIAL']['IDIOMA']]['Xerando gráfica'],
            message=TEXT[config['INITIAL']['IDIOMA']]['info-creating-graph']
        )

    '''
    *******************************************************************************
    ******************* Funcións xerais para obter información ********************
    *******************************************************************************
    '''

    def getDataFile(self):
        return infoData[0][1]

    def getColumnsFile(self):
        return infoData[0][1].columns

    def getPidsTids(self):
        return info

    def getCPUs(self):
        aux = {}
        aux['cpus'] = list(range(max(infoData[0][1].CPU) + 1))
        return aux

    def getColors(self):
        return getColors()

    def getColorsContinuos(self):
        return getColorsContinuos()

    def getCalcularOutliers(self, zName, info):
        return calcularOutliers(infoData[0][1], zName, info)

    def askReloadApp(self):
        global askExit
        answer = askyesnocancel(
            title=TEXT[config['INITIAL']['IDIOMA']]['Reiniciar?'],
            message=TEXT[config['INITIAL']['IDIOMA']]['text-ask-reload']
        )
        # true = si
        # false = non
        # cancel = None
        if answer:
            askExit = True
            self.destroy()


if __name__ == '__main__':
    while askExit:
        app = AppController(className="NUMA data visualization")
        app.mainloop()
