from aiogram import types

from server.app import dp
from server.modules.dvach.top_logic import handle_top_event


@dp.message_handler(commands=['top'])
async def top_handler(event: types.Message) -> None:
    """/top handler."""
    await handle_top_event(event)
