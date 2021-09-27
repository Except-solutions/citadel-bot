
from aiogram import types
from more_itertools import first

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import FOTD_TXT
from server.modules.fotd.roll_fotd_logic import roll_fotd


@dp.message_handler(simple_text_filter(FOTD_TXT))
async def roll_fotd_handler(event: types.Message):
    roll_fotd_result = await roll_fotd()
    await roll_fotd_result.map(  # type: ignore
        lambda result: (
            f'Пидор дня сегодня: {result[1].user_doc.username}. Поздравляем!'
            if first(result)
            else f'Сегодня пидор дня уже был выбран! И это {result[1].user_doc.username} !'
        )
    ).bind_ioresult(event.reply)
