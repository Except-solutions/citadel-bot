from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    bot_token: str = Field(..., env='BOT_TOKEN')


settings = Settings()
