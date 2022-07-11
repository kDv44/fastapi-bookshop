from fastapi import FastAPI
from settings import Setting as Set
import uvicorn

app = FastAPI()


@app.get('/')
def work_test():
    return {'message': 'it`s work! ᕙ(^▿^-ᕙ)'}


if __name__ == '__main__':
    uvicorn.run(Set.HOST_APP_ADDRESS, host=Set.HOST_ADDRESS, reload=Set.RELOAD_FLAG)
