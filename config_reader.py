# from pydantic import BaseSettings, SecretStr
from pydantic import SecretStr
from pydantic_settings import BaseSettings # NEW


class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = r'.env'
        env_file_encoding = 'utf-8'


config = Settings()
