from asyncio import sleep

from server.app import dp, scheduler
from server.settings.dev import settings


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=7, minute=0)
async def send_dobloe_utlo():
    await dp.bot.send_photo(chat_id=settings.group_id, photo=settings.dobloe_utlo_pic)


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=15, minute=0)
async def send_pokinut_zavod():
    await dp.bot.send_message(text='Внимание всем покинуть территорию завода!', chat_id=settings.group_id)
    await sleep(2)
    await dp.bot.send_message(text='Повторяю всем покинуть территорию завода!', chat_id=settings.group_id)
