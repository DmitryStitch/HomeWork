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

inline_buy = InlineKeyboardMarkup(resize_keyboard=True)
Product1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
Product2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
Product3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
Product4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
inline_buy.add(Product1, Product2, Product3, Product4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_massege(message: types.Message):
    reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calc = KeyboardButton(text='Рассчитать')
    button_info = KeyboardButton(text='Информация')
    button_buy = KeyboardButton(text='Купить')
    reply_keyboard.add(button_calc, button_info)
    reply_keyboard.add(button_buy)
    await message.answer("Привет! Я бот, помогающий вашему здоровью! Выберите пункт из меню, чтобы продолжить работу", reply_markup=reply_keyboard)

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
        await message.answer(f'Название: Product{1} | Описание: описание {1} | Цена: {1 * 100}')
        with open(f'{1}.jpg', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(f'Название: Product{2} | Описание: описание {2} | Цена: {2 * 100}')
        with open(f'{2}.jpg', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(f'Название: Product{3} | Описание: описание {3} | Цена: {3 * 100}')
        with open(f'{3}.jpg', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(f'Название: Product{4} | Описание: описание {4} | Цена: {4 * 100}')
        with open(f'{4}.jpg', 'rb') as img:
            await message.answer_photo(img)
        await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
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