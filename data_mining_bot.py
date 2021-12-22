import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from data_mining import collect_date
import time

bot = Bot(token='your TOKEN', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🗡 Ножи', '🥊 Перчатки', '🏹 Снайперские витовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals='🗡 Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Please waiting...')

    collect_date()

    with open('finish.json') as f:
        data = json.load(f)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n" \
               f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
               f"{hbold('Цена: ')}{item.get('item_price')}$"

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🏹 Снайперские витовки'))
async def get_discount_guns(message: types.Message):
    await message.answer('Please waiting...')

    collect_date(cat_type=4)

    with open('finish.json') as f:
        data = json.load(f)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n" \
               f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
               f"{hbold('Цена: ')}{item.get('item_price')}$"

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='🥊 Перчатки'))
async def get_discount_glove(message: types.Message):
    await message.answer('Please waiting...')

    collect_date(cat_type=13)

    with open('finish.json') as f:
        data = json.load(f)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n" \
               f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
               f"{hbold('Цена: ')}{item.get('item_price')}$"

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
