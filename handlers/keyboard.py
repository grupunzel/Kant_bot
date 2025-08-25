from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Основная клавиатура
def main_roots_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎓 Информация про университет", callback_data="info")],
            [InlineKeyboardButton(text="📍 Местоположение корпуса", callback_data="place")],
            [InlineKeyboardButton(text="🏘️ Общежития", callback_data="dormitory")],
            [InlineKeyboardButton(text="🏥 Медцентр", callback_data="hospital")],
            [InlineKeyboardButton(text="⚠️ Критические ситуации", callback_data="critical")],
            [InlineKeyboardButton(text="🇷🇺 Проверка русского языка", callback_data="language_check")]
        ]
    )

#Клавиатура, открывающаяся при нажатии на информацию про университет
def info_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")],
        [InlineKeyboardButton(text="💰 Стипендии", callback_data="scholarship")],
        [InlineKeyboardButton(text="📞 Контакты учебного офиса", callback_data="office_contacts")],
        [InlineKeyboardButton(text="🌍 Визово-миграционный центр", callback_data="visa_center")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

#Клавиатура, открывающаяся при нажатии на общежития
def dormitory_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Заселение в общежитие", callback_data="dormitory_check-in")],
        [InlineKeyboardButton(text="💵 Оплата", callback_data="dormitory_payment")],
        [InlineKeyboardButton(text="📖 Правила проживания", callback_data="dormitory_rules")],
        [InlineKeyboardButton(text="🧺 Прачечная", callback_data="dormitory_laundry")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

def dormitory_check_in_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Нет сертификата прививок или флюорографии", callback_data="no_certificate")],
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])

def back_to_dormitory_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])