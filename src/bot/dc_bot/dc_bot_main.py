from discord import Intents

from src.bot.dc_bot.dc_bot import BotClient
from src.data.dc_bot.dc_bot_cred import DCBotCred
from src.bot.shared.utils.dc_bot.fetch_bot_cred import fetch_bc
from src.utils.clog.clogger import Logger


async def dc_main(log: Logger) -> None:
    """Main module of the discord bot.

    Args:
        log -- instance of Logger.
    """

    bot_cred: DCBotCred = fetch_bc(log)

    intents = Intents.default()
    intents.message_content = True

    client = BotClient(log, intents=intents)
    await client.run(bot_cred.token)
