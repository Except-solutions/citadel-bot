# flake8: noqa

from aiogram import executor
from loader import dp, scheduler

from server.database import engine
from server.documents.users import user_doc_index


async def on_startup(dispatcher):
    # Indexing documents
    await user_doc_index(engine=engine)

if __name__ == '__main__':
    from server.modules import *
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
