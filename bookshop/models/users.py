from core import database
import sqlalchemy as sa


class Users(database.BaseModel):
    __tablename__ = 'users'

    username: str = sa.Column(sa.String(length=100), unique=True, nullable=False)
    email: str = sa.Column(sa.String(length=100), unique=True, nullable=False)
    hash_password = sa.Column(sa.String(length=1000), default="")

    is_adminer: bool = sa.Column(sa.Boolean, default=False)
