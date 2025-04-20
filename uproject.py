# from dataclasses import dataclass, field, asdict
# import json
# from typing import List, Any, Dict

from dataclasses import dataclass
from typing import List

from json_serializable import JsonSerializable



@dataclass
class Module:
    Name: str
    Type: str
    LoadingPhase: str

    
    def __init__(
        self, 
        Name, 
        Type="Runtime", 
        LoadingPhase = "Default"
    ):
        self.Name = Name
        self.Type = Type
        self.LoadingPhase = LoadingPhase



@dataclass
class UProject(JsonSerializable):

    #FileVersion: str
    #EngineAssociation: str
    #Category: str
    #Description: str
    Modules: List[Module]

    def add_module(self, module_name: str):
        self.Modules.append(Module(Name=module_name))