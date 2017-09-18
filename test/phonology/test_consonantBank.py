import unittest
import sys
sys.path.append('../../')

from src.phonology.consonantBank import ConsonantModel, getBox

class TestPhonemeBox(unittest.TestCase): 
    def test_velar_nasal(self): 
        list = [
            ConsonantModel('ŋ̊', 'velar', 'nasal', 'voiceless'), 
            ConsonantModel('ŋ', 'velar', 'nasal', 'voiced')
        ]
        
        box = getBox('velar', 'nasal')
        boxList = box.getModels()
        
        self.assertEqual(boxList, list, "velar nasals not working")
        
    def test_bilabial_plosive(self): 
        list = [
            ConsonantModel('p', 'bilabial', 'plosive', 'voiceless'), 
            ConsonantModel('b', 'bilabial', 'plosive', 'voiced'), 
            ConsonantModel('pʰ', 'bilabial', 'plosive', 'aspirated'), 
            ConsonantModel('pʼ', 'bilabial', 'plosive', 'ejective'), 
            ConsonantModel('ᵐb', 'bilabial', 'plosive', 'prenasal'), 
            ConsonantModel('ɓ', 'bilabial', 'plosive', 'implosive')
        ]
        
        box = getBox('bilabial', 'plosive')
        boxList = box.getModels()
        
        self.assertEqual(boxList, list, "bilabial plosive not working")
        
    def test_uvular_plosive(self): 
        list = [
            ConsonantModel('q', 'uvular', 'plosive', 'voiceless'), 
            ConsonantModel('ɢ', 'uvular', 'plosive', 'voiced'), 
            ConsonantModel('qʰ', 'uvular', 'plosive', 'aspirated'), 
            ConsonantModel('qʼ', 'uvular', 'plosive', 'ejective'), 
            ConsonantModel('ʛ', 'uvular', 'plosive', 'implosive')
        ]
        
        box = getBox('uvular', 'plosive')
        boxList = box.getModels()
        
        self.assertEqual(boxList, list, "uvular plosive not working")
        
    def test_glottal_plosive(self): 
        list = [
            ConsonantModel('ʔ', 'glottal', 'plosive', 'voiceless')
        ]
        
        box = getBox('glottal', 'plosive')
        boxList = box.getModels()
        
        self.assertEqual(boxList, list, "glottal plosive not working")
        
    def test_labio_dental_fricative(self): 
        list = [
            ConsonantModel('f', 'labio-dental', 'fricative', 'voiceless'), 
            ConsonantModel('v', 'labio-dental', 'fricative', 'voiced')
        ]
        
        box = getBox('labio-dental', 'fricative')
        boxList = box.getModels()
        
        self.assertEqual(boxList, list, "labio-dental fricatives not working")