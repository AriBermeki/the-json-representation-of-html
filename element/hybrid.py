from fastapi import FastAPI
from fastapi_socketio import SocketManager
from socketio import AsyncServer
import json
from typing import Dict, List, Optional
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import urllib.parse
from pathlib import Path
from typing import Dict, Optional
from fastapi import HTTPException, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi_socketio import SocketManager


app = FastAPI()
socketio = AsyncServer(async_mode='asgi')
socket_manager = SocketManager(app=app, mount_location='/_myapp_ws/', json=json)
socket_manager._sio



app.add_middleware(GZipMiddleware)
static_files = StaticFiles(
    directory=(Path(__file__).parent / 'static').resolve(),
    follow_symlink=True,
)
app.mount(f'/_myapp/static', static_files, name='static')
        
# Initialisierung des Templates-Folders
templates = Jinja2Templates(directory="templates")
        
# GET-Endpoint
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    prefix = request.headers.get('X-Forwarded-Prefix', request.scope.get('root_path', ''))
    socket_io_js_extra_headers: Dict = {}
    context = {
        "request": request,
        "title": 'Hybrid',
        "socket_io_js_extra_headers":socket_io_js_extra_headers,
        "prefix":prefix,
        "client_id": 1
        }
    return templates.TemplateResponse('main.html', context=context)
# Definiere die Routen für die Socket.IO-Verbindung



@socketio.on('handshake')
def handle_handshake(sid: str, ok: str) -> bool:
    return True

@socketio.on('msseagesys')
async def connect(sid, environ):
    print(f'Client {sid} connected')
    await socketio.emit('message', {'text': 'Welcome!', 'author': 'Server'}, room=sid)
    
@socketio.on('message')
async def message(sid, data) -> Dict:
    print(f'Received message: {data}')
    await socketio.emit('message', data, room=sid)


@socketio.on('event')
def handle_event(sid: str, msg: Dict) -> None:
    print(msg)





@socketio.on('disconnect')
async def disconnect(sid):
    print(f'Client {sid} disconnected')

# Definiere eine FastAPI-Route, die die Socket.IO-Verbindung verarbeitet


# Beispiel-Endpunkt für FastAPI
@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn

    # Starte den Server
    uvicorn.run(app, host="0.0.0.0", port=8000)
