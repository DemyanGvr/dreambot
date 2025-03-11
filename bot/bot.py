import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "8107472199:AAFMbroM47_8tzWpXVmiXKU27ssd8tzKyJk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обычная (Reply) клавиатура без ссылок
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔗 Регистрация со спецпредложением")],
        [KeyboardButton(text="💬 Приватный чат с инсайдерской схемой")]
    ],
    resize_keyboard=True
)

# Inline-клавиатура для кнопки с ссылкой
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💬 Приватный чат", url="https://t.me/azamatend")]
    ]
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("👋 Добро пожаловать! Выберите один из вариантов:", reply_markup=reply_keyboard)
    await message.answer("💬 Нажмите кнопку ниже, чтобы перейти в приватный чат:", reply_markup=inline_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
