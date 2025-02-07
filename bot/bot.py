import requests
import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TELEGRAM_BOT_TOKEN,API_TOKEN_SANDBOX, API_URL, WHITE_LIST_USERS
from bot.greeting import get_greeting


bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

def get_check_button():
    """Функция get_check_button создаёт кнопку: 'Проверить новый IMEI'"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проверить новый IMEI", callback_data="check_new_imei")]
    ])

@dp.callback_query(lambda imei: imei.data == "check_new_imei")
async def check_new_imei(callback_query: types.CallbackQuery):
    """Функция check_new_imei обрабатывает нажатие на кнопку для проверки нового IMEI"""
    await callback_query.answer()
    await callback_query.message.answer("Введите новый IMEI для проверки.")


@dp.message(Command("start"))
async def start(message: types.Message):
    """Функция start, отвечающая за обработку команды /start"""
    await message.answer(
        f"{get_greeting()} {message.from_user.first_name}!\nОтправьте IMEI для проверки."
    )


@dp.message()
async def check_imei(message: types.Message):
    """Функция check_imei, проверяет IMEI и взаимодействует с API"""
    user_id = message.from_user.id
    if user_id not in WHITE_LIST_USERS:
        await message.answer("У вас нет доступа к этому боту.")
        return

    imei = message.text.strip()
    if not imei.isdigit() or len(imei) not in [14, 15]:
        await message.answer(
            "Введите корректный IMEI (14-15 цифр).",
            reply_markup=get_check_button()
        )
        return

    imei_info = {"imei": imei, "token": API_TOKEN_SANDBOX}
    response = requests.post(API_URL, json=imei_info)

    if response.status_code == 200:
        data = response.json()
        await message.answer(
            f"Данные IMEI:\n{json.dumps(data, indent=2)}",
            reply_markup=get_check_button()
        )
    else:
        await message.answer("Ошибка при проверке IMEI.")


async def main():
    """Запуск бота с помощью start_polling"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
