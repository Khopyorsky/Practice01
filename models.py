from dataclasses import dataclass, field, fields
from datetime import datetime
import json


@dataclass
class User:
    first_name: str
    last_name: str
    age: int
    password: str
    created_at: datetime = field(default_factory=datetime.now, init=False, )
    updated_at: datetime | None = field(default=None, init=False)
    _initialized: bool = field(default=False, init=False, repr=False)

    def __post_init__(self):
        self._initialized = True

    def __setattr__(self, key, value):

        if key not in [fld.name for fld in fields(self)]:
            raise AttributeError(f"Couldn't assign new attributes to {self.__class__.__name__} instance")

        required_type = None

        for fld in fields(self):
            if fld.name == key:
                required_type = fld.type
        if required_type != type(value):
            raise AttributeError(f"<{key}> attribute must be {required_type.__name__}")

        if not self._initialized:
            super().__setattr__(key, value)
        else:
            if key.startswith('_') or key.endswith('_at'):
                raise ValueError(f"Couldn't change <{key}> attribute")
            super().__setattr__(key, value)
            super().__setattr__('updated_at', datetime.now())

    def _to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'password': self.password,
            'created_at': {
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day
            },
            'updated_at': {
                'year': self.updated_at.year,
                'month': self.updated_at.month,
                'day': self.updated_at.day
            } if self.updated_at else None
        }

    def save(self):
        dict_obj = self._to_dict()
        file_path = 'user.json'
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_obj, file, indent=3)

    @staticmethod
    def signalize():
        print('User has been created')
