# crudsは関数を定義してるだけでroutesフォルダで呼び出してる！！

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import schemas.product as product_schema
import cruds.product as product_crud

router = APIRouter()


# 商品を全取得
@router.get(
    "/product/", response_model=list[product_schema.ResponseProduct], tags=["product"]
)
async def read_product(db: AsyncSession = Depends(get_db)):
    return await product_crud.read_product(db)


# 商品の合計値を取得
@router.get(
    "/product/summary", response_model=list[product_schema.ProductSummary], tags={"product"}
)
async def read_product_summary(db: AsyncSession = Depends(get_db)):
    return await product_crud.read_product_summary(db)


# 商品を登録
@router.post(
    "/product/",
    response_model=product_schema.ResponseProduct,
    tags=["product"],
)
async def create_product(
    product: product_schema.ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    new_product = await product_crud.create_product(db, product)
    return new_product
