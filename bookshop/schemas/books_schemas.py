import uuid
import typing
from pydantic import BaseModel


class Books(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int


class CreateBooks(BaseModel):
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int


class GetBooks(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int

    class Config:
        orm_mode = True


class UpdateBooks(BaseModel):
    title: typing.Optional[str] = None
    author: typing.Optional[str] = None
    genre: typing.Optional[str] = None
    number_pages: typing.Optional[int] = None
    number_amount: typing.Optional[int] = None
