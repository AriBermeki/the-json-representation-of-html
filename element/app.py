from typing import Dict, List, Optional
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import webbrowser
from socketio import AsyncServer
from uvicorn import Config, Server
from language import Language
import globals
from base import ElementProtokoll

class App:
    def __init__(
            self, 
            layout: ElementProtokoll = None, 
            title:str ='Hybrid', 
            host: str = 'localhost', 
            port: int = 8000, 
            reload: bool = True,
            exclude: str = '',
            tailwind: bool = True,
            ):
        globals.ui_run_has_been_called = True
        globals.reload = reload
        globals.title = title
        globals.excludes = [e.strip() for e in exclude.split(',')]
        globals.tailwind = tailwind

        self.app = FastAPI()
        self.sio = AsyncServer()  # Initialize the AsyncServer instance
        self.layout = layout
        self.title = title
        self.host = host
        self.port = port
        
        # Initialisierung des Static-Folders
        self.app.mount("/static", StaticFiles(directory="static"), name="static")
        
        # Initialisierung des Templates-Folders
        self.templates = Jinja2Templates(directory="templates")
        
        # GET-Endpoint
        @self.app.get("/", response_class=HTMLResponse)
        async def read_item(request: Request):
            context = {
                "request": request,
                "title": self.title,
                "elements": self.layout.to_json()
            }
            return self.templates.TemplateResponse('index.html', context=context)
        
        # PUT-Endpoint
        @self.app.put("/items/{item_id}")
        def update_item(item_id: int, item: str):
            return {"item_id": item_id, "item": item}
        
        # POST-Endpoint
        @self.app.post("/items/")
        def create_item(item: str):
            return {"item": item}
        
        # DELETE-Endpoint
        @self.app.delete("/items/{item_id}")
        def delete_item(item_id: int):
            return {"item_id": item_id}
        
        # WebSocket-Endpoint
        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            while True:
                data = await websocket.receive_text()
                await websocket.send_text(f"Received: {data}")

        @self.app.on_event('startup')
        def handle_startup():
            # Implementiere die Logik für den Startvorgang
            pass

        @self.app.on_event('shutdown')
        def handle_shutdown():
            # Implementiere die Logik für den Shutdown-Vorgang
            pass

        @self.sio.event
        def handle_handshake(sid: str) -> bool:
            return 'ok'

        @self.sio.event
        def handle_disconnect(sid: str):
            return 'client disconnect'

        @self.sio.event
        def handle_event(sid: str, msg: Dict):
            pass

        @self.sio.event
        def handle_javascript_response(sid: str, msg: Dict):
            pass
    
    def remove_route(self, path: str) -> None:
        """Remove routes with the given path."""
        self.app.routes[:] = [r for r in self.app.routes if getattr(r, 'path', None)!= path]
    

    def run(self):
        # Starte den Uvicorn-Server in einem separaten Thread
        server_thread = threading.Thread(target=self._start_server)
        server_thread.start()

        # Öffne den Webbrowser zum angegebenen Host und Port
        url = f"http://{self.host}:{self.port}"
        webbrowser.open(url)

    def split_args(self, args: str) -> List[str]:
        return [a.strip() for a in args.split(',')]

    def _start_server(self):
        # Konfiguriere und starte den Uvicorn-Server
        config = Config(app=self.app, host=self.host, port=self.port)
        server = Server(config)
        server.run()

    def compile(self):
        self.run()

