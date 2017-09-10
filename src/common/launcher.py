
"""A ‘launcher’ window that gives a simple choice between different sub-apps and maybe recently used files (like LibreOffice does if you start it directly)"""

from . import main
import wx

class LauncherWin(main.CDSWin):
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