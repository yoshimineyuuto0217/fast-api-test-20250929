from sqlalchemy import (
    Column,
    Integer,
    String,
)
from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(36), nullable=False)
    address = Column(String(36), nullable=False, unique=True)
