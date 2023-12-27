from abc import ABC, abstractmethod
from typing import List

class TaggerI(ABC):
    @abstractmethod
    def tag(self, tokens: List):
        raise NotImplementedError()