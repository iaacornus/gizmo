from json import load
from os.path import dirname
from typing import NoReturn, TextIO
from discord import Intents

from src.bot.dc_bot.dc_bot import BotClient
from src.data.dc_bot.dc_bot_cred import DCBot
from src.bot.shared.utils.dc_bot.fetch_bot_cred import fetch_bc
from src.utils.clog.clogger import Logger


def dc_main(log: Logger) -> None:
    """Main module of the discord bot.

    Args:
        log -- instance of Logger.
    """

    bot_cred: DCBot = fetch_bc(log)
    intents = Intents.default()
    intents.message_content = True

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-3])
    PATH: str = f"{BASE_PATH}/src/data/shared/commands.json"

    try:
        ref: TextIO
        with open(PATH, "r", encoding="utf-8") as ref:
            commands: dict[str, str | list[str]] = load(ref)
    except (FileNotFoundError, PermissionError, IOError) as Err:
        log.logger(
            "E", f"{Err}. Cannot open reference file, aborting ..."
        )
        raise SystemExit

    client = BotClient(
            log,
            commands,
            bot_cred.ref_uid,
            intents=intents
        )
    client.run(bot_cred.token)

    return None
