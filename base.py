from inspect import signature 
from distutils.command.upload import upload
import uuid
import inspect
import os
import time
from pathlib import Path
from inspect import signature
from cgitb import reset
from faulthandler import disable
import json
from typing import Dict, Any, Union
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING




class CallbackRegistryType:
    uuid_callback_map = {}
    callback_uuid_map = {}

    def uuid_for_callback(self, callback):
        if callback is None:
            return None
        if callback in self.callback_uuid_map:
            return self.callback_uuid_map[callback]
        else:
            cb_uuid = str(uuid.uuid1())
            self.uuid_callback_map[cb_uuid] = callback
            self.callback_uuid_map[callback] = cb_uuid
            return cb_uuid

    def make_callback(self, uuid, *args):
        if uuid in self.uuid_callback_map:
            method = self.uuid_callback_map[uuid]
            param_length = len(signature(method).parameters)
            return method(*args[:param_length])
        else:
            # TODO: Return an error to the frontend
            return None

callbackRegistry = CallbackRegistryType()


class ElementProtokoll:
    def __init__(self):
        self.json_data = {}

    def add_tag(self, tag: str, attributes: Dict[str, Union[str, int]] = None, content: Union[str, List["ElementProtokoll"]] = None):
        tag_data = {}
        if attributes:
            tag_data['attributes'] = attributes
        if content:
            if isinstance(content, str):
                tag_data['content'] = content
            elif isinstance(content, list):
                tag_data['content'] = [item.json_data for item in content]

        if tag in self.json_data:
            if isinstance(self.json_data[tag], list):
                self.json_data[tag].append(tag_data)
            else:
                self.json_data[tag] = [self.json_data[tag], tag_data]
        else:
            self.json_data[tag] = tag_data

    def to_json(self)-> Dict[str, Any]:
        return json.dumps(self.json_data)

    
    
    def delete(self) -> None:
            """Called when the corresponding client is deleted.

            Can be overridden to perform cleanup.
            """








