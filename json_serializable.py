from dataclasses import dataclass, field, asdict, fields
from typing import Any, Dict, Type, TypeVar
import json

T = TypeVar('T', bound='JsonSerializable')

@dataclass(kw_only=True)
class JsonSerializable:
    extra: Dict[str, Any] = field(default_factory=dict, repr=False)

    def to_json(self) -> str:
        base_dict = asdict(self)
        combined = {**base_dict.pop('extra', {}), **base_dict}
        return json.dumps(combined, indent=2)

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        data = json.loads(json_str)
        field_names = {f.name for f in fields(cls)}
        known = {k: v for k, v in data.items() if k in field_names}
        extra = {k: v for k, v in data.items() if k not in field_names}
        return cls(**known, extra=extra)

    @classmethod
    def from_json_file(cls: Type[T], file_path: str) -> T:
        with open(file_path, 'r', encoding='utf-8') as f:
            return cls.from_json(f.read())
        
    def save(self, file_path: str) -> str:
        with open(file_path, "w") as f:
            f.write(self.to_json())