# main_kb.py используется для того, чтобы создавать и хранить клавиатуры 
# (кнопки, которые бот показывает пользователю) отдельно от логики. 
# Благодаря этому при изменении кнопок не нужно трогать обработчики,
# а одну и ту же клавиатуру можно переиспользовать в нескольких местах 
# (например, и в приветствии, и в эхо-ответе). Папка keyboards — это «лицо» бота.

from vkbottle import Keyboard, KeyboardButtonColor, Text

def get_main_keyboard():
    """Создаёт и возвращает основную клавиатуру"""
    keyboard = Keyboard(one_time=False, inline=False)

    # Первый ряд
    keyboard.add(Text("Привет"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Помощь"), color=KeyboardButtonColor.SECONDARY)

    # Второй ряд
    keyboard.row()
    keyboard.add(Text("Мой ID"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Очистить"), color=KeyboardButtonColor.NEGATIVE)

    return keyboard.get_json()