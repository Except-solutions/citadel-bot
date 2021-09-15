import asyncio

from aiogram import Bot, Dispatcher

from server.modules.handlers import BASE_COMMAND_HANDLERS
from server.settings.dev import settings


def register_handlers(dispatcher: Dispatcher) -> None:
    """Register main handlers."""
    dispatcher.register_message_handler(BASE_COMMAND_HANDLERS['start'], commands={'start', 'restart'})


async def main() -> None:
    """Bot started here."""
    bot = Bot(token=settings.bot_token)
    dispatcher = Dispatcher(bot=bot)
    register_handlers(dispatcher)
    try:
        await dispatcher.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
