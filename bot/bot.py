import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8107472199:AAFMbroM47_8tzWpXVmiXKU27ssd8tzKyJk"

dp = Dispatcher()
bot = Bot(token=8107472199:AAFMbroM47_8tzWpXVmiXKU27ssd8tzKyJk)

# Создаём клавиатуру с 2 кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔗 Регистрация со спецпредложением")],
        [KeyboardButton(text="💬 Приватный чат с инсайдерской схемой")]
    ],
    resize_keyboard=True
)

# Обрабатываем команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.text == "/start":
        await message.answer("👋 Добро пожаловать! Выберите один из вариантов:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
