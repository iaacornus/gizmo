from discord import Intents

from src.bot.dc_bot.dc_bot import BotClient
from src.data.dc_bot_cred import DCBotCred
from src.bot.shared.utils.dc_bot.fetch_bot_cred import fetch_bc
from src.utils.clog.clogger import Logger


def main() -> None:
    """Main module of AI."""

    log: Logger = Logger()

    bot_cred: DCBotCred = fetch_bc(log)

    intents = Intents.default()
    intents.message_content = True # type: ignore

    client = BotClient(log, intents=intents)
    client.run(bot_cred.token)


if __name__ == "__main__":
    main()
