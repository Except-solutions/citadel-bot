# flake8: noqa

from aiogram import executor
from loader import dp

from server.database import engine
from server.documents.users import user_doc_index
from server.modules import *


async def on_startup(dispatcher):
    # Indexing documents
    await user_doc_index(engine=engine)

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
