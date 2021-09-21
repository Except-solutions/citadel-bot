from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

RANDOMIZER_TXT: str = 'Рандомайзер 🤘'
randomizer: KeyboardButton = KeyboardButton(RANDOMIZER_TXT)


randomizer_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup()

RANDOM_BOOBS_TXT: str = 'Вот они сиське 🧜‍♀️'
random_boobs: KeyboardButton = KeyboardButton(RANDOM_BOOBS_TXT)


RANDOM_BUTT_TXT: str = 'То с чего срут 👃'
random_butt: KeyboardButton = KeyboardButton(RANDOM_BUTT_TXT)

RANDOM_CAT_TXT: str = 'КОТэтэр 😽'
random_cat: KeyboardButton = KeyboardButton(RANDOM_CAT_TXT)

randomizer_kb.add(random_boobs)
randomizer_kb.add(random_butt)
randomizer_kb.add(random_cat)
