import uuid
import json


class Element:
    def __init__(self, tag, properties=None, attributes=None, eventListeners=None, content=None):
        self._tag = tag
        self._properties = properties or {}
        self._attributes = attributes or {}
        self._eventListeners = eventListeners or {}
        self._content =  content

    @property
    def tag(self):
        return self._tag

    @property
    def properties(self):
        return self._properties

    @property
    def attributes(self):
        return self._attributes

    @property
    def eventListeners(self):
        return self._eventListeners

    @property
    def content(self):
        return self._content

    def to_json(self):
        data = {
            "tag": self.tag,
            "properties": self.properties,
            "attributes": self.attributes,
            "eventListeners": self.eventListeners,
            "content":None
        }

        if isinstance(self.content, Element):
            data["content"] = self.content.to_json()
        else:
            data["content"] = self.content

        return data




elemnt = Element(
    tag="div",
    properties={
        "id": "content",
        "class": "content-class",
        "style": "background-color: blue; color: white;"
    },
    attributes={
        "data-action": "submit"
    },
    eventListeners={
        "eventType": "copy",
        "eventArgs": "console.log(event)",
        "elementId": "myButton",
        "callbackUuid": "iafsifoeipjeofw",
        "sendToServer": True
    },
    content=Element(
        tag="button",
        properties={
            "id": "myButton",
            "class": "btn",
            "style": "background-color: blue; color: white;"
        },
        attributes={
            "data-action": "submit"
        },
        eventListeners={
            "eventType": "click",
            "eventArgs": "console.log(event)",
            "elementId": "myButton",
            "callbackUuid": "iafsifoeipjeofw",
            "sendToServer": True
        },
        content="Click me!"
    )
)

json_data = elemnt.to_json()
json_str = json.dumps(json_data, indent=4)
print(json_str)
