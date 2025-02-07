IMEI Check Bot

                  Описание
Этот проект включает два компонента:
1. Telegram-бот для проверки IMEI через FastAPI сервер.
2. FastAPI сервер для взаимодействия с внешним сервисом IMEI Check.

               Структура проекта
Проект состоит из двух основных частей:
1. Telegram Bot (bot/bot.py)
2. FastAPI сервер (app/main.py, app/imei_service.py)
   
В проекте так же вынесены в отдельные файлы зависимости и настройки(url,api,token):
1. Конфигурационные настройки (config.py)
2. Зависимости (requirements.txt)


            Запуск проекта
1. Установка всех необходимых зависимостей:
    pip install -r requirements.txt

2. Запуск сервера FastAPI:
   uvicorn app.main:app --reload 

   Запуск Telegram-бота:
   python -m bot.bot

Принцип работы приложение:
1. Пользователь отправляет IMEI в Telegram боте.
2. Бот перенаправляет IMEI на сервер FastAPI для проверки.
3. Сервер FastAPI отправляет запрос вo внешний сервис (IMEI Check) для получения информации об устройстве.
4. Сервер возвращает результат проверки обратно боту.
5. Бот отображает результат пользователю.

Инструкция для получения токенов:
1. https://imeicheck.net/developer-api (API_TOKEN_SANDBOX)
2. https://telegram.me/BotFather (TELEGRAM_BOT_TOKEN)
3. https://t.me/getmyid_bot (WHITE_LIST_USERS)
