class PhonemeBox(): 
    def __init__(self, place, manner, voiceless, voiced, others={}): 
        self.place = place
        self.manner = manner
        self.voiced = voiced
        self.voiceless = voiceless
        self.others = others
        
    def getPrenasal(self): 
        if not(self.voiced): 
            return False
        nasal = getNasal(self.place)
        superscripts = {'m': 'ᵐ', 'n': 'ⁿ', 'ɳ': 'ᶯ', 'ɲ': 'ᶮ', 'ŋ': 'ᵑ', '͡': '͡'}
        superscriptNasal = ''
        for sound in nasal: 
            if sound in superscripts: 
                superscriptNasal += superscripts[sound]
            else: 
                return False
        return superscriptNasal + self.voiced
        
    def getEjective(self): 
        return self.voiceless + 'ʼ'
        
    def getAspirated(self): 
        return self.voiceless + 'ʰ'
        
    def getImplosive(self): 
        if 'implosive' in self.others: 
            return self.others['implosive']
        return False
        
    def getModels(self): 
        list = [ConsonantModel(self.voiceless, self.place, self.manner, "voiceless")]
        if self.voiced: 
            list += [ConsonantModel(self.voiced, self.place, self.manner, "voiced")]
        if self.manner == "plosive" and self.place not in ["pharyngeal", "glottal"]: 
            list += [ConsonantModel(self.getAspirated(), self.place, self.manner, "aspirated")]
            list += [ConsonantModel(self.getEjective(), self.place, self.manner, "ejective")]
            prenasal = self.getPrenasal()
            if prenasal: 
                list += [ConsonantModel(prenasal, self.place, self.manner, "prenasal")]
            implosive = self.getImplosive()
            if implosive: 
                list += [ConsonantModel(implosive, self.place, self.manner, "implosive")]
        return list
        
consonants = [
    PhonemeBox('bilabial', 'nasal', 'm̥', 'm'), 
    PhonemeBox('labio-dental', 'nasal', 'ɱ̊', 'ɱ'), 
    PhonemeBox('alveolar', 'nasal', 'n̥', 'n'), 
    PhonemeBox('retroflex', 'nasal', 'ɳ̊', 'ɳ'), 
    PhonemeBox('palatal', 'nasal', 'ɲ̊', 'ɲ'), 
    PhonemeBox('velar', 'nasal', 'ŋ̊', 'ŋ'), 
    PhonemeBox('uvular', 'nasal', 'ɴ̥', 'ɴ'), 
    PhonemeBox('bilabial', 'plosive', 'p', 'b', {'implosive': 'ɓ'}), 
    PhonemeBox('alveolar', 'plosive', 't', 'd', {'implosive': 'ɗ'}), 
    PhonemeBox('retroflex', 'plosive', 'ʈ', 'ɖ'), 
    PhonemeBox('palatal', 'plosive', 'c', 'ɟ', {'implosive': 'ʄ'}), 
    PhonemeBox('velar', 'plosive', 'k', 'g', {'implosive': 'ɠ'}), 
    PhonemeBox('uvular', 'plosive', 'q', 'ɢ', {'implosive': 'ʛ'}), 
    PhonemeBox('pharyngeal', 'plosive', 'ʡ', False), 
    PhonemeBox('glottal', 'plosive', 'ʔ', False), 
    PhonemeBox('bilabial', 'fricative', 'ɸ', 'β'), 
    PhonemeBox('labio-dental', 'fricative', 'f', 'v'), 
    PhonemeBox('alveolar', 'fricative', 's', 'z'), 
    PhonemeBox('retroflex', 'fricative', 'ʂ', 'ʐ'), 
    PhonemeBox('palatal', 'fricative', 'ç', 'ʝ'), 
    PhonemeBox('velar', 'fricative', 'x', 'ɣ'), 
    PhonemeBox('uvular', 'fricative', 'χ', 'ʁ'), 
    PhonemeBox('pharyngeal', 'fricative', 'ħ', 'ʕ')
]

places = []
manners = []
for box in consonants:
    if box.place not in places:
        places.append(box.place)
    if box.manner not in manners:
        manners.append(box.manner)


def getBox(place, manner): 
    return [box for box in consonants if box.place == place and box.manner == manner][0]
    
def getNasal(place): 
    return getBox(place, 'nasal').voiced
    
class ConsonantModel(): 
    def __init__(self, symbol, place, manner, phonation, articulations={}): 
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.phonation = phonation
        self.articulations = articulations
        
    def __eq__(self, other): 
        return (self.symbol, self.place, self.manner, self.phonation, self.articulations) == (other.symbol, other.place, other.manner, other.phonation, other.articulations)
                
if __name__ == "__main__": 
    for box in consonants: 
        print(box.place, box.manner, box.voiceless, box.voiced, box.others)
        list = box.getModels()
        for model in list: 
            print(model.symbol, model.place, model.manner, model.phonation)