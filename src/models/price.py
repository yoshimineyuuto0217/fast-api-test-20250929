from sqlalchemy import (
    Column,
    Integer,
    String,
)
from database import Base


class Price(Base):
    __tablename__ = "price"
    price_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(36), nullable=False, unique=True)
    product_price = Column(Integer, nullable=False)
