from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Bot settings dev environment."""

    bot_token: str = Field(env='BOT_TOKEN')

    boobs_api: str = Field('http://api.oboobs.ru/boobs', env='BOOBS_API')
    boobs_media: str = Field('http://api.oboobs.ru/boobs', env='BOOBS_API')
    start_boob_id: int = 10000
    stop_boob_id: int = 15000

    butts_api: str = Field('http://api.obutts.ru/butts', env='BUTTS_API')
    butts_media: str = Field('http://media.obutts.ru', env='BUTTS_MEDIA')
    start_butt_id: int = 1000
    stop_butt_id: int = 7000

    cats_api: str = Field('http://aws.random.cat/meow', env='CATS_API')
    default_cat: str = 'https://purr.objects-us-east-1.dream.io/i/AyAgs.jpg'

    anime_api: str = 'https://api.waifu.pics/sfw/'
    default_anime: str = 'https://i.waifu.pics/4d8jVu4.jpg'


settings = Settings()
