from discord import Intents

from src.data.bot_cred import BotCred
from src.bot.bot import BotClient
from src.bot.utils.fetch_bot_credentials import fetch_bc
from src.utils.log.logger import Logger


def main() -> None:
    """Main module of AI."""

    log: Logger = Logger()

    bot_cred: BotCred = fetch_bc(log)

    intents = Intents.default()
    intents.message_content = True

    client = BotClient(intents=intents)
    client.run(bot_cred.token)
