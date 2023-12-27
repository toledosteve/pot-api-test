from typing import Dict, List
from typing import List

class MappingDefinition:
    def __init__(self, source: dict):
        self.source = source
        self.name = ""
        self.description = ""
        self.map: Dict[str, str] = {}
        self.orthography_rules: List[str] = []
        
    def parse(self):
        self._parse("name", type=str, required=True, nonempty=True)
        self._parse("description", type=str, required=False)
        self._parse("map", type=dict, required=True)
        self._parse("orthography_rules", type=list, required=False)
        
    def _parse(self, name, type, required, nonempty=False):
        value = self.source.get(name)
        if required and value is None:
            raise ValueError(f"{self.name}: Missing map attribute {name}")
        if required and nonempty and not value:
            raise ValueError(f"{self.name}: Map {name} should not be empty")
        if value is not None and not isinstance(value, type):
            raise ValueError(f"{self.name}: Invalid map {name}: {value}")
        setattr(self, name, value)
  
class Mapping:
    def __init__(
        self,
        name: str,
        map: Dict[str, str],
        rules: List[str] = None,
        description: str = None,
    ):
        self.name = name
        self.description = description
        self.map = map
        self.rules = rules
    
    @classmethod
    def load(cls, definition: dict):
        definition = MappingDefinition(definition)
        definition.parse()
        return Mapping(
            name=definition.name,
            description=definition.description,
            map=definition.map,
            rules=definition.orthography_rules
        )
