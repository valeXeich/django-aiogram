import os
import django

from aiogram.utils import executor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from .create_bot import dp
from .handlers import register_handlers


async def on_startup(_):
    print('Bot online')

register_handlers(dp)

executor = executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
