from aiogram import Bot, Dispatcher
from config.settings import settings
from config.logger import logger
from handlers import commands, messages, dormitory_handlers
from handlers.dormitory_handlers import dormitory_rules_handler


async def main():
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(messages.router)
    dp.include_router(dormitory_handlers.router)

    try:
        logger.info('Bot started')
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f'Bot crashed: {e}')
    finally:
        await bot.session.close()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
