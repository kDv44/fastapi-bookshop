import sqlalchemy as sa
import fastapi as fa

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from core.database import get_session
from models import users
from schemas.user_schemas import *
from security import sec

users_router = APIRouter()


@users_router.get('/get_users')
def get_all_users(
        session: Session = Depends(get_session)
):
    users_data = session.query(users.Users).all()

    return users_data


@users_router.post('/register_user', response_model=GetUser)
def create_users(
        user_data: CreateUser,
        session: Session = Depends(get_session)
):
    new_user = users.Users(
        **jsonable_encoder(user_data, exclude={'password'}),
        hash_password=sec.get_password_hash(user_data.password)
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@users_router.post("/access-token", response_model=AccessToken)
async def get_access_token(
        user_log: AuthUser,
        db: Session = Depends(get_session)
):
    user = db.scalar(sa.select(users.Users).where(users.Users.username == user_log.username))
    if not user or not sec.verify_password(user_log.password, user.hash_password):
        raise fa.HTTPException(status_code=400, detail="Wrong password or login")
    return await sec.set_and_get_tokens(user)
