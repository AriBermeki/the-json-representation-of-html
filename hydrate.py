from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_socketio import SocketManager
from pathlib import Path
from typing import Dict
import json
from base import ElementProtokoll,  callbackRegistry
import globals
import uvicorn
from page import Page
import threading
import webbrowser
from uvicorn import Config, Server
from pathlib import Path
from typing import Any, List, Optional, Tuple, Union
from language import Language

class UI:
    def __init__(
        self, 
        layout: ElementProtokoll = None,
        host: Optional[str] = '0.0.0.0', 
        port: int = 8080,
        title: str = 'Hybrid',
        viewport: str = 'width=device-width, initial-scale=1',
        favicon: Optional[Union[str, Path]] = 'favicon,icon',
        dark: Optional[bool] = False,
        language: Language = 'en-US',
        binding_refresh_interval: float = 0.1,
        view: str = 'web',
        window_size: Optional[Tuple[int, int]] = None,
        fullscreen: bool = False,
        reload: bool = True,
        uvicorn_logging_level: str = 'warning',
        uvicorn_reload_dirs: str = '.',
        uvicorn_reload_includes: str = '*.py',
        uvicorn_reload_excludes: str = '.*, .py[cod], .sw.*, ~*',
        exclude: str = '',
        tailwind: bool = True,
        storage_secret: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self.app = globals.app =FastAPI()
        self.templates = Jinja2Templates(Path(__file__).parent / 'templates')
        self.socket_manager = SocketManager(app=self.app, mount_location='/_hybrid_ws/', json=json)
        self.sio = self.socket_manager._sio
        self.app.add_middleware(GZipMiddleware)
        self.app.mount('/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')
        self.page_router = Page()
        self.socket_extra_headers: Dict[str, Any] = {}
        self.title = title
        self.host = host
        self.port = port
        self.viewport = viewport
        self.favicon = favicon
        self.dark = dark
        self.language = language
        self.binding_refresh_interval = binding_refresh_interval
        self.view = view
        self.window_size = window_size
        self.fullscreen = fullscreen
        self.uvicorn_logging_level = uvicorn_logging_level
        self.uvicorn_reload_dirs = uvicorn_reload_dirs
        self.uvicorn_reload_includes = uvicorn_reload_includes
        self.uvicorn_reload_excludes = uvicorn_reload_excludes
        self.exclude = exclude
        self.tailwind = tailwind
        self.reload = reload
        self.storage_secret = storage_secret
        self.app_settings = 'globals:app'
        self.layout = layout
    


        @self.app.get('/')
        async def index(request: Request, status_code: int = 200, response_class=HTMLResponse)->Response:
            self.app.include_router(self.page_router)
            prefix = request.headers.get('X-Forwarded-Prefix', request.scope.get('root_path', ''))
       
            print(self.layout.to_json())
           
            return self.templates.TemplateResponse('index.html', {
                'request': request,
                'prefix': prefix,
                'viewport':self.viewport,
                'title':self.title,
                'client_id': 1,
                'elements': self.layout.to_json(),
                'favicon': self.favicon,
                'socket_io_js_extra_headers': self.socket_extra_headers,
            }, status_code, {'Cache-Control': 'no-store', 'X-NiceGUI-Content': 'page'})

        @self.sio.on("handshake")
        async def connect(sid):
            print(f"Client {sid} connected")
            return 'ok'

        @self.sio.on("disconnect")
        async def disconnect(sid):
            print(f"Client {sid} disconnected")

        @self.sio.on("message")
        async def received_message(sid: str, data: Dict) -> None:
            print(f"Received message from client {sid}: {data}")
            await self.socket_manager.emit("response", f"Received your message: {data}", to=sid)

        @self.sio.on("base_event")
        async def handle_event(sid: str, msg: Dict) -> None:
            print(f"Received message from client {sid}: {msg}")
            print(msg['message'])
            
            if 'callback_uuid' in msg and 'args' in msg:
                if msg['callback_uuid'] and msg['args'] is not None:
                    callbackRegistry.make_callback(msg['callback_uuid'], msg['args'])
                elif msg['callback_uuid'] is not None:
                    callbackRegistry.make_callback(msg['callback_uuid'])
            else:
                # Handhabung, wenn 'callback_uuid' oder 'args' nicht im 'msg'-Dictionary vorhanden sind

                
                print(msg)

        @self.app.get("/")
        async def read_root():
            return {"Hello": "World"}

    def run(self):
        # Starten Sie den Uvicorn-Server in einem separaten Thread
        server_thread = threading.Thread(target=self._start_server)
        server_thread.start()

        # Öffnen Sie den Webbrowser zum angegebenen Host und Port
        url = f"http://{self.host}:{self.port}"
        webbrowser.open(url)

    def split_args(self, args: str) -> List[str]:
        return [a.strip() for a in args.split(',')]


    def _start_server(self):
        # Konfigurieren und starten Sie den Uvicorn-Server
        config = Config(
            self.app_settings,
            host=self.host,
            port=self.port,
            reload=self.reload,
            reload_includes=self.split_args(self.uvicorn_reload_includes) if self.reload else None,
            reload_excludes=self.split_args(self.uvicorn_reload_excludes) if self.reload else None,
            reload_dirs=self.split_args(self.uvicorn_reload_dirs) if self.reload else None,
            log_level=self.uvicorn_logging_level,
        )
        config.storage_secret = self.storage_secret
        Server(config)
        server = Server(config)
        server.run()

if __name__ == "__main__":
    ui = UI()
    ui.run()
