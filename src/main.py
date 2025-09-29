from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import product

app = FastAPI()

# CORSの設定
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main.pyがスワッガーに出てる部分になる
app.include_router(product.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

