from typing import Any

from discord import Client, Intents

from src.bot.shared.utils.dc_bot.filter import filter
from src.utils.clog.clogger import Logger


class BotClient(Client):
    """Client for discord bot."""

    def __init__(
            self,
            log: Logger,
            commands: dict[str, str | list[str]],
            *,
            intents: Intents,
            **options: Any
        ) -> None:
        self.log = log
        self.commands = commands
        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        self.log.logger("I", "Bot is ready.")

    async def on_message(self, message: Any) -> Any:
        feedback: list[str] | str = filter(
                self.log, message.content, self.commands
            )
        if feedback is not None:
            await message.channel.send(feedback)
