from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import cruds.price as price_crud

router = APIRouter()


@router.get("/calculation/", tags=["calculation"])
async def read_sales(db: AsyncSession = Depends(get_db)):
    return await price_crud.get_sales_summary(db)
