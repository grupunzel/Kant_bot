from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_roots_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎓Информация про университет", callback_data="info")],
             [KeyboardButton(text="📍Местоположение корпуса", callback_data="place")],
             [KeyboardButton(text="🏘️Общежития", callback_data="home")],
             [KeyboardButton(text="🏥Медцентр", callback_data="hospital")],
             [KeyboardButton(text="⚠️Критические ситуации", callback_data="critical")],
             [KeyboardButton(text="🇷🇺Проверка русского языка", callback_data="language_check")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

