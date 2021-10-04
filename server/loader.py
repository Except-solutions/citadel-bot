from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from server.settings.dev import settings

bot: Bot = Bot(token=settings.bot_token)
dp: Dispatcher = Dispatcher(bot=bot)
scheduler: AsyncIOScheduler = AsyncIOScheduler()
