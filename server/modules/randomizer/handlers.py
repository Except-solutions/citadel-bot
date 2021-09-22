
from aiogram import types

from server.app import dp
from server.filters.text_filters import simple_text_filter
from server.keyboards.buttons import (
    RANDOM_ANIME_TXT,
    RANDOM_BOOBS_TXT,
    RANDOM_BUTT_TXT,
    RANDOM_CAT_TXT,
    RANDOMIZER_TXT,
    randomizer_kb,
)
from server.keyboards.inline import anime_callback_values, anime_kb
from server.modules.randomizer.anime_logic import get_random_anime
from server.modules.randomizer.boobs_logic import get_random_boobs
from server.modules.randomizer.butt_logic import get_random_butt
from server.modules.randomizer.cat_logic import get_random_cat


@dp.message_handler(simple_text_filter(RANDOMIZER_TXT))
async def randomizer(event: types.Message):
    await event.reply(
        'Шо будем рандомить:',
        reply_markup=randomizer_kb,
    )


@dp.message_handler(simple_text_filter(RANDOM_BOOBS_TXT))
async def random_boobs(event: types.Message):
    await event.answer_photo(photo=await get_random_boobs())


@dp.message_handler(simple_text_filter(RANDOM_BUTT_TXT))
async def random_butts(event: types.Message):
    await event.answer_photo(photo=await get_random_butt())


@dp.message_handler(simple_text_filter(RANDOM_CAT_TXT))
async def random_cats(event: types.Message):
    await event.answer_photo(photo=await get_random_cat())


@dp.message_handler(simple_text_filter(RANDOM_ANIME_TXT))
async def random_anime(event: types.Message):
    await event.answer('Ролим:', reply_markup=anime_kb)


@dp.callback_query_handler(lambda update: update.data in anime_callback_values)
async def callback_random_anime(update: types.CallbackQuery):
    await update.bot.send_photo(update.message.chat.id, photo=await get_random_anime(update.data))
