
from aiogram import types
from returns.io import IOSuccess
from returns.pipeline import pipe
from returns.unsafe import unsafe_perform_io

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import FOTD_TXT
from server.modules.fotd.roll_fotd_logic import roll_fotd


@dp.message_handler(simple_text_filter(FOTD_TXT))
async def roll_fotd_handler(event: types.Message):
    roll_fotd_result = await roll_fotd()
    await unsafe_perform_io(
        roll_fotd_result.map(
            pipe(
                lambda user: f'Пидор дня сегодня: {user.user_doc.username}. Поздравляем!',
                lambda reply_text: event.reply(
                    reply_text,
                )
            )
        ).lash(
            lambda user: IOSuccess(event.answer(
                f'Сегодня пидор дня уже был выбран! И это {user.user_doc.username}',
            ))
        ).unwrap()
    )
