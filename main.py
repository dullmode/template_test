from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

#from templater import loader
#
#app = FastAPI()
#
#@app.get("/", response_class=HTMLResponse)
#def index(request:Request):
#    template = loader.get_template('index.html')
#    return template.render(request=request)
from router import route
app = FastAPI()
app.include_router(route.router)
