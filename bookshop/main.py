import uvicorn

from fastapi import FastAPI
from settings import setti
from services.books_api import books_router
from services.users_api import users_router


app = FastAPI()

app.include_router(books_router, tags=["books"], prefix="/bookshop")
app.include_router(users_router, tags=["users"], prefix="/bookshop/users")


@app.get('/')
def work_test():
    return {'message': 'it`s work! ᕙ(^▿^-ᕙ)'}


if __name__ == '__main__':
    uvicorn.run(setti.HOST_APP_ADDRESS, host=setti.HOST_ADDRESS, reload=setti.RELOAD_FLAG)
