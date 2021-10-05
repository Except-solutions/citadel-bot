from pathlib import Path

from pydantic import BaseSettings, Field

PROJECT_ROOT = Path(__file__).parent.parent
BASE_DIR = PROJECT_ROOT.parent


class Settings(BaseSettings):
    """Bot settings dev environment."""

    class Config:  # noqa: WPS431
        env_file = BASE_DIR.joinpath('config/.env')
        env_file_encoding = 'utf-8'
        case_sensitive = False
        use_enum_values = True

    bot_token: str = Field(env='BOT_TOKEN')
    mongo_uri: str = Field('mongodb://citadel:citadel@mongo:27017', env='MONGO_URI')

    boobs_api: str = Field('http://api.oboobs.ru/boobs', env='BOOBS_API')
    boobs_media: str = Field('http://api.oboobs.ru/boobs', env='BOOBS_MEDIA')
    start_boob_id: int = 10000
    stop_boob_id: int = 15000

    butts_api: str = Field('http://api.obutts.ru/butts', env='BUTTS_API')
    butts_media: str = Field('http://media.obutts.ru', env='BUTTS_MEDIA')
    start_butt_id: int = 1000
    stop_butt_id: int = 7000

    cats_api: str = Field('http://aws.random.cat/meow', env='CATS_API')
    default_cat: str = 'https://purr.objects-us-east-1.dream.io/i/AyAgs.jpg'

    dogs_api: str = Field('https://random.dog/woof.json', env='DOGS_API')
    default_dog: str = 'https://random.dog/5a34778b-ea6a-4e2f-8695-c35c7a665ad1.jpg'

    anime_api: str = 'https://api.waifu.pics/sfw/'
    default_anime: str = 'https://i.waifu.pics/4d8jVu4.jpg'

    dvach_url: str = Field('https://2ch.hk', env='DVACH_URL')

    group_id: str
    dobloe_utlo_pic: str = (
        'https://sun9-51.userapi.com'
        '/impg/FycA4k01IxAzWzd5wOxPW0VMsafzdNKDIKbfdQ/4j1LW1DvV9A.jpg'
        '?size=550x524&quality=96&sign=ece870656fba639ed62150172720f235&type=album'
    )


settings = Settings()
