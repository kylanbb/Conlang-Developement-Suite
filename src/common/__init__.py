
"""This sets up the application object and dispatches creätion of new windows."""

# TODO: rewrite so that sub-apps are dynamically looked up instead of statically listed

import wx
from sys import argv
from .. import dictionary, phonology #, family
from . import launcher

windowTypes = {
    "launch": launcher.Launcher,
    "dictionary": dictionary.Dictionary,
    #"family": family.Family,
    "phonology": phonology.Phonology
    # and more to come
    }

class CDSWin:
    "Abstract base class for app windows."
    frame = None
    def __init__(self):
        # creäte a top-level window, leave the rest to derived classes
        self.frame = wx.Frame(None)
        self.build()
    def build(self):
        "Build the GUI and everything belonging to it."
        # abstract method
        pass
    

class CDSApp(wx.App):
    "The application."
    wins = []

    def newWindow(self, typ):
        cdsWin = windowTypes[typ]() # intentionally unsafe
        wins.append(cdsWin)
        return cdsWin
    
    def OnInit(self):
        if argv[1] in windowTypes:
            firstWin = self.newWindow(argv[1])
        else:
            firstWin = self.newWindow("launch")
        self.SetTopWindow(firstWin.frame)
        return True
