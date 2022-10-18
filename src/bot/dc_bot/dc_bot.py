from typing import Any, Optional

from discord import Client, Intents
from discord.errors import HTTPException

from src.bot.shared.utils.dc_bot.filter import filter
from src.utils.clog.clogger import Logger


class BotClient(Client):
    """Client for discord bot."""

    def __init__(
            self,
            log: Logger,
            commands: dict[str, str | list[str]],
            ref_uid: int,
            *,
            intents: Intents,
            **options: Any
        ) -> None:
        self.log = log
        self.commands = commands
        self.ref_uid = ref_uid

        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        self.log.logger("I", "Bot is ready.")

    async def on_message(self, message: Any) -> Any:
        feedback: Optional[str] = filter(
                self.log,
                message.content,
                self.commands,
                int(message.author.id),
                int(self.ref_uid)
            )
        try:
            if feedback is not None:
                await message.channel.send(feedback)
        except HTTPException:
            self.log.logger(
                "e", f"Cannot send the feedback: {feedback}, skipping ..."
            )
