from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from Keyboards import client_kb
from config import bot

async def hello(message: types.Message):
    await message.reply(text="hello my boss",
                        reply_markup=client_kb.start_markup)

async def help(message: types.Message):
    await message.reply(text="can i help you")

async def telegram(message: types.Message):
    await message.reply(text="About Telegram. It is cross-platform system message processing with functions VoIP.")

async def bot(message: types.Message):
    await message.reply(text="what do bots do? It is a programm, which performing differenet actions.")

async def mood_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("good",
                                         callback_data="button_call_1")
    button_call_2 = InlineKeyboardButton("bad",
                                         callback_data="button_call_2")

    markup.add(button_call_1, button_call_2)
    question = "How are you"
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Becuase",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следуйщая викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "which option is correct?"
    answers = [
        "def add(): retutn",
        "def add(): return sum(list_1, list_2, list_3)",
        "{list_1 + list_1},list_2 = {list_2 + list_2},list_3 = {list_3 + list_3}'"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Becuase",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(telegram, commands=['telegram'])
    dp.register_message_handler(bot, commands=['bot'])