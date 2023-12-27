class InanimateIntransitive_Stemmer():
    def is_potential_vii_ending(self, word: str) -> str:
        word = self.step1_negative(word)
        word = self.step2_indicative(word)
        
        return word
    
    def step2_indicative(self, word: str) -> str:
        if word.endswith('mgedon'):
            word = word[:-3]+'t'
            
        if word.endswith('don'):
            word = word[:-3]
            if word.endswith('e'):
                word = word + 't'
            
        if word.endswith('non'):
            word = word[:-3]
            
        if word[-2:] == 'se':
            word = word + 'n'
            
        if word[-2:] == 'es':
            word = word + 'en'
            
        if word == 'bya':
            word = 'byé'
            
        return word
    
    def step1_negative(self, word: str) -> str:
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
    