from typing import Any

from discord import Client, Intents

from utils.clog.clogger import Logger


class BotClient(Client):
    """Client for discord bot."""

    def __init__(
            self, log: Logger, *, intents: Intents, **options: Any
        ) -> None:
        self.log = log
        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        self.log.logger("I", "Bot is ready.")

    async def on_message(self, message: Any) -> Any:
        print(f"\033[36mMESS\033[0m\t {message.content}")
