# main.py используется для того, чтобы быть «сердцем» бота: 
# в нём мы создаём экземпляр бота, загружаем токен,
# настраиваем логирование и регистрируем все обработчики из папки handlers. 
# Благодаря этому сам main.py остаётся коротким и читаемым, 
# а вся логика лежит в отдельных модулях.

import asyncio
from vkbottle import Bot
from config import BOT_TOKEN
from utils.logger import logger
from handlers import start, echo

async def main():
    """Основная функция запуска бота"""

    # Создаём бота
    bot = Bot(token=BOT_TOKEN)

    logger.info("🚀 Запуск бота...")
    logger.info(f"Token: {BOT_TOKEN[:20]}...")

    # Регистрируем все обработчики
    await start.register_handlers(bot)
    await echo.register_handlers(bot)

    logger.info("✅ Все обработчики зарегистрированы")
    logger.info("🤖 Бот запущен и слушает сообщения...")

    # Запускаем бота
    await bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())