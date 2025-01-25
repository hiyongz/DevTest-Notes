__author__ = 'kangpc'
__date__ = '2021-6-27 22:51'

from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app='demo:app', host="127.0.0.1", port=8001, reload=True, debug=True)