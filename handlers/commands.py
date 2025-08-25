import asyncio
import os
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from config.logger import logger
from handlers.keyboard import main_roots_keyboard, info_keyboard
import traceback
from aiogram.types import FSInputFile

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer('Привет! С чем помочь?', reply_markup=main_roots_keyboard())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        raise

@router.message(F.text == "🎓Информация про университет")
async def university_info(message: types.Message):
    text = "🎓 Информация о университете"
    await message.answer(text,
                         reply_markup=info_keyboard(),
                         parse_mode="Markdown")


@router.message(F.text == "📍 Местоположение корпуса")
async def location_info(message: types.Message):
    text = "📍 Местоположение корпуса"
    await message.answer(text, parse_mode="Markdown")


@router.message(F.text == "🏘️ Общежития")
async def dormitory_info(message: types.Message):
    text = "🏘️ Общежития"
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text == "🏥 Медцентр")
async def medical_center_info(message: types.Message):
    text = """🏥 *Медицинский центр"""
    await message.answer(text, parse_mode="Markdown")


@router.message(F.text == "⚠️ Критические ситуации")
async def emergency_info(message: types.Message):
    text =  "⚠️ Критические ситуации"
    await message.answer(text, parse_mode="Markdown")


@router.message(F.text == "🇷🇺 Проверка русского языка")
async def language_check_info(message: types.Message):
    text = "🇷🇺 Проверка русского языка"
    await message.answer(text, parse_mode="Markdown")


@router.message()
async def unknown_command(message: types.Message):
    await message.reply('Раздел не найден.\nВыберите интересующий раздел:', reply_markup=main_roots_keyboard())