from server.app import dp, scheduler
from server.settings.dev import settings


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=7, minute=0)
async def send_dobloe_utlo():
    await dp.bot.send_photo(chat_id=settings.group_id, photo=settings.dobloe_utlo_pic)
