from random import randint

from aiogram import types

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import NUMBER_RANGE_ROLL_TXT, ROLL_TXT, roll_kb

START_ROLL_NUMBER: int = 100_000
STOP_ROLL_NUMBER: int = 999_999


@dp.message_handler(simple_text_filter(ROLL_TXT))
async def roll(event: types.Message) -> None:
    await event.reply('Выбери стикер', reply_markup=roll_kb)


@dp.message_handler(simple_text_filter(NUMBER_RANGE_ROLL_TXT))
async def number_roll(event: types.Message) -> None:
    await event.reply(str(randint(START_ROLL_NUMBER, STOP_ROLL_NUMBER)))
