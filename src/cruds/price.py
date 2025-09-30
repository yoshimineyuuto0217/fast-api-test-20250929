from sqlalchemy.ext.asyncio import AsyncSession
from schemas.price import Price
from sqlalchemy import select,func
from models.price import Price as price_model
from models.product import Product as product_model


async def read_price(db: AsyncSession) -> list[Price]:
    result = await db.execute(select(price_model))
    return result.scalars().all()


# 売り上げを計算して返してくれてるもの
async def get_sales_summary(db: AsyncSession):
    calculation_product = (
        select(
        product_model.product_name,
        func.sum(product_model.product_quantity).label("total_quantity"),
        price_model.product_price,
        func.sum(product_model.product_quantity * price_model.product_price).label("total_sales"),
            # 以下のjoinはinnerJoinになる joinだけしか描かない時はinnerJoin扱いになる
        )
        .join(price_model, product_model.product_name == price_model.product_name)
        .group_by(product_model.product_name, price_model.product_price)
    )
    result = await db.execute(calculation_product)
    # 以下の返却方法は型安全性の低いreturn方法
    return result.mappings().all()
