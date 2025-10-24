from sqlalchemy.ext.asyncio import AsyncSession
import schemas.user as user_schemas
import models.user as user_model
from fastapi import HTTPException
from enums.status_codes import StatusCodes as sc
from enums.error_messages import ErrorMessages as em
import traceback


# ユーザの新規登録
async def create_User(
    db: AsyncSession, userInfo: user_schemas.UserCreate
) -> user_model.User:
    try:
        new_user = user_model.User(
            name=userInfo.name, address=userInfo.address
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    except InterruptedError:
        await db.rollback()
        error_detail = "".join(traceback.format_exception_only(type(e), e))
        raise HTTPException(
            status_code=sc.INTERNAL_SERVER_ERROR.value,
            detail=f"{em.MESSAGE_002.value} - {error_detail}",
        )
