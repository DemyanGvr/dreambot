import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "8107472199:AAFMbroM47_8tzWpXVmiXKU27ssd8tzKyJk"

bot = Bot(token=TOKEN)
dp = Dispatcher()  # В Aiogram 3.x Dispatcher создаётся без параметров

# Создаём клавиатуру с 2 кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔗 Регистрация со спецпредложением")],
        [KeyboardButton(text="💬 Приватный чат с инсайдерской схемой")]
    ],
    resize_keyboard=True
)

# Обрабатываем команду /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("👋 Добро пожаловать! Выберите один из вариантов:", reply_markup=keyboard)

async def main():
    dp.include_router(dp)  # Подключаем диспетчер
    await dp.start_polling(bot)  # Запуск бота

if __name__ == "__main__":
    asyncio.run(main())
