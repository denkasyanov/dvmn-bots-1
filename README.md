# Бот для уведомлений о проверках ДЗ dvmn.org

## Использование

### Запуск локально

1. Установить зависимости с помощью `pip install -r requirements.txt`
1. Скопировать/переименовать `.env.template` в `.env`
1. Заполнить в нем переменные окружения: токен для API dvmn.org и информацию для бота:
    - `DVMN_API_TOKEN` - токен [dvmn.org](https://dvmn.org/api/docs/) 
    - `TG_BOT_OWNER_CHAT_ID` - ID чата (пользователя) в телеграме, можно узнать у [@userinfobot](https://t.me/userinfobot)
    - `TG_BOT_TOKEN` - токен бота, генерируется при создании бота через [@BotFather](https://t.me/BotFather)
1. Запустить: `python main.py`
