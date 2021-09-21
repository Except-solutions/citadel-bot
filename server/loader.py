from aiogram import Bot, Dispatcher

from server.settings.dev import settings

bot: Bot = Bot(token=settings.bot_token)
dp: Dispatcher = Dispatcher(bot=bot)
