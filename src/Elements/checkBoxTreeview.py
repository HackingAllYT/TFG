import tkinter.ttk as ttk
import tkinter as tk
from tkinter import ttk

import numpy as np
from src.config.text import TREETYPE_TIDs_PIDs, TREETYPE_CPUs, RESOLU


'''
*******************************************************************************
*************************** Checbox Treeview Class ****************************
*******************************************************************************
'''


class CheckboxTreeview(ttk.Treeview):
    """
        Treeview widget with checkboxes left of each item.
        The checkboxes are done via the image attribute of the item, so to keep
        the checkbox, you cannot add an image to the item.
    """

    def __init__(self, master=None, treeType: str = None, editClass=None, controller=None, **kw):
        if treeType != None:
            ttk.Treeview.__init__(self, master, columns=(
                'Todos'), selectmode="extended", ** kw)

            self.relative_to_assets = controller.relative_to_assets
            # checkboxes are implemented with pictures
            self.im_checked = tk.PhotoImage(
                file=self.relative_to_assets('checked_18x18.png'))
            self.im_unchecked = tk.PhotoImage(
                file=self.relative_to_assets('unchecked_18x18.png'))
            self.im_tristate = tk.PhotoImage(
                file=self.relative_to_assets('tristate_18x18.png'))
            self.tag_configure("unchecked", image=self.im_unchecked)
            self.tag_configure("tristate", image=self.im_tristate)
            self.tag_configure("checked", image=self.im_checked)
            # check / uncheck boxes on click
            self.bind("<Button-1>", self.box_click, True)
            vsb = ttk.Scrollbar(self, orient="vertical", command=self.yview)
            vsb.pack(side='right', fill='y')

            hsb = ttk.Scrollbar(self, orient='horizontal', command=self.xview)
            hsb.pack(side='bottom', fill='x')

            self.itemsPidTidSelected = {}
            self.itemsCpuSelected = []
            self.treeType = treeType
            self.editClass = editClass
            self.bind('<ButtonRelease-1>', self.selectItem)
            self.config = controller.getConfig()
            if self.config["INITIAL"]['RESOLU'] == RESOLU['1']:
                self.column("Todos", minwidth=300, width=300, stretch=tk.NO)
            elif self.config["INITIAL"]['RESOLU'] == RESOLU['2']:
                self.column("Todos", minwidth=500, width=500, stretch=tk.NO)

            self.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

    def insert(self, parent, index, iid=None, **kw):
        """ same method as for standard treeview but add the tag 'unchecked'
            automatically if no tag among ('checked', 'unchecked', 'tristate')
            is given """
        if not "tags" in kw:
            kw["tags"] = ("unchecked",)
        elif not ("unchecked" in kw["tags"] or "checked" in kw["tags"]
                  or "tristate" in kw["tags"]):
            kw["tags"] = ("unchecked",)
        ttk.Treeview.insert(self, parent, index, iid, **kw)

    def check_descendant(self, item):
        """ check the boxes of item's descendants """
        children = self.get_children(item)
        for iid in children:
            self.item(iid, tags=("checked",))
            self.check_descendant(iid)

    def check_ancestor(self, item):
        """ check the box of item and change the state of the boxes of item's
            ancestors accordingly """
        self.item(item, tags=("checked",))
        parent = self.parent(item)
        if parent:
            children = self.get_children(parent)
            b = ["checked" in self.item(c, "tags") for c in children]
            if False in b:
                # at least one box is not checked and item's box is checked
                self.tristate_parent(parent)
            else:
                # all boxes of the children are checked
                self.check_ancestor(parent)

    def tristate_parent(self, item):
        """ put the box of item in tristate and change the state of the boxes of
            item's ancestors accordingly """
        self.item(item, tags=("tristate",))
        parent = self.parent(item)
        if parent:
            self.tristate_parent(parent)

    def uncheck_descendant(self, item):
        """ uncheck the boxes of item's descendant """
        children = self.get_children(item)
        for iid in children:
            self.item(iid, tags=("unchecked",))
            self.uncheck_descendant(iid)

    def uncheck_ancestor(self, item):
        """ uncheck the box of item and change the state of the boxes of item's
            ancestors accordingly """
        self.item(item, tags=("unchecked",))
        parent = self.parent(item)
        if parent:
            children = self.get_children(parent)
            b = ["unchecked" in self.item(c, "tags") for c in children]
            if False in b:
                # at least one box is checked and item's box is unchecked
                self.tristate_parent(parent)
            else:
                # no box is checked
                self.uncheck_ancestor(parent)

    def box_click(self, event):
        """ check or uncheck box when clicked """
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify("element", x, y)
        if "image" in elem:
            # a box was clicked
            item = self.identify_row(y)
            tags = self.item(item, "tags")
            if ("unchecked" in tags) or ("tristate" in tags):
                self.check_ancestor(item)
                self.check_descendant(item)
            else:
                self.uncheck_descendant(item)
                self.uncheck_ancestor(item)

    def insertElements(self, info: dict, treeType: str):
        """
        Función que serve para insertar os elementos que se atopan no diccionario
        dependendo do tipo de datos que sexan, TREETYPE_TIDs_PIDs ou TREETYPE_CPUs
        """
        self.insert("", 0, "Todos", text="Todos")
        aux = "Todos"
        if treeType == TREETYPE_TIDs_PIDs:
            for pid in info:
                self.insert(aux, "end", pid, text=pid)
                aux = pid
                tids = info[pid]
                for tid in tids:
                    tid = tid.split('&&&')
                    tid = tid[0] + ' ' + tid[1]
                    self.insert(pid, "end", str(pid)+'-'+str(tid), text=tid)
                aux = "Todos"
        elif treeType == TREETYPE_CPUs:
            datos = info['cpus']
            for cpu in datos:
                self.insert(aux, "end", cpu, text=cpu)

    '''
    *******************************************************************************
    ***** Funcións que serven para actualizar o valor dos items seleccionados *****
    *******************************************************************************
    '''

    def selectItem(self, e):
        if self.treeType == TREETYPE_TIDs_PIDs:
            self.__selectItemTidPid__()
        elif self.treeType == TREETYPE_CPUs:
            self.__selectItemCpu__()
        if self.editClass:
            self.editClass.zDataCallback(None)

    '''
    *******************************************************************************
    ***** Funcións que serven para actualizar o valor dos items seleccionados *****
    ************ no caso de que o treeview sexa un TREETYPE_TIDs_PIDs *************
    *******************************************************************************
    '''

    def __selectItemTidPid__(self):
        curItem = self.focus()
        item = self.item(curItem)
        if item["tags"][0] == 'checked':
            if '-' in curItem:
                # Isto quere dicir que é un TID
                info = curItem.split('-')
                self.insertItemSelected(info)
            elif 'Todos' in curItem:
                childrens = self.get_children(curItem)
                for PID in childrens:
                    childrens = self.get_children(PID)
                    for child in childrens:
                        info = child.split('-')
                        self.insertItemSelected(info)
            else:
                # Isto quere dicir que é un PID
                childrens = self.get_children(curItem)
                for child in childrens:
                    info = child.split('-')
                    self.insertItemSelected(info)

        elif item['tags'][0] == 'unchecked':
            if '-' in curItem:
                # Isto quere dicir que é un TID
                info = curItem.split('-')
                if info[0] in self.itemsPidTidSelected:
                    self.itemsPidTidSelected[info[0]].remove(info[1])
                    if not self.itemsPidTidSelected[info[0]]:
                        self.itemsPidTidSelected.pop(info[0])
            elif 'Todos' in curItem:
                self.itemsPidTidSelected = {}
            else:
                # Isto quere dicir que é un PID
                if curItem in self.itemsPidTidSelected:
                    self.itemsPidTidSelected.pop(curItem)

        for i in self.itemsPidTidSelected:
            aux = np.unique(self.itemsPidTidSelected[i])
            self.itemsPidTidSelected[i] = list(aux)

    def insertPIDSelected(self, childrens: tuple[str, ...]):
        for child in childrens:
            info = child.split('-')
            self.insertItemSelected(info)

    def insertItemSelected(self, info: list[str]):
        if info[0] in self.itemsPidTidSelected:
            self.itemsPidTidSelected[info[0]].append(info[1].split(' ')[0])
        else:
            self.itemsPidTidSelected[info[0]] = [info[1].split(' ')[0]]

    '''
    *******************************************************************************
    ***** Funcións que serven para actualizar o valor dos items seleccionados *****
    *************** no caso de que o treeview sexa un TREETYPE_CPUs ***************
    *******************************************************************************
    '''

    def __selectItemCpu__(self):
        '''
        Función privada que lle serve á clase para actualizar o valor da lista que 
        contén a información das CPUs seleccionadas 
        '''
        curItem = self.focus()
        item = self.item(curItem)
        if item["tags"][0] == 'checked':
            if 'Todos' in curItem:
                self.itemsCpuSelected = []
                childrens = self.get_children(curItem)
                for child in childrens:
                    self.itemsCpuSelected.append(child)
            else:
                self.itemsCpuSelected.append(curItem)
        elif item['tags'][0] == 'unchecked':
            if 'Todos' in curItem:
                self.itemsCpuSelected = []
            else:
                self.itemsCpuSelected.remove(curItem)

        self.itemsCpuSelected.sort()

    '''
    *******************************************************************************
    *** Función que serve para devolver un diccionario cos items seleccionados ****
    *******************************************************************************
    '''

    def getSelectedItemsPIDsTIDs(self):
        '''
        Devolve un diccionario dos items seleccionados formado por:
        @clave: PID dos procesos
        @valor: array cos TIDs asociados ao proceso
        '''
        return self.itemsPidTidSelected

    def getSelectedItemsCPUs(self):
        '''
        Devolve unha lista formada polas CPUs seleccionadas
        '''
        return self.itemsCpuSelected
