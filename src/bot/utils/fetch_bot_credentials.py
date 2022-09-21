from os import getenv
from os.path import dirname, exists
from typing import NoReturn

from dotenv import load_dotenv

from src.data.bot_cred import BotCred
from utils.clog.clogger import Logger


def fetch_bc(log: Logger) -> BotCred | NoReturn:
    """Fetch the credentials of the bot in the .env file.

    Args:
        log -- the instance of Logger.

    Returns:
        The bot credentials with updated values.
    """

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-3])
    PATH: str = f"{BASE_PATH}/bot.env"

    if not exists(PATH):
        log.logger("E", "Bot credentials not found, aborting ...")
        raise SystemExit


    load_dotenv(f"{BASE_PATH}/bot.env")

    return BotCred(
        getenv("TOKEN")
    )
