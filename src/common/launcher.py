
"""A ‘launcher’ window that gives a simple choice between different sub-apps and maybe recently used files (like LibreOffice does if you start it directly)"""

from sys import path
import os.path
if path[0] == os.path.dirname(__file__):
    # modify sys.path so that it points to src, not to src/common
    path[0] = os.path.dirname(path[0]) # parent directory

import common
import wx

class LauncherWin(common.CDSWin):
    title = "Conlang Development Suite"
    def build(self):
        # this is not at all pretty, but for testing, it will do.
        phonologyButton = wx.Button(self.frame, label="Phonology")
        dictionaryButton = wx.Button(self.frame, label="Dictionary")
        ## other apps
        
        self.frame.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.frame.Sizer.Add(phonologyButton, wx.EXPAND)
        self.frame.Sizer.Add(dictionaryButton, wx.EXPAND)
        
        def onButton(windowType):
            # Return a button click event handler
            def handler(event):
                wx.GetApp().newWindow(windowType)
                self.frame.Close()
            return handler
        self.frame.Bind(wx.EVT_BUTTON, onButton("phonology"), phonologyButton)
        self.frame.Bind(wx.EVT_BUTTON, onButton("dictionary"), dictionaryButton)