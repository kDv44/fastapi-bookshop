from fastapi import FastAPI
from settings import setti
from services.api import router as api_router
import uvicorn

app = FastAPI()

app.include_router(api_router, prefix="/bookshop")


@app.get('/')
def work_test():
    return {'message': 'it`s work! ᕙ(^▿^-ᕙ)'}


if __name__ == '__main__':
    uvicorn.run(setti.HOST_APP_ADDRESS, host=setti.HOST_ADDRESS, reload=setti.RELOAD_FLAG)
