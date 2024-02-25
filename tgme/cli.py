import os

import typer
from dotenv import load_dotenv

from .messenger import send_telegram_message

load_dotenv()  # Load environment variables from .env file

app = typer.Typer()


@app.command()
def send(message: str):
    """
    Send a message using the Telegram bot.
    Args:
        message (str): The message to send.
    """
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        typer.echo("Telegram token and chat ID must be set as environment variables.")
        raise typer.Exit()

    response = send_telegram_message(token, chat_id, message)
    typer.echo(f"Message sent: {response}")
