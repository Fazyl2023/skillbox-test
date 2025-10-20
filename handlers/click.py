from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Создаем роутер для команды start
router = Router()

@router.message()
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Перейти на сайт фильмов", url="https://imdb.com")]
        ]
    )
    
    await message.answer(
        "Нажми кнопку для перехода на сайт:",
        reply_markup=keyboard
    )

