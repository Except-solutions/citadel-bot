from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

waifu_btn: InlineKeyboardButton = InlineKeyboardButton('Waifu', callback_data='waifu')
neko_btn: InlineKeyboardButton = InlineKeyboardButton('Neko', callback_data='neko')
shinobu_btn: InlineKeyboardButton = InlineKeyboardButton('Shinobu', callback_data='shinobu')
bully_btn: InlineKeyboardButton = InlineKeyboardButton('Bully', callback_data='bully')
cry_btn: InlineKeyboardButton = InlineKeyboardButton('Cry', callback_data='cry')
hug_btn: InlineKeyboardButton = InlineKeyboardButton('Hug', callback_data='hug')
kiss_btn: InlineKeyboardButton = InlineKeyboardButton('Kiss', callback_data='kiss')
lick_btn: InlineKeyboardButton = InlineKeyboardButton('Lick', callback_data='lick')
pat_btn: InlineKeyboardButton = InlineKeyboardButton('Pat', callback_data='pat')
smug_btn: InlineKeyboardButton = InlineKeyboardButton('Smug', callback_data='smug')
highfive_btn: InlineKeyboardButton = InlineKeyboardButton('Highfive', callback_data='highfive')
nom_btn: InlineKeyboardButton = InlineKeyboardButton('Nom', callback_data='nom')
bite_btn: InlineKeyboardButton = InlineKeyboardButton('Bite', callback_data='bite')
slap_btn: InlineKeyboardButton = InlineKeyboardButton('Slap', callback_data='slap')
wink_btn: InlineKeyboardButton = InlineKeyboardButton('Wink', callback_data='wink')
poke_btn: InlineKeyboardButton = InlineKeyboardButton('Poke', callback_data='poke')
dance_btn: InlineKeyboardButton = InlineKeyboardButton('Dance', callback_data='dance')
cringe_btn: InlineKeyboardButton = InlineKeyboardButton('Cringe', callback_data='cringe')
blush_btn: InlineKeyboardButton = InlineKeyboardButton('Blush', callback_data='blush')

anime_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=3)
anime_kb.row(waifu_btn, neko_btn, shinobu_btn)
anime_kb.row(bully_btn, cry_btn, hug_btn)
anime_kb.row(kiss_btn, lick_btn, pat_btn)
anime_kb.row(smug_btn, highfive_btn, nom_btn)
anime_kb.row(bite_btn, slap_btn, wink_btn)
anime_kb.row(poke_btn, dance_btn, cringe_btn)
anime_kb.row(blush_btn)

anime_callback_values: tuple[str, ...] = tuple(
    buttons['callback_data'] for rows in anime_kb.inline_keyboard for buttons in rows
)
