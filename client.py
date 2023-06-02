import asyncio
import time
import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, List, Optional, Union

from fastapi import Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from .element import Element
from . import globals
import json

if TYPE_CHECKING:
    from .page import Page

templates = Jinja2Templates(Path(__file__).parent / 'templates')


class Client:

    def __init__(self, page: 'Page', *, shared: bool = False) -> None:
        self.id = str(uuid.uuid4())
        self.created = time.time()
        self.elements: Dict[int, Element] = {}
        self.next_element_id: int = 0
        self.is_waiting_for_connection: bool = False
        self.is_waiting_for_disconnect: bool = False
        self.environ: Optional[Dict[str, Any]] = None
        self.shared = shared

        with Element('div'):
                    self.content = Element('div')

        self.waiting_javascript_commands: Dict[str, str] = {}

        self.head_html = ''
        self.body_html = ''

        self.page = page

        self.connect_handlers: List[Union[Callable, Awaitable]] = []
        self.disconnect_handlers: List[Union[Callable, Awaitable]] = []

    @property
    def ip(self) -> Optional[str]:
        return self.environ.get('REMOTE_ADDR') if self.environ else None

    @property
    def has_socket_connection(self) -> bool:
        return self.environ is not None

    def __enter__(self):
        self.content.__enter__()
        return self

    def __exit__(self, *_):
        self.content.__exit__()

    def build_response(self, request: Request, status_code: int = 200) -> Response:
        prefix = request.headers.get('X-Forwarded-Prefix', '')

        elements = json.dumps({id: element.as_dict() for id, element in self.elements.items()})
        return templates.TemplateResponse('index.html', {
            'request': request,
            'client_id': str(self.id),
            'elements': elements,
            'head_html': self.head_html,
            'prefix': prefix,
            'viewport': globals.viewport,
            'tailwind': globals.tailwind,
            'socket_io_js_extra_headers': globals.socket_io_js_extra_headers,
        }, status_code, {'Cache-Control': 'no-store', 'X-NiceGUI-Content': 'Page'})

    async def connected(self, timeout: float = 3.0, check_interval: float = 0.1) -> None:
        '''Blocks execution until the client is connected.'''
        self.is_waiting_for_connection = True
        deadline = time.time() + timeout
        while not self.environ:
            if time.time() > deadline:
                raise TimeoutError(f'No connection after {timeout} seconds')
            await asyncio.sleep(check_interval)
        self.is_waiting_for_connection = False

    async def disconnected(self, check_interval: float = 0.1) -> None:
        '''Blocks execution until the client disconnects.'''
        return check_interval
       

    async def run_javascript(self, code: str, *,
                             respond: bool = True, timeout: float = 1.0, check_interval: float = 0.01) -> Optional[str]:
        '''Allows execution of javascript on the client.

        The client connection must be established before this method is called.
        You can do this by `await client.connected()` or register a callback with `client.on_connected(...)`.
        If respond is True, the javascript code must return a string.'''
        request_id = str(uuid.uuid4())
        command = {
            'code': code,
            'request_id': request_id if respond else None,
        }
  
        if not respond:
            return None
        deadline = time.time() + timeout
        while request_id not in self.waiting_javascript_commands:
            if time.time() > deadline:
                raise TimeoutError('JavaScript did not respond in time')
            await asyncio.sleep(check_interval)
        return self.waiting_javascript_commands.pop(request_id)

    def open(self, target: Union[Callable, str]) -> None:
        path = target if isinstance(target, str) else globals.page_routes[target]

    def on_connect(self, handler: Union[Callable, Awaitable]) -> None:
        self.connect_handlers.append(handler)

    def on_disconnect(self, handler: Union[Callable, Awaitable]) -> None:
        self.disconnect_handlers.append(handler)