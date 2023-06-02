import asyncio
import os
import time
import urllib.parse
from pathlib import Path
from typing import Dict, Optional
from fastapi import HTTPException, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, Response,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_socketio import SocketManager
import json
from .page import Page
from . import globals
from .app import App
from .client import Client
from fastapi import Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from .element import Element


globals.app = app = App(default_response_class=json)
# NOTE we use custom json module which wraps orjson
socket_manager = SocketManager(app=app, mount_location='/_hybrid_ws/', json=json)
globals.sio = sio = app.sio
templates = Jinja2Templates(Path(__file__).parent / 'templates')
app.add_middleware(GZipMiddleware)
app.mount(f'/_hybrid/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')
globals.index_client = Client(Page('/'), shared=True).__enter__()



@app.get('/')
async def index(request: Request,status_code=200) -> Response:
    prefix = request.headers.get('X-Forwarded-Prefix', '')
    element = Element.all_elements
 

    return templates.TemplateResponse('index.html', {
            'request': request,
            'elements': element,
            'prefix': prefix,
            'title':'Hybrid'
    }, status_code, {'Cache-Control': 'no-store', 'X-NiceGUI-Content': 'Page'})






@app.on_event('startup')
def handle_startup(with_welcome_message: bool = True) -> None:
    if not globals.ui_run_has_been_called:
        raise RuntimeError('\n\n'
                           'You must call ui.run() to start the server.\n'
                           'If ui.run() is behind a main guard\n'
                           '   if __name__ == "__main__":\n'
                           'remove the guard or replace it with\n'
                           '   if __name__ in {"__main__", "__mp_main__"}:\n'
                           'to allow for multiprocessing.')
    globals.state = globals.State.STARTING
    globals.loop = asyncio.get_running_loop()
    globals.state = globals.State.STARTED
    if with_welcome_message:
        print(f'NiceGUI ready to go on http://{globals.host}:{globals.port}')


@app.on_event('shutdown')
def handle_shutdown() -> None:
    globals.state = globals.State.STOPPING
    globals.state = globals.State.STOPPED







@sio.on('handshake')
def handle_handshake(sid: str) -> bool:
    client = get_client(sid)
    if not client:
        return False
    client.environ = sio.get_environ(sid)
    sio.enter_room(sid, client.id)
    for t in client.connect_handlers:
        (t, client)
    for t in globals.connect_handlers:
        (t, client)
    return True


@sio.on('disconnect')
def handle_disconnect(sid: str) -> None:
    client = get_client(sid)
    if not client:
        return



@sio.on('event')
def handle_event(sid: str, msg: Dict) -> None:
    client = get_client(sid)
    if not client or not client.has_socket_connection:
        return
    with client:
        sender = client.elements.get(msg['id'])
        if sender:
            sender._handle_event(msg)


@sio.on('javascript_response')
def handle_javascript_response(sid: str, msg: Dict) -> None:
    client = get_client(sid)
    if not client:
        return
    client.waiting_javascript_commands[msg['request_id']] = msg['result']


def get_client(sid: str) -> Optional[Client]:
    query_bytes: bytearray = sio.get_environ(sid)['asgi.scope']['query_string']
    query = urllib.parse.parse_qs(query_bytes.decode())
    client_id = query['client_id'][0] #globals.clients.get(client_id)
    return client_id


