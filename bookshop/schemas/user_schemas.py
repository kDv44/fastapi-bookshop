import uuid
import pydantic as p
import typing as t


class CreateUser(p.BaseModel):
    username: str
    email: str
    password: str
    is_adminer: bool

    class Config:
        orm_mode = True


class GetUser(p.BaseModel):
    id: uuid.UUID
    email: str
    username: str
    is_adminer: bool

    class Config:
        orm_mode = True


class AuthUser(p.BaseModel):
    username: str
    password: str


class AccessToken(p.BaseModel):
    access_token: str
    token_type: str


class TokenPayload(p.BaseModel):
    sub: t.Optional[str] = None


class Token(p.BaseModel):
    token_type: str
    access_token: str
