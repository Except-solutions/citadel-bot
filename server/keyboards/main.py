from aiogram.types import ReplyKeyboardMarkup

from server.keyboards.buttons import fotd_btn, randomizer_btn, roll_btn

start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(selective=True)
start_kb.row(randomizer_btn, roll_btn, fotd_btn)
