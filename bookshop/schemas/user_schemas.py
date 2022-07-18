import pydantic as p


class CreateUser(p.BaseModel):
    username: str
    email: str
    password: str
    is_adminer: bool

    class Config:
        orm_mode = True


class GetUser(p.BaseModel):
    id: int
    email: str
    username: str
    is_adminer: bool

    class Config:
        orm_mode = True


class AuthUser(p.BaseModel):
    username: str
    password: str
