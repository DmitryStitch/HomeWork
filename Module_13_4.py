import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(commands = ['start'])
async def start_massege(massege: types.Message):
    await massege.answer("Привет! Чтобы получить расчет калорий, напиши 'Calories'.")

@dp.message_handler(text = ['Calories'])
async def set_age(massege: types.Message):
    await massege.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(massege: types.Message, state: FSMContext):
    await state.update_data(age = int(massege.text))
    await massege.answer("Введите свой рост (в см): ")
    await UserState.next()

@dp.message_handler(state = UserState.growth)
async def set_weight(massege: types.Message, state: FSMContext):
    await state.update_data(growth = int(massege.text))
    await massege.answer("Введите свой вес (в кг): ")
    await UserState.next()

@dp.message_handler(state = UserState.weight)
async def send_calories(massege: types.Message, state: FSMContext):
    await state.update_data(weight = int(massege.text))
    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')

    calories = 10 * weight + 6.25 * growth + 5 * age + 5

    await massege.answer(f"Ваша норма каллорий:{calories}")
    await state.finish()

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.exception(e)