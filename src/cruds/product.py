# crudsは関数を定義してるだけでroutesフォルダで呼び出してる！！

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
import schemas.product as product_schema
import models.product as product_model
from datetime import datetime, timezone
from enums.error_messages import ErrorMessages as em
from enums.status_codes import StatusCodes as sc
from sqlalchemy.future import select
import traceback


# 製品情報の新規登録 | POST
async def create_product(
    db: AsyncSession, product: product_schema.ProductCreate
) -> product_model.Product:
    try:
        new_product = product_model.Product(
            product_name=product.product_name,
            product_weight=product.product_weight,
            product_height=product.product_height,
            product_temperature=product.product_temperature,
            product_quantity=product.product_quantity,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)
        return new_product

    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=sc.INTERNAL_SERVER_ERROR.value, detail=em.MESSAGE_001.value
        )
    except SQLAlchemyError as e:
        await db.rollback()
        error_detail = "".join(traceback.format_exception_only(type(e), e))
    raise HTTPException(
        status_code=sc.INTERNAL_SERVER_ERROR.value,
        detail=f"{em.MESSAGE_002.value} - {error_detail}",
    )

# 製品情報を取得 | GET
async def read_product(db:AsyncSession) -> list[product_model.Product]:
    result = await db.execute(select(product_model.Product))
    return result.scalars().all()