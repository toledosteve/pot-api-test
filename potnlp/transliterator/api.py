from abc import ABC, abstractmethod

class TransliteratorI(ABC):
    @abstractmethod
    def transliterate(self, text: str):
        raise NotImplementedError()
    