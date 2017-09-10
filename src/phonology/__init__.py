# coding=utf-8
"""A phonology editor with IPA chart, phonotactics, allophony, etc."""

import wx
import common
from . import inventory, allophony, phonotactics

class PhonologyView(object):
    "Abstract base class for views in the Phonology window."
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.notebook)
    def build(self):
        "Build the GUI and everything belonging to it."
        # abstract method
        pass


class PhonologyWin(common.CDSWin):
    title = "CDS Phonology"
    
    def viewInventory(self):
        self.notebook.ChangeSelection(0)
    def viewAllophony(self):
        self.notebook.ChangeSelection(1)
    def viewPhonotactics(self):
        self.notebook.ChangeSelection(2)

    def __init__(self):
        super(PhonologyWin, self).__init__(self)
        self.notebook = wx.Notebook(self.frame, style=wx.NB_TOP)
        self.inventory = inventory.InventoryView(self)
        self.allophony = allophony.AllophonyView(self)
        self.phonotactics = phonotactics.PhonotacticsView(self)

    
    def build(self):
        # a Notebook that gives a choice between
        # inventory, phonotactics, and allophony (and possibly more)
        self.notebook.SetDoubleBuffered(True)

        self.notebook.AddPage(self.inventory.panel, "Inventory")
        self.notebook.AddPage(self.allophony.panel, "Allophony")
        self.notebook.AddPage(self.phonotactics.panel, "Phonotactics")

        self.viewInventory() # select the first page, which is Inventory

        self.inventory.build()
        self.allophony.build()
        self.phonotactics.build()
