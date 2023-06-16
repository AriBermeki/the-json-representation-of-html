import threading
import webbrowser
from uvicorn import Config, Server
from fastapi import FastAPI
from app import App


class FastAPIWithBrowser:
    def __init__(self, app: App, host: str = 'localhost', port: int = 8000):
        self.app = app
        self.host = host
        self.port = port

    def run(self):
        # Starten Sie den Uvicorn-Server in einem separaten Thread
        server_thread = threading.Thread(target=self._start_server)
        server_thread.start()

        # Öffnen Sie den Webbrowser zum angegebenen Host und Port
        url = f"http://{self.host}:{self.port}"
        webbrowser.open(url)

    def _start_server(self):
        # Konfigurieren und starten Sie den Uvicorn-Server
        config = Config(app=self.app, host=self.host, port=self.port)
        server = Server(config)
        server.run()


# Beispiel für die Verwendung der Klasse FastAPIWithBrowser

# Erstellen Sie eine Instanz der FastAPI-Anwendung
app = FastAPI()

# Definieren Sie einen Endpunkt
@app.get("/")
def root():
    return {"message": "Hello, World!"}

# Erstellen Sie eine Instanz der FastAPIWithBrowser-Klasse
fastapi_with_browser = FastAPIWithBrowser(app)

# Starten Sie den Uvicorn-Server und öffnen Sie den Webbrowser
fastapi_with_browser.run()
