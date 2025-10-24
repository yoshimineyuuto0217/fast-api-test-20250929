from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import cruds.user as user_crud
import schemas.user as user_schema

router = APIRouter()


# 商品を登録 | GET
@router.post("/user", tags=["user"], response_model=user_schema.UserResponse)
async def create_User(
    userInfo: user_schema.UserCreate, db: AsyncSession = Depends(get_db)
):
    new_user = await user_crud.create_User(db,userInfo)
    return new_user
