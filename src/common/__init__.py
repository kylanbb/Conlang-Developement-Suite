# coding=utf-8
"""This sets up the application object and dispatches creätion of new windows."""

# TODO: rewrite so that sub-apps are dynamically looked up instead of statically listed

import wx
from sys import argv

class CDSWin:
    "Abstract base class for app windows."
    
    title = ""
    def __init__(self):
        # creäte a top-level window, leave the rest to derived classes
        self.frame = wx.Frame(None, title=self.title)
        self.frame.Bind(wx.EVT_CLOSE, lambda e: wx.GetApp().closeWindow(self))

    def build(self):
        "Build the GUI and everything belonging to it."
        # abstract method
        pass
    
import dictionary, phonology #, family
from . import launcher

windowTypes = {
    "launch": launcher.LauncherWin,
    "dictionary": dictionary.DictionaryWin,
    #"family": family.FamilyWin,
    "phonology": phonology.PhonologyWin
    # and more to come
    }

class CDSApp(wx.App):
    "The application."
    wins = []

    def newWindow(self, typ):
        cdsWin = windowTypes[typ]() # intentionally unsafe
        cdsWin.build()
        cdsWin.frame.Show()
        self.wins.append(cdsWin)
        return cdsWin

    def closeWindow(self, window):
        if window in self.wins:
            self.wins.remove(window)
        window.frame.Destroy()
    
    def OnInit(self):
        if len(argv) > 1 and argv[1] in windowTypes:
            firstWin = self.newWindow(argv[1])
        else:
            firstWin = self.newWindow("launch")
        self.SetTopWindow(firstWin.frame)
        return True
