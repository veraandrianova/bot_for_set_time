
from aiogram import types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from connector import DiskConnector
from config import token
test = DiskConnector()
storage = MemoryStorage()
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp: Dispatcher = Dispatcher(bot, storage=storage)
