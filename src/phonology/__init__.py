
"""A phonology editor with IPA chart, phonotactics, allophony, etc."""

from sys import path
import os.path
if path[0] == os.path.dirname(__file__):
    # modify sys.path so that it points to src, not to src/phonology
    path[0] = os.path.dirname(path[0]) # parent directory

import common
import wx

class PhonologyView:
    "Abstract base class for views in the Phonology window."
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.notebook)
    def build(self):
        "Build the GUI and everything belonging to it."
        # abstract method
        pass

from . import inventory, allophony, phonotactics

class PhonologyWin(common.CDSWin):
    title = "CDS Phonology"
    
    def viewInventory(self):
        self.notebook.ChangeSelection(0)
    def viewAllophony(self):
        self.notebook.ChangeSelection(1)
    def viewPhonotactics(self):
        self.notebook.ChangeSelection(2)
    
    def build(self):
        # a Notebook that gives a choice between
        # inventory, phonotactics, and allophony (and possibly more)
        self.notebook = wx.Notebook(self.frame, style=wx.NB_TOP)
        self.notebook.SetDoubleBuffered(True)

        self.inventory = inventory.InventoryView(self)
        self.allophony = allophony.AllophonyView(self)
        self.phonotactics = phonotactics.PhonotacticsView(self)

        self.notebook.AddPage(self.inventory.panel, "Inventory")
        self.notebook.AddPage(self.allophony.panel, "Allophony")
        self.notebook.AddPage(self.phonotactics.panel, "Phonotactics")

        self.viewInventory() # select the first page, which is Inventory

        self.inventory.build()
        self.allophony.build()
        self.phonotactics.build()
        pass
