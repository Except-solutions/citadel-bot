from types import MappingProxyType
from typing import Callable, Coroutine

from aiogram import types

from server.modules.core.start import start_handler

HandlerT = Callable[[types.Message], Coroutine]

BASE_COMMAND_HANDLERS: MappingProxyType[str, HandlerT] = MappingProxyType({
    'start': start_handler,
})
