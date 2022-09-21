from os import getenv
from os.path import dirname, exists
from typing import NoReturn

from dotenv import load_dotenv

from pkg_data.dc_bot_cred import DCBotCred
from utils.clog.clogger import Logger


def fetch_bc(log: Logger) -> DCBotCred | NoReturn:
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

    token: str = token_ (token_ := getenv("TOKEN")) if not None else "EMPTY"

    return DCBotCred(token)
