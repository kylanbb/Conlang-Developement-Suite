
import wx
from dictionary import main

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
        
        self.panel.Sizer = wx.GridBagSizer(vgap=5, hgap=10)
        
        # creäte all the controls
        self.entryText = wx.TextCtrl(self.panel)
        self.posChoice = wx.Choice(self.panel, choices=main.PARTS_OF_SPEECH)
        self.pronuncText = wx.TextCtrl(self.panel)
        self.shortDefText = wx.TextCtrl(self.panel)
        self.longDefText = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        # for when there’s a pronunciation estimator, something like:
        ##self.pronuncChk = wx.CheckBox(self.panel, label="Custom pronunciation")
        self.classesChkLst = wx.CheckListBox(self.panel)
        ...
        self.createdLbl = wx.StaticText(self.panel, label="Entry creäted: ")
        
        self.posChoice.Selection = main.POS_UNSPECIFIED
        
        def label(lbl):
            return wx.StaticText(self.panel, label=lbl)
        
        # arrange them in a grid
        for args, kwargs in [
            ([label("Entry"), (0, 0)], {}),
            ([self.entryText,     (1, 0)], {"flag": wx.EXPAND}),
            ([label("Part of speech"), (0, 1)], {"flag": wx.TOP, "border": 5}),
            ([self.posChoice,     (1, 1)], {"flag": wx.EXPAND}),
            ([label("Pronunciation"), (2, 0)], {"flag": wx.TOP, "border": 5}),
            ([self.pronuncText,   (3, 0)], {"flag": wx.EXPAND}),
            ([label("Short definition"), (2, 1)], {"flag": wx.TOP, "border": 5}),
            ([self.shortDefText,  (3, 1)], {"flag": wx.EXPAND}),
            ([label("Long definition"), (4, 0)], {"flag": wx.TOP, "border": 5}),
            ([self.longDefText,   (5, 0)], {"flag": wx.EXPAND}),
            ([label("Classes"), (4, 1)], {"flag": wx.TOP, "border": 5}),
            ([self.classesChkLst, (5, 1)], {"flag": wx.EXPAND}),
            # ...
            ([self.createdLbl,    (6, 0)], {"flag": wx.EXPAND, "span": (0, 1)}),
        ]: self.panel.Sizer.Add(*args, **kwargs)
        self.panel.Sizer.AddGrowableCol(0, 1)
        self.panel.Sizer.AddGrowableCol(1, 1)
        self.panel.Sizer.AddGrowableRow(5, 1)
                
    def load(self, entry):
        pass
    def get(self):
        return Entry()
    
    def save(self):
        # (maybe ask for permission to save first)
        # take all the fields, store them in an entry
        # then call self.parent.update(entry)
        ...

class Entry:
    "Data class for everything associated with a dictionary entry"
    _fields = [
        "word",
        "shortDef",
        "longDef",
        "partOfSpeech",
        "pronunciation",
        "classes",
        "timeCreated",
    ]
    
    def __init__(self, 
            word=None,
            shortDef=None,
            longDef=None,
            partOfSpeech=None,
            pronunciation=None,
            classes=None,
            timeCreated=None):
        from datetime import datetime
        if timeCreated is None:
            self.timeCreated = datetime.now()
        else:
            self.timeCreated = timeCreated
        self.word = word
        self.shortDef = shortDef
        self.longDef = longDef
        self.partOfSpeech = partOfSpeech
        self.pronunciation = pronunciation
        self.classes = classes
        

    def update(self, other):
        "Update this entry with all fields that are not None in other"
        for field in self._fields:
            othervalue = getattr(other, field, None)
            if othervalue is not None:
                setattr(self, field, othervalue)
