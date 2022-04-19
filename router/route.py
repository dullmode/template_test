from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from templater import loader

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index(request:Request):
    template = loader.get_template('index.html')
    return template.render(request=request)
