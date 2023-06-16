from typing import Optional, Union, Callable
from fastapi import APIRouter
from pathlib import Path
from fastapi import APIRouter
from pathlib import Path
class Page(APIRouter):

    def page(self,
             path: str, *,
             title: Optional[str] = None,
             viewport: Optional[str] = None,
             favicon: Optional[Union[str, Path]] = None,
             dark: Optional[bool] = ...,
             response_timeout: float = 3.0,
             **kwargs,
             ) -> Callable:
        """Page

        Creates a new page at the given route.
        Each user will see a new instance of the page.
        This means it is private to the user and not shared with others
        (as it is done `when placing elements outside of a page decorator 

        :param path: route of the new page (path must start with '/')
        :param title: optional page title
        :param viewport: optional viewport meta tag content
        :param favicon: optional relative filepath or absolute URL to a favicon (default: `None`, NiceGUI icon will be used)
        :param dark: whether to use Quasar's dark mode (defaults to `dark` argument of `run` command)
        :param response_timeout: maximum time for the decorated function to build the page (default: 3.0)
        :param kwargs: additional keyword arguments passed to FastAPI's @app.get method


        from fastapi import FastAPI
        from fastapi.responses import HTMLResponse

        # Erstellen Sie eine Instanz der Page-Klasse
        page_router = Page()

        # Erstellen Sie eine Instanz der FastAPI-Anwendung
        app = FastAPI()

        # Verwenden Sie die page-Methode als Dekorator, um eine neue Seite zu definieren
        @page_router.page("/")
        async def home_page():
            return HTMLResponse("<h1>Home Page</h1>")

        @page_router.page("/about")
        async def about_page():
            return HTMLResponse("<h1>About Page</h1>")

        # Fügen Sie den Router zur FastAPI-Anwendung hinzu
        app.include_router(page_router)

        # Starten Sie die FastAPI-Anwendung
        if __name__ == "__main__":
            import uvicorn
            uvicorn.run(app, host="0.0.0.0", port=8000)

    
        """
        def decorator(func: Callable) -> Callable:
            # Decorator logic goes here
            # You can access the function being decorated using `func`

            # Example: Register the route with FastAPI
            self.add_api_route(path, func, **kwargs)

            return func

        return decorator
    

    def remove_route(self, path: str) -> None:
        self.routes[:] = [r for r in self.routes if getattr(r, 'path', None) != path]