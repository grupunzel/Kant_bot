from aiogram import Router, types
from aiogram.filters import CommandStart
from config.logger import logger
import traceback

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer('Привет! Это бот ... ')
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        raise

