import uuid
from typing import Any, Dict
from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

class Client:
    def __init__(self, base_url: str):
        self.id = str(uuid.uuid4())
        self.base_url = base_url
        self.client = FastAPI()
        self.templates = Jinja2Templates(Path(__file__).parent / 'templates')

    def request(self, method: str, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = Request.get(method, url, json=data, params=params)
        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return JSONResponse(response)

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Any:
        return self.request("POST", endpoint, data=data, params=params)

    def put(self, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Any:
        return self.request("PUT", endpoint, data=data, params=params)

    def delete(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        return self.request("DELETE", endpoint, params=params)
