import logging
import os

import requests
import telegram
from dotenv import load_dotenv

from logs import TelegramLogHandler


if __name__ == "__main__":
    load_dotenv()
    DVMN_API_TOKEN = os.getenv("DVMN_API_TOKEN")
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
    TG_BOT_OWNER_CHAT_ID = os.getenv("TG_BOT_OWNER_CHAT_ID")

    bot = telegram.Bot(token=TG_BOT_TOKEN)

    logging.basicConfig(
        handlers=[TelegramLogHandler(tg_bot=bot, chat_id=TG_BOT_OWNER_CHAT_ID)]
    )

    logging.warning("Бот запущен")

    params = {"timesamp": None}

    while True:

        try:
            try:
                response = requests.get(
                    "https://dvmn.org/api/long_polling/",
                    headers={"Authorization": f"Token {DVMN_API_TOKEN}"},
                    params=params,
                    timeout=5,
                )

            except (requests.ReadTimeout, requests.ConnectionError):
                continue

            if not response.ok:
                continue

            reviews_details = response.json()

            status = reviews_details.get("status")

            if status == "timeout":
                params["timestamp"] = reviews_details.get("timestamp_to_request")

            elif status == "found":
                params["timestamp"] = reviews_details.get("last_attempt_timestamp")

                # Assuming multiple reviews cannot be posted at the exact same moment
                latest_attempt = reviews_details["new_attempts"][0]
                if latest_attempt:

                    lesson_title = latest_attempt["lesson_title"]
                    lesson_url = latest_attempt["lesson_url"]

                    text_header = f'У вас проверили работу <a href="{lesson_url}">"{lesson_title}"</a>'

                    is_successful = not latest_attempt["is_negative"]

                    text_review_result = (
                        "Преподавателю все понравилось, можно приступать к следующему уроку."
                        if is_successful
                        else "К сожалению, в работе нашлись ошибки."
                    )

                    bot.send_message(
                        text=f"{text_header}\n\n{text_review_result}",
                        chat_id=TG_BOT_OWNER_CHAT_ID,
                        parse_mode=telegram.ParseMode.HTML,
                    )

        except Exception:
            logging.exception("Бот упал с ошибкой")
