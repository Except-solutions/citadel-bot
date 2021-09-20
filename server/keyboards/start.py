from aiogram.types import ReplyKeyboardMarkup

from server.keyboards.buttons import randomizer

start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup()
start_kb.add(randomizer)
