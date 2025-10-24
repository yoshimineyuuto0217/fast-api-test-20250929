from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import product
from routes import price
from routes import user
from database import async_engine, Base 


app = FastAPI()

# CORSの設定
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main.pyがスワッガーに出てる部分になる
app.include_router(product.router)
app.include_router(price.router)
app.include_router(user.router)

@app.on_event("startup")
async def startup_event():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ テーブル作成完了！")