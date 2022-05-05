from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следуйщая викторина",
                                         callback_data="button_call_2")

    markup.add(button_call_2)
    question = "сколько будет 2+2"
    answers = [
        "2",
        "12020",
        "5",
        "4"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="5",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следуйщая викторина",
                                         callback_data="button_call_3")

    markup.add(button_call_3)
    question = "кто основал Макдональдс"
    answers = [
        "Рэй Крок",
        "Джо Джирард",
        "Стив Джобс",
        "Садыр Жапаров"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="основана в 1940 15 мая Дик и Макдональды \(основатели концепции ресторанов",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Следуйщая викторина",
                                         callback_data="button_call_4")

    markup.add(button_call_4)
    question = "Когда было изобретено первое авто "
    answers = [
        "1789",
        "2019",
        "1886",
        "1801"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Карл Фредрих 1886 году представил миру своё первое авто",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()

    question = "When telegram was appeared"
    answers = [
        "2011",
        "2013",
        "2015",
        "2007"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="14th of august in 2013",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4,
                                       lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5,
                                       lambda call: call.data == "button_call_4")
