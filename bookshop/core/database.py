import uuid
import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import url_db

engine = create_engine(url_db)
Base = declarative_base()

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)


class BaseModel(Base):
    __abstract__ = True

    id: uuid.UUID = sa.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )


def get_session() -> Session:
    session = Session()
    try:
        yield session
    except Exception as e:
        print(e)
    finally:
        session.close()
