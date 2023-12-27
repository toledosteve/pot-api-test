from typing import List
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize.api import TokenizerI
import re

class PotawatomiTokenizer(TokenizerI):
    def tokenize(self, text: str) -> List[str]:
        CONJUNCT_PREVERB_COMBO = r'(?<!\w)(é|ga|wa|da)(gi|wi|je|tso|tse|dso|shkwa|che|pich|pit)(?!\w)'
        INDEPENDENT_PREVERB_COMBO = r'(?<!\w)(n|g|w)(gi|wi|de|da|dagi)(?!\w)'
        OTHER_PREVERB_COMBO = r'(?<!\w)(bwa)(mshé)'
        text = re.sub(CONJUNCT_PREVERB_COMBO, r'\1\2', text)
        text = re.sub(INDEPENDENT_PREVERB_COMBO, r'\1\2', text)
        text = re.sub(OTHER_PREVERB_COMBO, r'\1 \2', text)
        text = SpaceTokenizer().tokenize(text)
        return text
    

        