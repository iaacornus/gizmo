from os import getenv
from os.path import dirname, exists
from dotenv import load_dotenv

from src.data.dc_bot.dc_bot_cred import DCBot
from src.utils.clog.clogger import Logger


def fetch_bc(log: Logger) -> DCBot:
    """Fetch the credentials of the bot in the .env file.

    Args:
        log -- the instance of Logger.

    Returns:
        The bot credentials with updated values.
    """

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-5])
    PATH: str = f"{BASE_PATH}/bot.env"

    if not exists(PATH):
        log.logger("E", "Bot credentials not found, aborting ...")
        return False

    load_dotenv(f"{BASE_PATH}/bot.env")

    return DCBot(
        getenv("TOKEN"),
        getenv("UID")
    )
