import sqlalchemy as sa
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from core.database import get_session
from models import books
from schemas.books_schemas import *
from schemas.user_schemas import *

books_router = APIRouter()


@books_router.get('/books', response_model=list[GetBooks])
def get_books(session: Session = Depends(get_session)):
    books_data = session.query(books.Books).all()

    return books_data


@books_router.post('/add_books', response_model=GetBooks)
def create_books(
        books_data: CreateBooks,
        session: Session = Depends(get_session)
):
    new_book = books.Books(**jsonable_encoder(books_data))
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


@books_router.put("/change_books_info/{books_id}", response_model=GetBooks)
def update_books(
        books_id: uuid.UUID,
        books_info: UpdateBooks,
        session: Session = Depends(get_session)
):
    update_data = jsonable_encoder(books_info, exclude_none=True)
    updates_books = session.query(books.Books).filter(books.Books.id == books_id).first()
    session.execute(sa.update(books.Books).where(books.Books.id == books_id).values(**update_data))
    session.refresh(updates_books)
    session.commit()

    return updates_books


@books_router.delete("/delete_books/{books_name}")
def delete_books(
        books_name: str,
        session: Session = Depends(get_session)
):
    data_delete = session.query(books.Books).filter_by(title=books_name).first()
    session.delete(data_delete)
    session.commit()
    return "deleted"
