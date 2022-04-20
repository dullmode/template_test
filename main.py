from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from router import route
app = FastAPI()
app.include_router(route.router)
