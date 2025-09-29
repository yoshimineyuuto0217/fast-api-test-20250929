from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# OSの中にあるENVを探しに行くなかったらdevelopmentの文字列使う
ENV = os.getenv("ENV", "development")

# OSの中にあるDATABASE_URLを探しにくdocker使ってるのでymlのDBURLを使う
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@fast-api-db:5432/mydb"


if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
