from aiogram import types


async def start_handler(event: types.Message) -> None:
    """/start handler."""
    user = event.from_user.get_mention(as_html=True)
    await event.answer(
        f'Hello, {user} 👋!',
        parse_mode=types.ParseMode.HTML,
    )
