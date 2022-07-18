from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_session
from models import books, users
from schemas.books_schemas import GetBooks
from schemas.user_schemas import *

router = APIRouter()


# here we get all the books
@router.get('/books', response_model=list[GetBooks])
def get_books(session: Session = Depends(get_session)):
    get_books_result = (
        session.query(books.Books).all()
    )
    return get_books_result
