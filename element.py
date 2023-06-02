import uuid
import json

class Element:
    """The base class of all page elements"""

    # Klassenvariable zur Speicherung der Element-Objekte
    all_elements = []

    def __init__(self, type_, content=None, id=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.uuid = str(uuid.uuid1())
        self.component = type_
        self.id = id
        self.content = content

        # Hinzufügen des aktuellen Objekts zur Liste aller Elemente
        

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def as_dict(self):
        return {x: self.__dict__[x] for x in self.__dict__ if self.__dict__[x] is not None}

