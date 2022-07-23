from core import database
import sqlalchemy as sa


class Books(database.BaseModel):
    __tablename__ = 'books'

    title: str = sa.Column(sa.String(length=100))
    author: str = sa.Column(sa.String(length=100))
    genre: str = sa.Column(sa.String(length=100))
    number_pages: int = sa.Column(sa.Integer())
    number_amount: int = sa.Column(sa.Integer())
