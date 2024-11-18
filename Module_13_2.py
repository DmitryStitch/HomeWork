import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(state=None)
async def all_massages(message: types.Message, state: FSMContext):
    print("Введите команду /start, чтобы начать общение.")

@dp.message_handler(commands = ['start'])
async def start_massege(massege):
    print("Привет! Я бот помогающий твоему здоровью.")

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.exception(e)