import re

class CorpusReader:
    def __init__(self):
        pass

    def get(self, file):
        modified = []
        with open(file, "r") as file:
            for line in file:
                modified.append(re.sub(r'[\/-]', '', line.strip('\n')))
        return modified
    