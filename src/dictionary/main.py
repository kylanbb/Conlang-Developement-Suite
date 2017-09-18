
"""A lexicon manager/dictionary. Different views, filterable, editable."""

from sys import path
import os.path
if path[0] == os.path.dirname(__file__):
    # modify sys.path so that it points to src, not to src/dictionary
    path[0] = os.path.dirname(path[0]) # parent directory

import src.common as common

class DictionaryWin(common.CDSWin):
    title = "CDS Dictionary"
