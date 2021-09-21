from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from server.app import dp
from server.keyboards.start import start_kb


@dp.message_handler(CommandStart())
async def start_handler(event: types.Message) -> None:
    """/start handler."""
    await event.answer(
        'Hi! 👽',
        reply_markup=start_kb,
    )
