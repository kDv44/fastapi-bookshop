from pydantic import BaseSettings


class Setting(BaseSettings):
    HOST_APP_ADDRESS: str = 'main:app'
    HOST_ADDRESS: str = '127.0.0.1'
    HOST_PORT: int = 8080
    RELOAD_FLAG: bool = True

    DB_PASSWORD: str = '1234'
    DB_HOST: str = 'localhost:5432'
    DB_IMAGE: str = 'postgres'

    SECRET_KEY: str = 'UXRbyEyXBD73TjMVz7L3jXKM7TjrwFu7'


setti = Setting()

url_db = f'postgresql://postgres:{setti.DB_PASSWORD}@{setti.DB_HOST}/{setti.DB_IMAGE}'
