import re

class InanimateIntransitive_Stemmer():
    def __init__(self):
        pass
         
    def stem(self, word: str, ctx: dict) -> str:
        if ctx['negative']:
            word = self._stem_negative(word)
        else:
            word = self._stem_indicative(word)
            
        if ctx['conjunct']:
            word = self._stem_conjunct(word)
        
        # Thereare no hints that I'm aware of to indicate dubitative other than suffix
        word = self._stem_dubitative(word)
        ## Check for party nipples
        #check for preterit
        
        
        return word
    
    def _stem_indicative(self, word: str) -> str:      
        if word.endswith('don'):
            word = word[:-3]
            if word.endswith('se'):
                word = word + 'n'
            elif word.endswith('me'):
                word = word + 't'
            elif word.endswith('n'):
                word = word + 'et'
            elif word.endswith('mge'):
                word = word + 't'
            
        if word.endswith('non'):
            word = word[:-3]
            if word.endswith('b'):
                word = word + 'en'
            elif word.endswith('de'):
                word = word[:-2] + 'et'
            elif word.endswith('es'):
                word = word + 'en'
            
        if word == 'bya':
            word = 'byé'
            
        return word
    
    def _stem_negative(self, word: str) -> str:
        if word.endswith('mgesnon'):
            word = word[:-4]
            if word.endswith('e'):
                word = word + 't'
                
        if word.endswith('snon'):
            word = word[:-4]
            if word.endswith('de'):
                word = word[:-2] + 'et'
                
        if word.endswith('senon'):
            word = word[:-5]
            if word.endswith('b'):
                word = word + 'en'
            elif word.endswith('n'):
                word = word + 'et'
                
        return word
    
    def _stem_conjunct(self, word: str) -> str:
        if word.endswith('k'):
            word = word[:-1]
            if word.endswith('se'):
                word = word + 'n'
            elif word.endswith('me') or word.endswith('mge'):
                word = word + 't'
            
        return word    
    
    def _stem_dubitative(self, word: str) -> str:
        # There is a challenge because we don't know what kind of stem this is (D Stem/N Stem) unless we do a lookup.
        if word.endswith('mgedek'):
            word = word[:-3] + 't'
            
        if word.endswith('odek'):
            word = word[:-4]
            if word.endswith('bn'):
                word = word + 'ben'
            
        if word.endswith('dek'):
            word = word[:-3]
            if word.endswith('n'):
                word = word + 'et'
            elif word.endswith('me'):
                word = word + 't'
        
        #if word.endswith('ndek') or word.endswith('nedek'):
            
        return word
    
    def _stem_preterit(self, word: str) -> str:
        pass
    
    def _stem_participle(self, word: str) -> str:
        pass
    