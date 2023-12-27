# transliterator.py
from potnlp.transliterator.api import TransliteratorI
import re
import unicodedata

class Transliterator(TransliteratorI):
    def __init__(self, mapping:dict, pre_process=None, post_process=None):
        self.mapping = mapping
        self.pre_process_function = pre_process
        self.post_process_function = post_process

    def transliterate(self, text: str):
        # sometimes characters such as ë will separate out the double dot and the e as two separate unicode chars
        text = unicodedata.normalize('NFC', text)

        # strip out leading and trailing spaces
        text = text.strip()
                
        if self.pre_process_function:
            text = self.pre_process_function(text)
        
        text = (self._process_word(word, self.mapping) for word in self._split_sentence(text))
        
        # convert to string again
        text = "".join(text)

        for rule in self.mapping.rules:
            pattern, replacement = rule
            text = re.sub(pattern, replacement, text)
        
        if self.post_process_function:
            text = self.post_process_function(text)
            
        return "".join(text)
    
    def _split_sentence(self, sentence: str):
        return (word for word in re.compile(r"\b").split(sentence) if word)
    
    def _process_word(self, word: str, mapping):
        text = self._process_letters(word, mapping)
        return "".join(text)
    
    def _process_letters(self, word, mapping):
        text = []
        i = 0
        while i < len(word):
            seq_found = False

            # Sort sequences by length (longest first) and check for matches
            for seq in sorted(mapping.map.keys(), key=len, reverse=True):
                if word[i:i+len(seq)].lower() == seq:
                    text.append(mapping.map[seq])
                    i += len(seq)
                    seq_found = True
                    break

            if not seq_found:
                text.append(word[i])
                i += 1

        return text
    
