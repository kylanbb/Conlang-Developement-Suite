
"""This sets up the application object and dispatches creätion of new windows."""

# TODO: rewrite so that sub-apps are dynamically looked up instead of statically listed

from sys import path
import os.path
if path[0] == os.path.dirname(__file__):
    # modify sys.path so that it points to src, not to src/common
    path[0] = os.path.dirname(path[0]) # parent directory

import wx

class CDSWin:
    "Abstract base class for app windows."
    MIN_HEIGHT = 0
    MIN_WIDTH = 0
    
    title = ""
    def __init__(self):
        # creäte a top-level window, leave the rest to derived classes
        self.frame = wx.Frame(None, title=self.title)
        self.frame.Bind(wx.EVT_CLOSE, lambda e: wx.GetApp().closeWindow(self))

    def build(self):
        "Build the GUI and everything belonging to it."
        # abstract method
        pass
    
    def resetMinSize(self):
        self.frame.MinSize = wx.Size(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.frame.Fit()
        self.frame.MinSize = self.frame.Size

def _windowTypes():
    import dictionary, phonology #, family
    import common.launcher as launcher
    return {
        "launch": launcher.LauncherWin,
        "dictionary": dictionary.DictionaryWin,
        #"family": family.FamilyWin,
        "phonology": phonology.PhonologyWin
        # and more to come
    }

from sys import argv

class CDSApp(wx.App):
    "The application."
    wins = []
       
    def newWindow(self, typ):
        try:
            cdsWin = _windowTypes()[typ]() # intentionally unsafe
            cdsWin.build()
            cdsWin.frame.Show()
            self.wins.append(cdsWin)
        except:
            self.closeWindow(cdsWin)
            raise
        return cdsWin

    def closeWindow(self, window):
        if window in self.wins:
            self.wins.remove(window)
        window.frame.Destroy()
    
    def OnInit(self):
        if len(argv) > 1 and argv[1] in _windowTypes():
            firstWin = self.newWindow(argv[1])
        else:
            firstWin = self.newWindow("launch")
        self.SetTopWindow(firstWin.frame)
        return True
