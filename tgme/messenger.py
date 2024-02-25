from urllib.parse import urlencode

import requests


def send_telegram_message(token: str, chat_id: str, message: str) -> dict:
    """
    Send a message via Telegram bot using a GET request.

    Args:
        token (str): Telegram bot token.
        chat_id (str): Chat ID to send the message to.
        message (str): The message to send.

    Returns:
        dict: The response from Telegram API.
    """
    base_url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    url = f"{base_url}?{urlencode(params)}"
    response = requests.get(url)
    return response.json()
