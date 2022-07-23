import datetime as dt
import typing as t
import secrets

from passlib.context import CryptContext
from jose import jwt
from settings import setti
from models.users import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_password() -> str:
    return secrets.token_urlsafe(25)


def create_access_token(user: Users) -> str:
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=10)
    to_encode = {
        "exp": expire,
        "sub": str(user.id)
    }
    encoded_jwt = jwt.encode(to_encode, setti.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def set_and_get_tokens(user: Users) -> t.Dict[str, t.Any]:
    access_token = create_access_token(user)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
