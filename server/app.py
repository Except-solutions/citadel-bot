# flake8: noqa

from aiogram import executor
from loader import dp

from server.modules import *

if __name__ == '__main__':
    executor.start_polling(dp)
