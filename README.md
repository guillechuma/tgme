# tgme - Telegram Messaging Bot

tgme is a Python package that provides an easy way to send messages via a Telegram bot. It includes both a library for use in Python scripts and a command-line interface (CLI) for direct message sending from the terminal.

## Features

- Send messages to a Telegram chat using your bot token and chat ID.
- Command-line interface for quick and easy message sending.
- Easy integration into Python scripts for automated messaging.

## Installation

To install tgme, follow these steps:

1. Clone this repo

2. Go inside the package and build with poetry

```
cd tgme
potry build
```

3. Install package with pip

```
pip install -e .
```

## Configuration

Before using TGMe, you need to set up your Telegram bot token and chat ID as environment variables:

```
export TELEGRAM_TOKEN=your_bot_token
export TELEGRAM_CHAT_ID=your_chat_id
```

Alternatively, you can use a `.env` file in your project directory:

```
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## Usage

### As a python package

Import `send_telegram_message` from the package and use it in your scripts:

```
from tgme.message import send_telegram_message

token = "your_telegram_bot_token"
chat_id = "your_chat_id"
message = "Hello from TGMe!"

send_telegram_message(token, chat_id, message)
```

### As a CLI tool

Once installed, you can use the `tgme` command directly from the command line:

```
tgme send --message "Your message here"
```

## Development

To set up a development environment:

1. Clone repository

2. Install the dependencies:

```
poetry install
```

3. Activate the virtual environment:

```
poetry shell
```

## Contributing

Contributions to TGMe are welcome! Feel free to report issues or submit pull requests.
