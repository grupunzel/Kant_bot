from aiogram import Router, F
from handlers.dormitory_handlers.dormitory_keyboard import back_to_addresses_keyboard
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from config.logger import logger

router = Router()

# Хэндлер для общежития №1
@router.callback_query(F.data == "dormitory_1")
async def dormitory_1_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 1 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-1.jpg')
        caption = "1"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 1 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 1: {e}")
        await callback.message.answer("Фото общежития №1 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 1: {e}")
        await callback.message.answer("Фото общежития №1 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_1_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №2
@router.callback_query(F.data == "dormitory_2")
async def dormitory_2_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 2 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-2.jpg')
        caption = "2"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 2 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 2: {e}")
        await callback.message.answer("Фото общежития №2 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 2: {e}")
        await callback.message.answer("Фото общежития №2 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_2_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №3
@router.callback_query(F.data == "dormitory_3")
async def dormitory_3_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 3 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-3.jpg')
        caption = "3"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 3 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 3: {e}")
        await callback.message.answer("Фото общежития №3 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 3: {e}")
        await callback.message.answer("Фото общежития №3 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_3_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №4
@router.callback_query(F.data == "dormitory_4")
async def dormitory_4_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 4 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-4.jpg')
        caption = "4"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 4 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 4: {e}")
        await callback.message.answer("Фото общежития №4 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 4: {e}")
        await callback.message.answer("Фото общежития №4 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_4_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №5
@router.callback_query(F.data == "dormitory_5")
async def dormitory_5_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 5 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-5.jpg')
        caption = "5"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 5 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 5: {e}")
        await callback.message.answer("Фото общежития №5 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 5: {e}")
        await callback.message.answer("Фото общежития №5 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_5_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №6
@router.callback_query(F.data == "dormitory_6")
async def dormitory_6_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 6 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-6.jpg')
        caption = "6"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 6 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 6: {e}")
        await callback.message.answer("Фото общежития №6 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 6: {e}")
        await callback.message.answer("Фото общежития №6 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_6_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №7
@router.callback_query(F.data == "dormitory_7")
async def dormitory_7_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 7 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-7.jpg')
        caption = "7"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 7 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 7: {e}")
        await callback.message.answer("Фото общежития №7 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 7: {e}")
        await callback.message.answer("Фото общежития №7 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_7_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №8
@router.callback_query(F.data == "dormitory_8")
async def dormitory_8_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 8 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-8.jpg')
        caption = "8"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 8 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 8: {e}")
        await callback.message.answer("Фото общежития №8 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 8: {e}")
        await callback.message.answer("Фото общежития №8 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_8_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №9
@router.callback_query(F.data == "dormitory_9")
async def dormitory_9_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 9 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-9.jpg')
        caption = "9"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 9 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 9: {e}")
        await callback.message.answer("Фото общежития №9 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 9: {e}")
        await callback.message.answer("Фото общежития №9 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_9_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()

# Хэндлер для общежития №10
@router.callback_query(F.data == "dormitory_10")
async def dormitory_10_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 10 photo")
        photo = FSInputFile('handlers/dormitory_handlers/dormitory_pictures/dormitory-10.jpg')
        caption = "10"
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_addresses_keyboard()
        )
        logger.info(f"Photo for dormitory 10 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 10: {e}")
        await callback.message.answer("Фото общежития №10 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 10: {e}")
        await callback.message.answer("Фото общежития №10 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_10_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()
