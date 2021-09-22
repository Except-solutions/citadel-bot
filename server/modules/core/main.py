from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import BACK_TO_START_TXT
from server.keyboards.main import start_kb


@dp.message_handler(CommandStart())
async def start_handler(event: types.Message) -> None:
    """/start handler."""
    await event.reply(
        'Hi! 👽',
        reply_markup=start_kb,
    )


@dp.message_handler(simple_text_filter(BACK_TO_START_TXT))
async def back_to_start(event: types.Message) -> None:
    await event.reply(
        'Окей 👽',
        reply_markup=start_kb,
    )
