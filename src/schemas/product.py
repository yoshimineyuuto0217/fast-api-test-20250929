# レスポンスで受け取る引数と返す引数を設定
from pydantic import BaseModel, Field
from datetime import datetime


# 新規作成時に使う型 | Method：Create
class ProductBase(BaseModel):
    product_name: str = Field(..., example="製品1")
    product_weight: str = Field(..., example="10kg")
    product_height: str = Field(..., example="20cm")
    product_temperature: str = Field(..., example="25℃")
    product_quantity: int = Field(..., example=100)


class ProductCreate(ProductBase):
    pass


class ResponseProduct(ProductBase):
    product_id: int
    created_at: datetime
    updated_at: datetime

    # 今回の500エラーclass Configのインデント位置が間違ってた為
    # ここでオブジェクト型にして返す設定
    class Config:
        orm_mode = True
