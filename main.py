

from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def index():
    html_content = """
    <html>
        <head>
            <title>Home Page</title>
        <head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", response_class=HTMLResponse)
def read_root():
    return index()

