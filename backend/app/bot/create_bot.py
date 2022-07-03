from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token='5305179029:AAHTJqyjoEPeZfiN1x0BAQtvaUOl0pFpSOg')

dp = Dispatcher(bot, storage=storage)