from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Bot settings dev environment."""

    bot_token: str = Field(env='BOT_TOKEN')
    boobs_api: str = Field('http://api.oboobs.ru/boobs/', env='BOOBS_API')


settings = Settings()
