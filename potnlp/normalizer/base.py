import re
import unicodedata

class DataNormalizer:
    def __init__(self, keep_extra_spaces=False):
        self.regex_rules = [
            (r' ́e', 'é'),
            (r'(ne\?’)', 'né'),
            (r'’', '\''),
            (r'\[.*?\]', ''),
            (r'[^\'\w\s.,-]', ''),
            (r'\n+', '\n'),
            #(r'[\t\n\r]+', ' '), // not sure if i want to store new lines or not
        ]
        self.keep_extra_spaces = keep_extra_spaces or False
        
    def add_regex_rule(self, pattern: str, replacement: str):
        self.regex_rules.append((pattern, replacement))
        
    def apply_regex_rules(self, text: str) -> str:
        for pattern, replacement in self.regex_rules:
            text = re.sub(pattern=pattern, repl=replacement, string=text)
        return text
    
    def lowercase(self, text: str) -> str:
        return text.lower()
    
    def remove_extra_whitespace(self, text: str) -> str:
        return re.sub(r'\s+', ' ', text).strip()
    
    def uniform_unicode(self, text: str) -> str:
        text = unicodedata.normalize('NFC', text)
        return ''.join([char for char in text if not unicodedata.combining(char)])
    
    
    def normalize(self, text: str) -> str:
        text = self.apply_regex_rules(text)
        text = self.lowercase(text)

        if not self.keep_extra_spaces:
            text = self.remove_extra_whitespace(text)
        text = self.uniform_unicode(text)
        return text