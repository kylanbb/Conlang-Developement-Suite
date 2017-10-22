
"""The phoneme inventory editor"""

from . import main
from . import consonantBank

class InventoryView(main.PhonologyView):
    def build(self):
        # make a split screen with two consonant charts and two vowel trapeziums;
        # one on top for the phonology being edited, one at the bottom for complete IPA
        pass

class ConsonantTable:
    def __init__(self, parent, readOnly):
        self.readOnly = readOnly
        self.panel = wx.Panel(parent.panel)
        self.parent = parent
    
    def build(self):
        # GridBagSizer for all the boxes
        # every phoneme box gets its own window
        # a static text or panel or something? Not sure
        self.panel.Sizer = wx.GridBagSizer(vgap=5, hgap=5)
        
        for box in consonantBank.consonants:
            ...
            for sound in box.getModels():
                ...
            ...
