from os import getenv
from os.path import dirname

import discord

from dotenv import load_dotenv


class BotClient(discord.Client):
    """Client for discord bot."""

    async def on_read(self) -> None:
        print("bot is ready.")

    async def on_message(self, message) -> None:
        print(message.content)


def main() -> None:
    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-2])
    load_dotenv(f"{BASE_PATH}/bot.env")
    token: str = getenv("TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = BotClient(intents=intents)
    client.run(token)


main()
