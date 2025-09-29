import asyncio
from database import async_engine, Base

async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created!")

if __name__ == "__main__":
    asyncio.run(init_models())
