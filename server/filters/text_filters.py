from typing import Callable

from aiogram import types


def simple_text_filter(msg_text: str) -> Callable[[types.Message], bool]:
    def _text_filter(message: types.Message) -> bool:
        return message.text == msg_text
    return _text_filter
