from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
telegram_button = KeyboardButton("/telegram")
bot_button = KeyboardButton("/bot")
location_button = KeyboardButton("Share Location", request_location=True)
info_button = KeyboardButton("Share info", request_contact=True)

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

start_markup.row(help_button, quiz_button, telegram_button, bot_button, location_button, info_button)