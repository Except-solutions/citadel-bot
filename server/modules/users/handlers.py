from aiogram import types
from returns.io import IOSuccess
from returns.pipeline import pipe
from returns.unsafe import unsafe_perform_io

from server.app import dp
from server.keyboards.main import start_kb
from server.modules.users.register_user_logic import register_user


@dp.message_handler(commands='register_me')
async def register_user_handler(event: types.Message) -> None:
    io_create_result = await register_user(telegram_id=event.from_user.id, username=event.from_user.username)
    await unsafe_perform_io(
        io_create_result.map(pipe(
            lambda user: f'@{user.username} Успешно зарегестрирован!',
            lambda reply_text: event.reply(
                reply_text,
                reply_markup=start_kb,
            )
        )).lash(
            lambda _: IOSuccess(event.answer(
                'Похоже вы уже зарегестрированы!',
                reply_markup=start_kb,
            ))
        ).unwrap()
    )
