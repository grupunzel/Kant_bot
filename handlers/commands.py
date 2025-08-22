from aiogram import Router, types, F
from aiogram.filters import CommandStart
from config.logger import logger
from handlers.keyboard import main_roots_keyboard, info_keyboard
import traceback
from aiogram.types import FSInputFile
import os
router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer('Привет! С чем помочь?', reply_markup=main_roots_keyboard())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        raise

# Хэндлер для информации про университет
@router.message(F.text == "🎓Информация про университет")
async def university_info(message: types.Message):
    text = "🎓 Информация о университете"
    await message.answer(text,
                         reply_markup=info_keyboard(),
                         parse_mode="Markdown")

@router.message(F.text == "📍Местоположение корпуса")
async def location_info(message: types.Message):
    text = """📍 *Местоположение корпусов*

• Главный корпус: [адрес и карта]
• Корпус А: [адрес и карта] 
• Корпус Б: [адрес и карта]
• Спортивный комплекс: [адрес и карта]"""

    await message.answer(text, parse_mode="Markdown")



@router.message(F.text == "🏘️Общежития")
async def dormitory_info(message: types.Message):

    await message.reply_document(document=FSInputFile("handlers/info_files/ОБЩЕЖИТИЕ.pdf"),
                                 caption="Чтобы ознакомиться с подробной информацией, откройте прикрепленный ниже файл.")


@router.message(F.text == "🏥Медцентр")
async def medical_center_info(message: types.Message):
    text = """🏥 *Медицинский центр*

• Режим работы: пн-пт 9:00-18:00
• Телефон: +7 (XXX) XXX-XX-XX
• Услуги: первая помощь, консультации
• Запись на прием"""

    await message.answer(text, parse_mode="Markdown")


@router.message(F.text == "⚠️Критические ситуации")
async def emergency_info(message: types.Message):
    text = ''
    await message.answer(text, parse_mode="Markdown")


@router.message(F.text == "🇷🇺Проверка русского языка")
async def language_check_info(message: types.Message):
    text = """🇷🇺 *Проверка русского языка*

Здесь будет информация о:
• Тестировании для иностранных студентов
• Подготовительных курсах
• Расписании экзаменов
• Контактах языкового центра"""

    await message.answer(text, parse_mode="Markdown")


@router.message()
async def unknown_command(message: types.Message):
    await message.reply('Раздел не найден.\nВыберите интересующий раздел:', reply_markup=main_roots_keyboard())