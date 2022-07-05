# Review Notification Chatbot for dvmn.org

 This is a Telegram chatbot for sending notifications about reviewed home assignemnts on [dvmn.org](https://dvmn.org/). It also sends all errors occured during its lifetime.

Chatbot uses Telegram API via [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library for sending messages. It uses [dvmn.org API](https://dvmn.org/api/docs/) for receiving updates on home assignment review status.

## Usage

### Local usage

1. Install required python libraries `pip install -r requirements.txt`
1. Copy/move `.env.template` to `.env`
1. Fill in the following environment variables in `.env`
    - `DVMN_API_TOKEN` - [dvmn.org](https://dvmn.org/api/docs/) token
    - `TG_BOT_OWNER_CHAT_ID` - Telegram chat (user) ID. Can be obtained from [@userinfobot](https://t.me/userinfobot)
    - `TG_BOT_TOKEN` - Telegram Bot token. Generated during bot creation with [@BotFather](https://t.me/BotFather)
1. Run with: `python main.py`
