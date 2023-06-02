import asyncio
import logging
from contextlib import contextmanager
from enum import Enum
from typing import TYPE_CHECKING, Awaitable, Callable, Dict, List, Optional, Union

from socketio import AsyncServer
from uvicorn import Server

from hybrid.app import App
if TYPE_CHECKING:
    from .client import Client


class State(Enum):
    STOPPED = 0
    STARTING = 1
    STARTED = 2
    STOPPING = 3

app: App
sio: AsyncServer
server: Server
loop: Optional[asyncio.AbstractEventLoop] = None
log: logging.Logger = logging.getLogger('hybrid')
state: State = State.STOPPED
ui_run_has_been_called: bool = False
index_client: 'Client'
host: str
port: int
reload: bool
title: str
viewport: str
favicon: Optional[str]
dark: Optional[bool]
binding_refresh_interval: float
excludes: List[str]
tailwind: bool
socket_io_js_extra_headers: Dict = {}
_socket_id: Optional[str] = None
page_routes: Dict[Callable, str] = {}
startup_handlers: List[Union[Callable, Awaitable]] = []
shutdown_handlers: List[Union[Callable, Awaitable]] = []
connect_handlers: List[Union[Callable, Awaitable]] = []
disconnect_handlers: List[Union[Callable, Awaitable]] = []

