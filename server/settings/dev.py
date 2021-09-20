from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Bot settings dev environment."""

    bot_token: str = Field(env='BOT_TOKEN')
    boobs_api: str = Field('http://api.oboobs.ru/boobs/', env='BOOBS_API')
    start_boob_id: int = 10000
    stop_boob_id: int = 15000


settings = Settings()
