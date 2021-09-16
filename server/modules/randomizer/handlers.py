
from aiogram import types
from server.keyboards.buttons import randomizer_kb
from server.modules.randomizer.logic import get_random_boobs


async def randomizer(event: types.Message):
    await event.answer(
        'Шо будем рандомить:',
        reply_markup=randomizer_kb,
    )


async def random_boobs(event: types.Message):
    await event.answer_photo(photo=await get_random_boobs())

