
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
        pass

class FilterOptions:
    "Data class representing the state of the filter."
    # methods to set, modify, and query the filtering options
    def allow(self, entry):
        "Whether the filter allows that entry or not"
        pass
