from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse
from typing import List

from src.routers.product_router import product_router

# middleware
from src.utils.http_error_handler import HTTPErrorHandler

app = FastAPI()

# app.add_middleware(HTTPErrorHandler)


app.title = "My first app with FastAPI"
app.version = "2.0.0"

@app.get('/', tags=['Home'])
def home():
    # return "Hello World!"
    # return HTMLResponse('<h1>Hello World</h1>')
    return PlainTextResponse(content='Hello World', status_code=200)

@app.get('/readme')
def get_readme():
    return FileResponse('README.md')

# include product routers
app.include_router(router=product_router)
