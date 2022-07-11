from pydantic import BaseSettings


class Setting(BaseSettings):
    HOST_APP_ADDRESS: str = 'main:app'
    HOST_ADDRESS: str = '127.0.0.1'
    HOST_PORT: int = 8080
    RELOAD_FLAG: bool = True

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    