# echo.py используется для того, чтобы хранить «запасные» обработчики: 
# реакцию на кнопку «Очистить» и эхо-заглушку на любое сообщение, 
# которое не подошло ни под одну команду. Благодаря этому логика 
# «что делать с непонятным сообщением» изолирована от конкретных 
# команд и легко меняется, не затрагивая start.py.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle.bot import Bot, Message
from vkbottle import EMPTY_KEYBOARD
import bot_text
from utils.logger import logger
from keyboards.main_kb import get_main_keyboard

async def register_handlers(bot: Bot):
    """Регистрирует обработчик очистки и эхо-заглушку"""

    @bot.on.message(text="Очистить")
    async def clear_handler(message: Message):
        logger.info(f"Пользователь {message.from_id} очистил клавиатуру")
        await message.answer(bot_text.CLEAR_MESSAGE, keyboard=EMPTY_KEYBOARD)

    @bot.on.message()
    async def main_handler(message: Message):
        # Приводим текст к нижнему регистру и убираем пробелы по краям
        text = (message.text or "").lower().strip()

        # Проверяем, не приветствие ли это
        if text in bot_text.GREETING_WORDS:
            logger.info(f"Пользователь {message.from_id} поздоровался: {text}")
            await message.answer(bot_text.HELLO_MESSAGE, keyboard=get_main_keyboard())
            return

        # Если это не приветствие — отвечаем «не понял»
        logger.info(f"Получено сообщение от {message.from_id}: {text[:50] if text else 'пусто'}")
        await message.answer(
            bot_text.UNKNOWN_MESSAGE,
            keyboard=get_main_keyboard()
        )