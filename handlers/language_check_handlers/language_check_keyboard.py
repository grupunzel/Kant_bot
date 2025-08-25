from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_check_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎧 Аудирование", callback_data="listening")],
        [InlineKeyboardButton(text="📝 Грамматика", callback_data="grammar")],
        [InlineKeyboardButton(text="🎤 Говорение", callback_data="speaking")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])