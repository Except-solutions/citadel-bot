
from aiogram import types

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import ROLL_TXT, roll_kb


@dp.message_handler(simple_text_filter(ROLL_TXT))
async def roll(event: types.Message) -> None:
    await event.reply('Выбери стикер', reply_markup=roll_kb)
