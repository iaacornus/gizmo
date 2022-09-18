from discord import Client

class BotClient(Client):
    """Client for discord bot."""

    async def on_read(self) -> None:
        print("bot is ready.")

    async def on_message(self, message) -> None:
        print(message.content)
