import tkinter.ttk as ttk
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import numpy as np


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def loadPids(data):
    global info
    dataNoRepeat = data.drop_duplicates(subset=["PID"], keep='first')
    # Create an empty list
    info = {}

    # Iterate over each row
    for rows in dataNoRepeat.itertuples():

        item = data.loc[data['PID'] == rows.PID]
        if rows.PID in info:
            aux = info[rows.PID]
            for it in item.itertuples():
                aux.append(it.TID)
            aux = list(set(aux))
            info[rows.PID] = aux
        else:
            aux = []
            for it in item.itertuples():
                aux.append(it.TID)
            aux = list(set(aux))
            info[rows.PID] = aux

    return info


class CheckboxTreeview(ttk.Treeview):
    """
        Treeview widget with checkboxes left of each item.
        The checkboxes are done via the image attribute of the item, so to keep
        the checkbox, you cannot add an image to the item.
    """

    def __init__(self, master=None, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        # checkboxes are implemented with pictures
        self.im_checked = tk.PhotoImage(
            file=relative_to_assets('checked_18x18.png'))
        self.im_unchecked = tk.PhotoImage(
            file=relative_to_assets('unchecked_18x18.png'))
        self.im_tristate = tk.PhotoImage(
            file=relative_to_assets('tristate_18x18.png'))
        self.tag_configure("unchecked", image=self.im_unchecked)
        self.tag_configure("tristate", image=self.im_tristate)
        self.tag_configure("checked", image=self.im_checked)
        # check / uncheck boxes on click
        self.bind("<Button-1>", self.box_click, True)
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        vsb.pack(side='right', fill='y')

        self.itemsSelected = {}
        self.bind('<ButtonRelease-1>', self.selectItem)

        self.configure(yscrollcommand=vsb.set)

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

    def insertElements(self, info: dict):
        self.insert("", 0, "Todos", text="Todos")
        aux = "Todos"
        for pid in info:
            self.insert(aux, "end", pid, text=pid)
            aux = pid
            tids = info[pid]
            for tid in tids:
                self.insert(pid, "end", str(pid)+'-'+str(tid), text=tid)
            aux = "Todos"

    '''
    *******************************************************************************
    ***** Funcións que serven para actualizar o valor dos items seleccionados *****
    *******************************************************************************
    '''

    def selectItem(self, e):
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
                if info[0] in self.itemsSelected:
                    self.itemsSelected[info[0]].remove(info[1])
                    if not self.itemsSelected[info[0]]:
                        self.itemsSelected.pop(info[0])
            elif 'Todos' in curItem:
                self.itemsSelected = {}
            else:
                # Isto quere dicir que é un PID
                if curItem in self.itemsSelected:
                    self.itemsSelected.pop(curItem)

        for i in self.itemsSelected:
            aux = np.unique(self.itemsSelected[i])
            self.itemsSelected[i] = list(aux)

    def insertPIDSelected(self, childrens: tuple[str, ...]):
        for child in childrens:
            info = child.split('-')
            self.insertItemSelected(info)

    def insertItemSelected(self, info: list[str]):
        if info[0] in self.itemsSelected:
            self.itemsSelected[info[0]].append(info[1])
        else:
            self.itemsSelected[info[0]] = [info[1]]

    '''
    *******************************************************************************
    *** Función que serve para devolver un diccionario cos items seleccionados ****
    *******************************************************************************
    '''

    def getSelectedItems(self):
        return self.itemsSelected
