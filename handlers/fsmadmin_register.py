from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards import admin_kb
from config import bot


class FSMADMIN(StatesGroup):
    id = State()
    username = State()
    first_name = State()
    last_name = State()

async def user_command(message: types.Message):
    global USER_ID
    USER_ID = message.chat.id
    await bot.send_message(message.from_user.id,
                           "'Yes, user\n"
                           "what is your id, username, first_name and last_name",
                           reply_markup=admin_kb.button_admin)

async def fsm_start(message: types.Message):
    if message.from_user.id == USER_ID:
        await FSMADMIN.username.set()
        await message.reply("send me username please")

async def load_id(message: types.Message,
                  state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    if message.chat.id == USER_ID:
        await FSMADMIN.next()
        await message.reply("Send me username")

async def load_username(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMADMIN.next()
    await message.reply("send me first_name")

async def load_first_name(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMADMIN.next()
    await message.reply("send me last_name")

async def load_last_name(message: types.Message,
                           state: FSMContext):
        async with state.proxy() as data:
            data['last_name'] = message.text
        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(user_command, commands=['user'])
    dp.register_message_handler(fsm_start, commands=['upload'], state=None)
    dp.register_message_handler(load_id, state=FSMADMIN.id)
    dp.register_message_handler(load_username, state=FSMADMIN.username)
    dp.register_message_handler(load_first_name, state=FSMADMIN.first_name)
    dp.register_message_handler(load_last_name, state=FSMADMIN.last_name)