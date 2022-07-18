import pydantic as p


class CreateBooks(p.BaseModel):
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int


class GetBooks(p.BaseModel):
    id: int
    title: str
    author: str
    genre: str
    number_pages: int
    number_amount: int
