import pydantic
import sqlalchemy as sa
import fastapi as fa

from fastapi import security as fastapi_security
from jose import jwt
from settings import setti
from security import sec
from sqlalchemy import orm
from schemas import user_schemas
from core import database
from models.users import Users


oauth2 = fastapi_security.OAuth2PasswordBearer(
    tokenUrl=f"/user/access-token",
)


def exception_try_login() -> None:
    raise fa.HTTPException(
        status_code=401,
        detail="Not correct password or login",
    )


async def get_current_user(token: str, is_moderator=False) -> Users:
    try:
        payload = jwt.decode(token, setti.SECRET_KEY, algorithms=[sec.ALGORITHM])
        token_data = user_schemas.TokenPayload(**payload)
    except (jwt.JWTError, pydantic.ValidationError) as e:
        exception_try_login()
    if token_data.sub:
        db: orm.Session = database.get_session().__next__()
        user = db.scalar(sa.select(Users).where(Users.id == token_data.sub))
        if is_moderator and not user.is_moderator:
            raise fa.HTTPException(status_code=401, detail="You not root.")
    else:
        raise fa.HTTPException(status_code=401, detail="Not valid token.")
    if not user:
        raise fa.HTTPException(status_code=404, detail="User not found.")
    return user


async def get_user_access_token(
    token: str = fa.Depends(oauth2),
):
    return await get_current_user(token)


async def get_moderator_access_token(
    token: str = fa.Depends(oauth2),
):
    return await get_current_user(token, is_moderator=True)
