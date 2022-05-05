from aiogram import types, Dispatcher
from config import bot

async def echo_and_ban(message: types.Message):
    ban_words = ['bitch']
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await bot.send_message(message.chat.id,
                                   f"ban for the word, user:{message.from_user.full_name}")
            await bot.delete_message(message.chat.id,
                                     message.message_id)

    await message.reply('Unregistered command')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban)