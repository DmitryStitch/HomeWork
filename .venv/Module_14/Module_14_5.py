import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, add_user, is_included
initiate_db()

api = "8190268705:AAEvLMdJ0uj_6LJ7Pm8oXWH4duV4Sxe7Ar4"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calc = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
button_reg = KeyboardButton(text='Регистрация')
reply_keyboard.add(button_calc, button_info, button_buy, button_reg)

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_расчет = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_формулы = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_расчет, button_формулы)

inline_buy = InlineKeyboardMarkup(resize_keyboard=True)
Product1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
Product2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
Product3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
Product4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
inline_buy.add(Product1, Product2, Product3, Product4)


@dp.message_handler(commands=['start'])
async def start_massege(message):
    await message.answer("Привет! Я - бот, помогающий вашему здоровью! Выберите пункт из меню, чтобы продолжить работу", reply_markup=reply_keyboard)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(text='Регистрация')
async def registr(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    with sqlite3.connect("initiate_db.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        user_exists = cursor.fetchone()

    if user_exists:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username=username)
        await message.answer("Введите ваш email: ")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите ваш возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
        await state.update_data(age=message.text)
        data = await state.get_data()
        username = data['username']
        email = data['email']
        age = data['age']
        add_user(username, email, age)
        await message.answer("Регистрация завершена")
        await state.finish()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products or []:  # Обработка пустого списка
        title, description, price = product[1], product[2], product[3]
        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price}")
        with open(f'{product[1]}.jpg','rb') as img:
            await message.answer_photo(img)
        await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(" Вы успешно преобрели продукт!")
    await call.answer()

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