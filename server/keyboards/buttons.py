from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

RANDOMIZER_TXT: str = 'Рандомайзер 🤘'
randomizer: KeyboardButton = KeyboardButton(RANDOMIZER_TXT)


randomizer_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup()

RANDOM_BOOBS_TXT: str = 'Вот они сиське! 🧜‍♀️'
random_boobs: KeyboardButton = KeyboardButton(RANDOM_BOOBS_TXT)

randomizer_kb.add(random_boobs)
