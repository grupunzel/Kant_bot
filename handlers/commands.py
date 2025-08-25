import asyncio
import os
import traceback
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from config.logger import logger
from handlers.keyboard import main_roots_keyboard, info_keyboard
from handlers.dormitory_handlers.dormitory_keyboard import dormitory_keyboard
from aiogram.types import FSInputFile, CallbackQuery
from handlers.language_check_handlers.language_check_keyboard import language_check_keyboard

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer('Привет! С чем помочь?', reply_markup=main_roots_keyboard())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        raise

@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery):
    text = "🎓 Информация о университете"
    await callback.message.edit_text(text,
                         reply_markup=info_keyboard(),
                         parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data == "place")
async def location_info(callback: CallbackQuery):
    text = "📍 Местоположение корпуса"
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data == "dormitory")
async def dormitory_info(callback: CallbackQuery):
    text = "🏘️ Общежития"
    await callback.message.delete()
    await callback.message.answer(
        text,
        reply_markup=dormitory_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(F.data == "hospital")
async def medical_center_info(callback: CallbackQuery):
    text = """🏥 Медицинский центр"""
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data == "critical")
async def emergency_info(callback: CallbackQuery):
    text = "⚠️ Критические ситуации"
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery):
    text = "🇷🇺 Проверка русского языка"
    await callback.message.edit_text(text,
                                  parse_mode="Markdown",
                                  reply_markup=language_check_keyboard())
    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery):
    text = "Привет! С чем помочь?"
    await callback.message.edit_text(
        text,
        reply_markup=main_roots_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

