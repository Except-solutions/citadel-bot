from types import MappingProxyType
from typing import Callable, Coroutine, Tuple

from aiogram import types

from server.keyboards.buttons import RANDOMIZER_TXT, RANDOM_BOOBS_TXT
from server.modules.core.start import start_handler
from server.modules.randomizer.handlers import randomizer, random_boobs

HandlerT = Callable[[types.Message], Coroutine]

COMMAND_HANDLERS: MappingProxyType[str, HandlerT] = MappingProxyType({
    'start': start_handler,
})

TEXT_HANDLERS: MappingProxyType[str, Tuple[HandlerT, Callable[[str], bool]]] = MappingProxyType({
    'randomizer': (randomizer, lambda message: message.text == RANDOMIZER_TXT),
    'random_boobs': (random_boobs, lambda message: message.text == RANDOM_BOOBS_TXT)
})
