import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_расчет = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_формулы = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_расчет, button_формулы)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_massege(message: types.Message):
    reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calc = KeyboardButton(text='Рассчитать')
    button_info = KeyboardButton(text='Информация')
    reply_keyboard.add(button_calc, button_info)
    await message.answer("Привет! Я бот, помогающий вашему здоровью! Выберите 'Рассчитать', чтобы перейти к рассчету", reply_markup=reply_keyboard)

@dp.message_handler(text='Рассчитать')
async def show_inline_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 х рост (см) – 5 х возраст (лет) + 5")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.Message):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
        weight = int(message.text)
        await state.update_data(weight=weight)
        data = await state.get_data()
        age = data.get('age')
        growth = data.get('growth')
        weight = data.get('weight')
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f"Ваша норма калорий: {calories}")
        await state.finish()


@dp.message_handler(state=None)
async def all_massages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logging.exception(e)