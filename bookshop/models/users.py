import uuid

from core import database
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


class Users(database.BaseModel):
    __tablename__ = 'Users'

    user_id: uuid.UUID = sa.Column(postgresql.UUID(as_uuid=True), nullable=False)

    username = sa.Column(sa.String(length=100))
    email = sa.Column(sa.String(length=100))
    password = sa.Column(sa.String(length=200))

    is_adminer = sa.Column(sa.Boolean(), default=False)
