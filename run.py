from hydrate import App
from compiler import FastAPIWithBrowser




def run():
    fastapi_with_browser = FastAPIWithBrowser(App)
    return fastapi_with_browser