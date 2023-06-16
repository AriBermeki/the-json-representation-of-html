import json
from typing import Any, Callable, Dict, List, Optional, Union
from base import ElementProtokoll, callbackRegistry




class Big(ElementProtokoll):
    def __init__(
            self, 
            data_action: Optional[Any] = None, 
            integrated: Optional[Any] = None, 
            accesskey: Optional[Any] = None, 
            className: Optional[Any] = None, 
            contenteditable: Optional[Any] = None, 
            data_custom: Optional[Dict[str, Any]] = None, 
            direction: Optional[Any] = None,
            draggable: Optional[Any] = None, 
            hidden: Optional[Any] = None, 
            element_id: Optional[Any] = None, 
            lang: Optional[Any] = None, 
            spellcheck: Optional[Any] = None, 
            style: Optional[Any] = None, 
            tabindex: Optional[Any] = None, 
            title: Optional[Any] = None, 
            translate: Optional[Any] = None, 
            content: Optional[List['ElementProtokoll']] = None
        ):
        class_name = str(self.__class__.__name__.lower())

        super().__init__()

        attributes = {}
        if data_action:
            attributes['data-action'] = data_action
        if integrated:
            attributes['integrated'] = integrated
        if accesskey:
            attributes['accesskey'] = accesskey
        if className:
            attributes['class'] = className
        if contenteditable:
            attributes['contenteditable'] = contenteditable
        if data_custom:
            attributes.update(data_custom)
        if direction:
            attributes['dir'] = direction
        if draggable:
            attributes['draggable'] = draggable
        if hidden:
            attributes['hidden'] = hidden
        if element_id:
            attributes['id'] = element_id
        if lang:
            attributes['lang'] = lang
        if spellcheck:
            attributes['spellcheck'] = spellcheck
        if style:
            attributes['style'] = style
        if tabindex:
            attributes['tabindex'] = tabindex
        if title:
            attributes['title'] = title
        if translate:
            attributes['translate'] = translate

        self.add_tag(class_name, attributes, content)