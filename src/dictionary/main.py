
"""A lexicon manager/dictionary. Different views, filterable, editable."""

from sys import path
import os.path
if path[0] == os.path.dirname(__file__):
    # modify sys.path so that it points to src, not to src/dictionary
    path[0] = os.path.dirname(path[0]) # parent directory

import common
import wx

PARTS_OF_SPEECH = [
    "unspecified",
    "noun",
    "verb",
    "adjective",
    "adverb",
    "pronoun",
    "preposition",
    "conjunction",
    "particle",
    "phrase",
    # anything missing?
]
POS_UNSPECIFIED = 0

from dictionary import entries

class DictionaryWin(common.CDSWin):
    title = "CDS Dictionary"
    _selected = 0
    def __init__(self):
        super().__init__()
        # substitute Dictionary with implementation class here:
        self.dict = Dictionary()
    
    def build(self):
        from dictionary import filtering
        
        self.frame.Sizer = wx.BoxSizer(wx.VERTICAL)
        
        # on top, the filter panel
        self.dictFilter = filtering.Filter(self)
        self.frame.Sizer.Add(self.dictFilter.panel, proportion=0, flag=wx.EXPAND)
        self.dictFilter.build()
        # below, the entry list and entry properties
        # in a SplitterWindow so the width can be adjusted
        self.splitter = wx.SplitterWindow(self.frame, style=wx.SP_LIVE_UPDATE)
        self.frame.Sizer.Add(self.splitter, proportion=1, flag=wx.EXPAND)
        
        self.bottom = wx.Panel(self.frame)
        self.frame.Sizer.Add(self.bottom, proportion=0, flag=wx.EXPAND)
        self.bottom.Sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.addButton = wx.Button(self.bottom, id=wx.ID_ADD)
        self.removeButton = wx.Button(self.bottom, id=wx.ID_REMOVE)
        self.bottom.Sizer.Add(self.addButton, proportion=1, flag=wx.ALL, border=5)
        self.bottom.Sizer.Add(self.removeButton, proportion=1, flag=wx.ALL, border=5)
        
        # entries in a ListBox to the left, properties on the right get their own class
        self.entriesBox = wx.ListBox(self.splitter, style=wx.LB_NEEDED_SB|wx.LB_SORT)
        self.entryProperties = entries.EntryProperties(self)
        self.splitter.SplitVertically(self.entriesBox, self.entryProperties.panel, sashPosition=150)
        self.entryProperties.build()
        
        self.frame.Fit()
        self.frame.MinSize = self.frame.Size
        
        self.bottom.Bind(wx.EVT_BUTTON, lambda e: self.newEntry(), self.addButton)
        self.bottom.Bind(wx.EVT_BUTTON, lambda e: self.removeEntry(), self.removeButton)
        self.frame.Bind(wx.EVT_LISTBOX, self.onListbox, self.entriesBox)
        
    
    def filter(self, filterOptions):
        # use the filterOptions to filter the entry list on the left
        # this requires keeping all the entries in a data structure and building the
        # list box contents dynamically
        # either: filteredEntries = self.dict.filter(filterOptions)
        # then clear the list box and populate with the filtered entries (easy to code)
        # or (harder to code, but faster): iterate over the list box’s items and remove
        # those that don’t satisfy the filter.
        index = 0
        while index < self.entriesBox.Count:
            key = self.entriesBox.GetClientData(index)
            if filterOptions.allow(self._dict.get(key)):
                index += 1
            else:
                self.entriesBox.Delete(index)
        
    def newEntry(self, entry=None):
        if entry is None: entry = entries.Entry()
        # add entry to the dictionary data structure
        # keeping its unique key (index or whatever)
        key = self.dict.add(entry)
        # add the word to the list box and store the key as cliënt data
        self.entriesBox.Append(entry.word if entry.word is not None else "", key)
    
    def removeEntry(self, index=None):
        if index is None: index = self._selected
        # remove it from the dictionary backend
        removed = self.dict.delete(self.entriesBox.GetClientData(index))
        # remove it from the ListBox
        self.entriesBox.Delete(index)
    
    def updateEntry(self, index=None, entry=None):
        selected = index is None
        if selected:
            index = self._selected
            entry = self.entryProperties.get()
        key = self.entriesBox.GetClientData(index)
        self.dict.update(key, entry)
        self.entriesBox.Delete(index)
        index = self.entriesBox.Append(entry, key)
        if selected:
            self.entriesBox.Selection = index
            self._selected = index
    
    
    def onListbox(self, event):
        if not self.entryProperties.save():
            self.entriesBox.Selection = self._selected # restore selection
            return
        self._selected = event.Selection;
        key = event.ClientData
        self.entryProperties.load(self.dict.getEntry(key))


class Dictionary:
    "Abstract class for the data structure storing the dictionary."
    def get(self, key):
        pass
    def add(self, entry):
        # return the new key
        return 0
    def delete(self, key):
        ##return Entry()
        pass
    def update(self, key, entry):
        # if entry is None, do nothing!
        pass
    def filter(self, filterOptions):
        # return a mapping from key to item
        return {}

class DictDictionary(Dictionary):
    _dict = []
    def get(self, key):
        return _dict[key]

    def add(self, entry):
        key = hash(entry)
        while key in _dict:
            key += 1
        _dict[key] = entry
        return key

    def delete(self, key):
        return _dict.pop(key)

    def update(self, key, entry):
        _dict[key].update(entry)

    def filter(self, filterOptions):
        result = {}
        for key, entry in _dict.items():
            if filterOptions.allow(entry):
                result[key] = entry
