import re
from typing import List
from potnlp.stem.vii import InanimateIntransitive_Stemmer

class PotawatomiLemmatizer():
    def __init__(self):
        self._vowels = "aeéio"
        #(?<=\b(wa|ga|é|éwi|égi)\s)(\w+\s)*\w+(yan|yen|t|net|ygo|yak|yék|wat)\b
        
    # def _end_in_vowel(self, word: str) -> bool:
    #     if word:
    #         return word[-1] in self._vowels
    #     return False
    
    def _check_condition(self, regex: str, sentence: List, index: int, max_depth: int) -> int:
        if index < 0 or index < max_depth:
            return False
    
        match = re.search(regex, sentence[index])
        if match:
            return True
        
        return self._check_condition(regex=regex, sentence=sentence, index=index-1, max_depth=max_depth)
       
    # def _stem_animate_intransitive(self, sentence: str, target_word: str) -> str:
    #     pass
    #     # Step 1 - Determine which mode
        
    #     # Step 2 - Strip
    #     # AI Conjunct Verbs
    #     v_stem_suffixes = sorted(["an", "en", "t", "net", "go", "ak", "ék", "wat"], key=len, reverse=True)

    #     if target_word.endswith('m'):
    #         v_stem_suffixes = [suffix[:-1] + 'k' if suffix == 't' else suffix for suffix in v_stem_suffixes]
    #     else:
    #         v_stem_suffixes = [('y' + suffix) if suffix not in ['t', 'wat', 'net'] else suffix for suffix in v_stem_suffixes]
            
    #     print(v_stem_suffixes)
        
    #     i = 0
    #     lastFoundIdx = 0
    #     is_verb = False
    #     for w in sentence:
    #         for suffix in v_stem_suffixes:
    #             if w.endswith(suffix):
    #                 if self._is_conjunct(sentence=sentence, index=i, max_depth=lastFoundIdx):
    #                     lastFoundIdx = i
    #                     is_verb = True
    #                     break;
    #                 else:
    #                     break;
    #         i += 1
            
    #     if (is_verb):
    #         pattern = rf"{'|'.join(map(re.escape, v_stem_suffixes))}"
    #         return re.sub(pattern=pattern, repl=r'', string=target_word)
        
    #     return False
    
    def lemmatize(self, tokens: List, token: str):
        word = token.lower()
        wlen = len(token)
        
        if wlen <= 2:
            return token

        foundIdx = [idx for idx, w in enumerate(tokens) if w == word]
        
        if foundIdx:
            vii = InanimateIntransitive_Stemmer()
            # Look for context hints
            conjunct_ctx = self._check_condition(regex=r'^(ga|wa|éwi|égi|é|jé|gishpen)$', sentence=tokens, index=foundIdx[0], max_depth=0)
            negative_ctx = self._check_condition(regex=r'^(cho)$', sentence=tokens, index=foundIdx[0], max_depth=0)
            #ind_long_form_ctx = self._check_condition(regex=r'(?<!\w)(n|g|w)(gi|wi|de|da|dagi)(?!\w)', sentence=tokens, index=foundIdx[0], max_depth=0)
            prohibitive_ctx = self._check_condition(regex=r'^(gégo)$', sentence=tokens, index=foundIdx[0], max_depth=0)
            ## Short form will have to be figured out separately since there's some complexity involved
            
            context = {
                "conjunct": conjunct_ctx,
                "negative": negative_ctx,
                "prohibitive": prohibitive_ctx
            }
            
            return vii.stem(word, context)
            
            #print(is_conjunct)
            #return tokens[:int(foundIdx[0])+2]
            # lemma = self._stem_animate_intransitive(sentence=tokens[:int(foundIdx[0])+2], target_word=word)
            # if lemma:
            #     if self._end_in_vowel(lemma):
            #         return lemma
            #     else:
            #         return lemma+"e"
                    
                    
        

            
            
        