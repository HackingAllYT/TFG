
import tkinter as tk

from pathlib import Path
import configparser
from text import TEXT
from StartPage import StartPage
from PageOne import PageOne
from PageTwo import PageTwo
from threading import *
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno
from migplot import parse_file, initial_chart, interactive_chart_plot
from checkBoxTreeview import loadPids
import modalConfiguration as cm
import modalSelectFigure as msf
from EditHeatMap import HeatMapPane


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

config = configparser.ConfigParser()
config.read('config.ini')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1024x720')
        self.resizable(False, False)
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        self.eval('tk::PlaceWindow . center')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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

    def clear_entry(self):
        self.show_frame(PageOne)

    def showSelection(self):
        self.frames[PageTwo].addFrame(HeatMapPane, 'HeatMap')
        self.show_frame(PageTwo)

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

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame One ************************
    *******************************************************************************
    '''

    def openConfigurationModal(self):
        global conModal
        #conModal = cm.configurationModal(window)
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
            print("Pasamos por qui")
            self.frames[PageTwo].addFrame(HeatMapPane, 'HeatMap')
            self.show_frame(PageTwo)
        elif result == 'scatter':
            ""

    def mostrarHomedendeImaxe(self):
        self.show_frame(StartPage)

    '''
    *******************************************************************************
    ************************ Funcións propias do Frame Two ************************
    *******************************************************************************
    '''

    def confirmExit(self):
        answer = askyesno(title=TEXT[config['INITIAL']['IDIOMA']]['Saír?'],
                          message=TEXT[config['INITIAL']['IDIOMA']]['Está seguro que quere pechar?'])
        if answer:
            self.destroy()

    def xerarNovaGrafica(self, info):
        interactive_chart_plot(
            x_index=infoData[0][1].columns.get_loc(info['xRow']),
            y_index=infoData[0][1].columns.get_loc(info['yRow']),
            zName=info['zRow'],
            plotName=info['name'],
            data=infoData[0][1]
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


if __name__ == '__main__':
    app = SeaofBTCapp()
    app.eval('tk::PlaceWindow . center')
    app.mainloop()
