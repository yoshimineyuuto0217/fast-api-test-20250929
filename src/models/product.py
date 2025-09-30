from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime, timezone


class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(36), nullable=False)
    product_weight = Column(String(10), nullable=False)
    product_height = Column(String(10), nullable=False)
    product_temperature = Column(String(10), nullable=False)
    product_quantity = Column(Integer, nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
