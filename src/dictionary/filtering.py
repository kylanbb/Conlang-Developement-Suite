
import wx

class Filter:
    "The dictionary filter pane at the top."
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.frame)
    def build(self):
        "Build the GUI and everything belonging to it."
        self.panel.Sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # text entry and filter options, powerful but easy to understand
        self.filterText = wx.TextCtrl(self.panel, value="filter", style=wx.TE_PROCESS_ENTER)
        self.applyButton = wx.Button(self.panel, id=wx.ID_APPLY)
        self.panel.Sizer.Add(self.filterText, proportion=1, flag=wx.ALL, border=5)
        self.panel.Sizer.Add(self.applyButton, proportion=0, flag=wx.ALL, border=5)
        self.panel.Bind(wx.EVT_TEXT_ENTER, self.onFilter, self.filterText)
        self.panel.Bind(wx.EVT_BUTTON, self.onFilter, self.applyButton)
        # add stuff for properly controlling the filter
        
    def onFilter(self, event):
        self.parent.filter(self.getOptions())
    
    def getOptions(self):
        ##return FilterOptions()
        pass

class FilterOptions:
    "Data class representing the state of the filter."
    # methods to set, modify, and query the filtering options
    def allow(self, entry):
        "Whether the filter allows that entry or not"
        pass
