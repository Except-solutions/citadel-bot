from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BACK_TO_START_TXT: str = 'В начало 👈'
back_to_start_btn: KeyboardButton = KeyboardButton(BACK_TO_START_TXT)

RANDOMIZER_TXT: str = 'Рандомайзер 🤘'
randomizer_btn: KeyboardButton = KeyboardButton(RANDOMIZER_TXT)
randomizer_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(selective=True)

RANDOM_BOOBS_TXT: str = 'Вот они сиське 🧜‍♀️'
random_boobs_btn: KeyboardButton = KeyboardButton(RANDOM_BOOBS_TXT)

RANDOM_BUTT_TXT: str = 'Жэпы 👃'
random_butt_btn: KeyboardButton = KeyboardButton(RANDOM_BUTT_TXT)

RANDOM_CAT_TXT: str = 'КОТэтэр 😽'
random_cat_btn: KeyboardButton = KeyboardButton(RANDOM_CAT_TXT)

RANDOM_DOG_TXT: str = 'Баси 🐶'
random_dog_btn: KeyboardButton = KeyboardButton(RANDOM_DOG_TXT)

RANDOM_ANIME_TXT: str = 'Православное маНЯме 👅'
random_anime_btn: KeyboardButton = KeyboardButton(RANDOM_ANIME_TXT)

randomizer_kb.row(random_boobs_btn, random_butt_btn)
randomizer_kb.row(random_cat_btn, random_dog_btn)
randomizer_kb.row(back_to_start_btn, random_anime_btn)


ROLL_TXT: str = 'ROLL 🤘'
roll_btn: KeyboardButton = KeyboardButton(ROLL_TXT)
roll_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(selective=True)

NUMBER_RANGE_ROLL_TXT: str = '111111-999999 ⁉️'
number_range_btn: KeyboardButton = KeyboardButton(NUMBER_RANGE_ROLL_TXT)
roll_kb.row(KeyboardButton('🎲'), number_range_btn)
roll_kb.row(back_to_start_btn)

FOTD_TXT: str = 'Пидор дня 👨‍❤️‍👨'
fotd_btn: KeyboardButton = KeyboardButton(FOTD_TXT)
