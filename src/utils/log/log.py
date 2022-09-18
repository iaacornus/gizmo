from src.utils.log.logger import Logger


def log(log: Logger, exception_: str, message: str) -> None:
    """Function to avoid multiple instantiation of Logger.

    Args:
        log -- Logger instance.
        exception_ -- determines what type of log level to use
        message -- message to be logged.
    """

    log.logger(exception_, message)
