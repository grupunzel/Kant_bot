from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

# Хэндлер для расписания
@router.callback_query(F.data == "schedule")
async def schedule_handler(callback: CallbackQuery):
    text = ""
    await callback.message.reply(text)
    await callback.answer()

# Хэндлер для стипендий
@router.callback_query(F.data == "scholarship")
async def scholarship_handler(callback: CallbackQuery):
    text = ""
    await callback.message.reply(text)
    await callback.answer()

# Хэндлер для контактов учебного офиса
@router.callback_query(F.data == "office_contacts")
async def office_contacts_handler(callback: CallbackQuery):
    text = ""
    await callback.message.reply(text)
    await callback.answer()

# Хэндлер для визово-миграционного центра
@router.callback_query(F.data == "visa_center")
async def visa_center_handler(callback: CallbackQuery):
    text = ""
    await callback.message.reply(text)
    await callback.answer()