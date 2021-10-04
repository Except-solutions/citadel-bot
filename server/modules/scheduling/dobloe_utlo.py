from aiogram import Dispatcher

from server.loader import dp, scheduler
from server.settings.dev import settings


async def send_dobloe_utlo(dispatcher: Dispatcher):
    await dispatcher.bot.send_photo(chat_id=settings.group_id, photo=settings.dobloe_utlo_pic)

scheduler.add_job(send_dobloe_utlo, 'cron', day_of_week='mon-fri', hour=7, minute=0, args=(dp, ))
