import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories' )
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button_1, button_2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['start'])
async def start_massege(message: types.Message):
    await message.answer("Привет!Я бот помагающий твоему здоровью!")

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb)
    await answer()

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@dp.callback_query_handler(text = ['calories'])
async def set_age(call: types.Message):
    await call.message.answer("Введите свой возраст:")
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