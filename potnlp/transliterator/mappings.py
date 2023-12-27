from pathlib import Path
from operator import attrgetter
from enum import Enum
from typing import Tuple, List
from potnlp.transliterator.mapping import Mapping
import json

def _mapping_loader():
    return (Mapping.load(definition) for definition in _definition_reader())

def _definition_reader():
    mappings_path = Path(__file__).parent / "mappings"
    if not mappings_path.exists():
        raise ValueError(f"Mapping path does not exist: {mappings_path}")
    paths = mappings_path.glob("*.json")
    for path in paths:
        definition = _load_definition(path)
        yield definition
        
def _load_definition(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)
    
class _Mappings(Enum):
    
    @classmethod
    def names(cls) -> List[str]:
        return sorted(item.name for item in cls)
    
    @classmethod
    def items(cls) -> List[Tuple[str, Mapping]]:
        return [(item.name, item.value) for item in sorted(cls, key=attrgetter("value.name"))]
    
    @classmethod
    def get(cls, name: str) -> Mapping:
        item = cls.__members__.get(name)
        return item.value if item else None        
        
Mappings:dict = Enum(
    "Mappings", [(mapping.name, mapping) for mapping in _mapping_loader()], type=_Mappings
)