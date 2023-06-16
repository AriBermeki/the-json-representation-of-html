import asyncio
import inspect
import logging
from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Iterator, List, Optional, Union
from socketio import AsyncServer
from uvicorn import Server
from language import Language



class State(Enum):
    STOPPED = 0
    STARTING = 1
    STARTED = 2
    STOPPING = 3



sio: AsyncServer
server: Server
loop: Optional[asyncio.AbstractEventLoop] = None
log: logging.Logger = logging.getLogger('hybrid')
state: State = State.STOPPED
ui_run_has_been_called: bool = False

reload: bool
title: str
viewport: str
favicon: Optional[Union[str, Path]]
dark: Optional[bool]
language: Language
binding_refresh_interval: float
excludes: List[str]
tailwind: bool
socket_io_js_extra_headers: Dict = {}

_socket_id: Optional[str] = None

page_routes: Dict[Callable[..., Any], str] = {}

startup_handlers: List[Union[Callable[..., Any], Awaitable]] = []
shutdown_handlers: List[Union[Callable[..., Any], Awaitable]] = []
connect_handlers: List[Union[Callable[..., Any], Awaitable]] = []
disconnect_handlers: List[Union[Callable[..., Any], Awaitable]] = []
exception_handlers: List[Callable[..., Any]] = [log.exception]