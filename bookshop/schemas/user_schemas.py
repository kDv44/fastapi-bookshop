import pydantic as p
import uuid


class CreateUser(p.BaseModel):
    username: str
    email: str
    password: str
    is_adminer: bool


class GetUser(p.BaseModel):
    id: uuid
    email: str
    username: str
    is_adminer: bool


class AuthUser(p.BaseModel):
    username: str
    password: str
