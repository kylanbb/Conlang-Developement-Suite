
import wx

class Filter:
    "The dictionary filter pane at the top."
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.frame)
    def build(self):
        "Build the GUI and everything belonging to it."
        # text entry and filter options, powerful but easy to understand
        # to the ‘Apply Filter’ button or whatever, bind parent.filter
        self.filterText = wx.TextCtrl(self.panel, value="filter", style=wx.TE_PROCESS_ENTER)
        self.panel.Sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.Sizer.Add(filterText, proportion=1, flag=wx.EXPAND)
        # somehow not visible.?

class FilterOptions:
    "Data class representing the state of the filter."
    # methods to set, modify, and query the filtering options
    def allow(self, entry):
        "Whether the filter allows that entry or not"
        pass
