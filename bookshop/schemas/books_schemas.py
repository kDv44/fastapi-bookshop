import pydantic as p
import uuid


class CreateBooks(p.BaseModel):
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int


class GetBooks(p.BaseModel):
    id: uuid
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int

