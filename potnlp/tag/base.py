from potnlp.tag.api import TaggerI
import re

class PotawatomiPOSTagger(TaggerI):
    def __init__(self, window_size=1):
        self.window_size = window_size
        self.rules = [
            (r".*o$", "DEM"),
            (r".*ing$", "VERB"),
            (r".*ly$", "ADV"),
            (r".*able$", "ADJ"),
            (r".*ful$", "ADJ"),
            (r".*ness$", "NOUN"),
            (r".*s$", "NOUN"),
        ]

    def tag(self, sentence):
        tagged_sentence = []

        # for i, word in enumerate(sentence):
        #     tagged_word = self.apply_rules(word, sentence, i)
        #     tagged_sentence.append(tagged_word)

        # return tagged_sentence

    def apply_rules(self, word, words, index):
        for rule, pos_tag in self.rules:
            if re.match(rule, word):
                context = self.get_context(words, index)
                if "da" in context:
                    pos_tag = "PV"  # Override as adverb if "not" is nearby
                return (word, pos_tag)
        return (word, "UNKNOWN")

    def get_context(self, words, index):
        start = max(0, index - self.window_size)
        end = min(len(words), index + self.window_size + 1)
        context = words[start:end]
        return context
        

# def preverbTagger(self, text: List) -> List:
    #     f = open('corpus/index.pv')
    #     pv = f.read()
    #     modified = []
    #     preverbs = [item.split("|") for item in pv.splitlines()]

    #     for i in range(len(text)):
    #         found = False
    #         for pv in preverbs:
    #             if text[i] == pv[0]:
    #                 found = True
    #                 match = pv[1]
    #                 break
    #             else:
    #                 found = False
                    
        
    #         if (found):
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
            
    #     return modified
    
    # def personMarkerTagger(self, text: List) -> List:
    #     # assumes it's already gone through PV tagger
    #     f = open('corpus/index.pn')
    #     pn = f.read()
    #     modified = []
    #     tense = ['gi', 'wi', 'de', 'da']
    #     pronoun = [item.split("|") for item in pn.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for pn in pronoun:      
    #             if (text[i] == pn[0]) and (text[i+1][0] in tense):
    #                 found = True
    #                 match = pn[1]
    #                 break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified

    # def emphasizerTagger(self, text: List) -> List:
    #     f = open('corpus/index.emph')
    #     e = f.read()
    #     modified = []
    #     tense = ['gi', 'wi', 'de', 'da', 'wa', 'ga']
    #     emph = [item.split("|") for item in e.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for e in emph:      
    #             if (text[i] == e[0]):
    #                 if text[i-1][0] not in tense:
    #                     found = True
    #                     match = e[1]
    #                     break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified

    # def demonstrativeTagger(self, text: List) -> List:
    #     f = open('corpus/index.dem')
    #     d = f.read()
    #     modified = []
    #     dem = [item.split("|") for item in d.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for d in dem:      
    #             if (text[i] == d[0]):
    #                 found = True
    #                 match = d[1]
    #                 break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified