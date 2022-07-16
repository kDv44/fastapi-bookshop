import uuid

from core import database
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


class Books(database.BaseModel):
    __tablename__ = 'Books'

    book_id: uuid.UUID = sa.Column(postgresql.UUID(as_uuid=True), nullable=False)

    title = sa.Column(sa.String(length=100))
    author = sa.Column(sa.String(length=100))
    genre = sa.Column(sa.String(length=100))
    number_pages = sa.Column(sa.Integer())
    number_amount = sa.Column(sa.Integer())

    is_sale = sa.Column(sa.Boolean(), default=False)
