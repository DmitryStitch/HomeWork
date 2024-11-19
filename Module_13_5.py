import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_inf = KeyboardButton(text='Рассчитать')
button_call = KeyboardButton(text='Информация')
kb.add(button_inf, button_call)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['start'])
async def start_massege(message: types.Message):
    await message.answer("Привет! Чтобы получить расчет калорий, напиши 'Рассчитать'.", reply_markup=kb)

@dp.message_handler(text = 'Информация')
async def all_massages(message: types.Message, state: FSMContext):
    await message.reply("Привет! Я бот помогающий твоему здоровью!")

@dp.message_handler(text = ['Рассчитать'])
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age = int(message.text))
    await message.answer("Введите свой рост (в см): ")
    await UserState.next()

@dp.message_handler(state = UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth = int(message.text))
    await message.answer("Введите свой вес (в кг): ")
    await UserState.next()

@dp.message_handler(state = UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')

    calories = 10 * weight + 6.25 * growth + 5 * age + 5

    await message.answer(f"Ваша норма каллорий:{calories}")
    await state.finish()

@dp.message_handler(state=None)
async def all_massages(message: types.Message, state: FSMContext):
    print(f"Получено сообщение:{message.text}")
    await message.reply("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.exception(e)