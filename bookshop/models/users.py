from core import database
import sqlalchemy as sa


class Users(database.BaseModel):
    __tablename__ = 'Users'

    user_id: int = sa.Column(sa.Integer())

    username: str = sa.Column(sa.String(length=100))
    email: str = sa.Column(sa.String(length=100))
    password: str = sa.Column(sa.String(length=200))

    is_adminer: bool = sa.Column(sa.Boolean(), default=False)
