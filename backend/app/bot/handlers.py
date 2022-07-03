from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.services import create_user


class RegisterFSM(StatesGroup):
    username = State()
    password = State()
    r_password = State()


password = None

async def start_registration(message: Message):
    await RegisterFSM.username.set()
    await message.reply('Укажите свой username')

async def set_username(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await RegisterFSM.next()
    await message.reply('Укажите пароль')

async def set_password(message: Message, state: FSMContext):
    global password
    async with state.proxy() as data:
        data['password'] = message.text
        password = data['password']
    await RegisterFSM.next()
    await message.reply('Повторите пароль')

async def r_password_invalid(message: Message):
    await message.reply('Не правильный пароль')

async def check_password(message: Message, state: FSMContext):
    async with state.proxy() as data:
        created, user = await create_user(
            t_name=message.from_user.first_name,
            t_username=message.from_user.username,
            t_user_id=message.from_user.id,
            username=data['username'],
            password=data['password']
        )
    if created:
        await message.reply('Учетная запись успешно создана')
    else:
        await message.reply('Пользователь с таким username уже занят')
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_registration, commands='Регистрация', state=None)
    dp.register_message_handler(set_username, state=RegisterFSM.username)
    dp.register_message_handler(set_password, state=RegisterFSM.password)
    dp.register_message_handler(r_password_invalid, lambda message: message.text != password, state=RegisterFSM.r_password)
    dp.register_message_handler(check_password, lambda message: message.text == password, state=RegisterFSM.r_password)
