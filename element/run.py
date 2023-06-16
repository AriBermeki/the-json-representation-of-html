from app import App
from compiler import FastAPIWithBrowser




def run():
    fastapi_with_browser = FastAPIWithBrowser(app)
    return fastapi_with_browser