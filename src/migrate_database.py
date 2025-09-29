import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from database import Base
import models
import os
from dotenv import load_dotenv
from constants import PRODUCTION_ENV_PATH

ENV = os.getenv("ENV", "development")
# 本番環境で環境変数を読み込むため
if ENV == "production":
    load_dotenv(dotenv_path=PRODUCTION_ENV_PATH)


# Docker Compose から注入された環境変数からDATABASE_URLを取得する
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL is not set")


engine = create_async_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def reset_database():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(reset_database())