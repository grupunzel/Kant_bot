from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_roots_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎓 Информация про университет", callback_data="info")],
             [InlineKeyboardButton(text="📍 Местоположение корпуса", callback_data="place")],
             [InlineKeyboardButton(text="🏘️ Общежития", callback_data="home")],
             [InlineKeyboardButton(text="🏥 Медцентр", callback_data="hospital")],
             [InlineKeyboardButton(text="⚠️ Критические ситуации", callback_data="critical")],
             [InlineKeyboardButton(text="🇷🇺 Проверка русского языка", callback_data="language_check")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def info_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")],
        [InlineKeyboardButton(text="💰 Стипендии", callback_data="scholarship")],
        [InlineKeyboardButton(text="📞 Контакты учебного офиса", callback_data="office_contacts")],
        [InlineKeyboardButton(text="🌍 Визово-миграционный центр", callback_data="visa_center")]
    ])

