# start.py используется для того, чтобы хранить обработчики конкретных команд 
# («Привет», «Помощь», «Мой ID») в отдельном файле, а не в main.py. Благодаря 
# этому main.py остаётся «сердцем» (только запуск и регистрация), а вся логика 
# реакции на команды лежит в папке handlers — это «мозг» бота.

import sys
from pathlib import Path

# Добавляем родительскую директорию в путь поиска модулей
sys.path.append(str(Path(__file__).parent.parent))

from vkbottle.bot import Bot, Message
import bot_text
from utils.logger import logger

async def register_handlers(bot: Bot):
    """Регистрирует обработчики команд"""

    @bot.on.message(text="Привет")
    async def hello_handler(message: Message):
        logger.info(f"Пользователь {message.from_id} поздоровался")
        await message.answer(bot_text.HELLO_MESSAGE)

    @bot.on.message(text="Помощь")
    async def help_handler(message: Message):
        logger.info(f"Пользователь {message.from_id} вызвал /help")
        await message.answer(bot_text.HELP_MESSAGE)

    @bot.on.message(text="Мой ID")
    async def id_handler(message: Message):
        
        user_id = message.from_id
        users = await message.ctx_api.users.get(
        user_ids=user_id)
        first_name = users[0].first_name
        await message.answer(f"Привет, {first_name}!")

        # logger.info(f"Пользователь {message.from_id} запросил свой ID")
        # await message.answer(bot_text.ID_MESSAGE.format(user_id=message.from_id))