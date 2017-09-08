
"""The phoneme inventory editor"""

from . import main

class InventoryView(main.PhonologyView):
    def build(self):
        # make a split screen with two consonant charts and two vowel trapeziums;
        # one on top for the phonology being edited, one at the bottom for complete IPA
        pass
