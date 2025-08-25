from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Клавиатура, открывающаяся при нажатии на общежития
def dormitory_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Заселение в общежитие", callback_data="dormitory_check-in")],
        [InlineKeyboardButton(text="💵 Оплата", callback_data="dormitory_payment")],
        [InlineKeyboardButton(text="📍 Адреса общежитий", callback_data="dormitory_address")],
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

def dormitory_addresses_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="№ 1", callback_data="dormitory_1")],
        [InlineKeyboardButton(text="№ 2", callback_data="dormitory_2")],
        [InlineKeyboardButton(text="№ 3", callback_data="dormitory_3")],
        [InlineKeyboardButton(text="№ 4", callback_data="dormitory_4")],
        [InlineKeyboardButton(text="№ 5", callback_data="dormitory_5")],
        [InlineKeyboardButton(text="№ 6", callback_data="dormitory_6")],
        [InlineKeyboardButton(text="№ 7", callback_data="dormitory_7")],
        [InlineKeyboardButton(text="№ 8", callback_data="dormitory_8")],
        [InlineKeyboardButton(text="№ 9", callback_data="dormitory_9")],
        [InlineKeyboardButton(text="№ 10", callback_data="dormitory_10")],
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])

def back_to_addresses_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory_address")]
    ])
