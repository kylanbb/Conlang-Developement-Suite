
import wx

class EntryProperties:
    "The entry properties pane on the right"
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.splitter)
    def build(self):
        "Build the GUI and everything belonging to it."
        # text entries for all the entry properties, like word, POS,
        # pronunciation, translation/meaning, usage notes, derivation links
        pass


class Entry:
    "Data class for everything associated with a dictionary entry"
    def __init__(self, word="", timeCreated=None):
        from datetime import datetime
        if timeCreated is None: self.timeCreated = datetime.now()
        else: self.timeCreated = timeCreated
        self.word = word
        ...
