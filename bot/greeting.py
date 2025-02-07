from datetime import datetime

def get_greeting():
    """Функция для получения приветствия в зависимости от времени суток"""
    current_hour = datetime.now().hour

    if 6 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"