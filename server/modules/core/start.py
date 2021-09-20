from aiogram import types

from server.keyboards.start import start_kb


async def start_handler(event: types.Message) -> None:
    """/start handler."""
    await event.answer(
        'Hi! 👽',
        reply_markup=start_kb,
    )
