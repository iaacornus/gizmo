from src.bot.dc_bot.dc_bot_main import dc_main
from src.utils.clog.clogger import Logger


def main() -> None:
    """Main module of AI."""

    log: Logger = Logger()
    dc_main(log)


if __name__ == "__main__":
    main()
