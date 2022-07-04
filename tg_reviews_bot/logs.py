import logging
import os


class TelegramLogHandler(logging.Handler):
    def __init__(self, tg_bot, chat_id=None):
        super().__init__()
        self.chat_id = chat_id or os.getenv("TG_BOT_OWNER_CHAT_ID")
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)

        self.tg_bot.send_message(
            chat_id=self.chat_id,
            text=log_entry,
        )
