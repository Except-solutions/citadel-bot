import asyncio

from aiogram import Bot, Dispatcher

from server.modules.handlers import COMMAND_HANDLERS, TEXT_HANDLERS
from server.settings.dev import settings


def register_command_handlers(dispatcher: Dispatcher) -> None:
    """Telegram commands msg."""
    dispatcher.register_message_handler(COMMAND_HANDLERS['start'], commands={'start', 'restart'})


def register_text_handlers(dispatcher: Dispatcher) -> None:
    """Telegram text msg."""
    dispatcher.register_message_handler(TEXT_HANDLERS['randomizer'][0], TEXT_HANDLERS['randomizer'][1])
    dispatcher.register_message_handler(TEXT_HANDLERS['random_boobs'][0], TEXT_HANDLERS['random_boobs'][1])


async def main() -> None:
    """Bot started here."""
    bot: Bot = Bot(token=settings.bot_token)
    dispatcher: Dispatcher = Dispatcher(bot=bot)

    register_command_handlers(dispatcher)
    register_text_handlers(dispatcher)
    try:
        await dispatcher.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
