from os import getenv
from os.path import dirname, exists
from typing import NoReturn

from dotenv import load_dotenv

from src.utils.log.logger import Logger


def fetch_bc(log: Logger) -> dict[str, str] | NoReturn:
    """Fetch the credentials of the bot in the .env file.

    Args:
        log -- the instance of Logger.

    Returns:
        A map of values of the the bot credentials.
    """

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-2])
    PATH: str = f"{BASE_PATH}/bot.env"

    if not exists(PATH):
        log.logger("E", "Bot credentials not found, aborting ...")
        raise SystemExit

    bot_cred: dict[str, str]

    load_dotenv(f"{BASE_PATH}/bot.env")
    bot_cred["TOKEN"] = getenv("TOKEN")

    return bot_cred
