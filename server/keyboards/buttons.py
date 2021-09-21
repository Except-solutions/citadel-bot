from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BACK_TO_START_TXT: str = 'В начало 👈'
back_to_start_btn: KeyboardButton = KeyboardButton(BACK_TO_START_TXT)

RANDOMIZER_TXT: str = 'Рандомайзер 🤘'
randomizer_btn: KeyboardButton = KeyboardButton(RANDOMIZER_TXT)


randomizer_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup()

RANDOM_BOOBS_TXT: str = 'Вот они сиське 🧜‍♀️'
random_boobs_btn: KeyboardButton = KeyboardButton(RANDOM_BOOBS_TXT)


RANDOM_BUTT_TXT: str = 'То с чего срут 👃'
random_butt_btn: KeyboardButton = KeyboardButton(RANDOM_BUTT_TXT)

RANDOM_CAT_TXT: str = 'КОТэтэр 😽'
random_cat_btn: KeyboardButton = KeyboardButton(RANDOM_CAT_TXT)

RANDOM_ANIME_TXT: str = 'Православное маНЯме 👅'
random_anime_btn: KeyboardButton = KeyboardButton(RANDOM_ANIME_TXT)

randomizer_kb.row(random_boobs_btn, random_butt_btn, random_cat_btn)
randomizer_kb.row(back_to_start_btn, random_anime_btn)
