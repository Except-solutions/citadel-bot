from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Bot settings dev environment."""

    bot_token: str = Field(env='BOT_TOKEN')


settings = Settings()
