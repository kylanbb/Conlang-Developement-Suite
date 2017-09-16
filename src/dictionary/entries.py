
import wx

_posChoices = [
    "unspecified",
    "noun",
    "verb",
    "adjective",
    "adverb",
    "pronoun",
    "preposition",
    "conjunction",
    "particle",
    "phrase"
    # anything missing?
]

class EntryProperties:
    "The entry properties pane on the right"
    def __init__(self, parent):
        self.parent = parent
        self.panel = wx.Panel(parent.splitter)
    def build(self):
        "Build the GUI and everything belonging to it."
        # text entries for all the entry properties, like word, POS,
        # pronunciation, translation/meaning, usage notes, derivation links
        # see issue #7
        self.panel.Sizer = wx.GridBagSizer(vgap=5, hgap=5)
        
        # creäte all the controls
        self.entryText = wx.TextCtrl(self.panel)
        self.posChoice = wx.Choice(self.panel, choices=_posChoices)
        self.shortDefText = wx.TextCtrl(self.panel)
        self.longDefText = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.pronuncText = wx.TextCtrl(self.panel)
        # for when there’s a pronunciation estimator, something like:
        ##self.pronuncChk = wx.CheckBox(self.panel, label="Custom pronunciation")
        self.classesChkLst = wx.CheckListBox(self.panel)
        ...
        self.createdLbl = wx.StaticText(self.panel, label="Entry creäted: ")
        
        # arrange them in a grid
        ##for args, kwargs in [
        ##    ([self.entryText,     (0, 0)], {"flag": wx.EXPAND}),
        ##    ([self.posChoice,     (0, 0)], {"flag": wx.EXPAND}),
        ##    ([self.shortDefText,  (0, 0)], {"flag": wx.EXPAND}),
        ##    ([self.longDefText,   (0, 0)], {"flag": wx.EXPAND}),
        ##    ([self.pronuncText,   (0, 0)], {"flag": wx.EXPAND}),
        ##    ([self.classesChkLst, (0, 0)], {"flag": wx.EXPAND}),
        ##    # ...
        ##    ([self.createdLbl,    (0, 0)], {"flag": wx.EXPAND})
        ##]: self.panel.Sizer.Add(*args, **kwargs)


class Entry:
    "Data class for everything associated with a dictionary entry"
    def __init__(self, word="", timeCreated=None):
        from datetime import datetime
        if timeCreated is None: self.timeCreated = datetime.now()
        else: self.timeCreated = timeCreated
        self.word = word
        ...
