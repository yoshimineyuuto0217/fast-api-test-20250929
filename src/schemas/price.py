from pydantic import BaseModel, Field
from datetime import datetime


class Price(BaseModel):
    price_id: int
    product_name: str
    product_price: int

    class Config:
        orm_mode: True
