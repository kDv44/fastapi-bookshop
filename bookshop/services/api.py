from fastapi import APIRouter
from core.database import Session
from models import books, users
from schemas.books_schemas import GetBooks
from schemas.user_schemas import *

router = APIRouter()


# here we get all the books
@router.get('/books', response_model=list[GetBooks])
def get_books():
    session = Session()
    get_books_result = (
        session.query(books.Books).all()
    )
    return get_books_result

