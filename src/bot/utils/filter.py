from utils.clog.clogger import Logger


def filter(log: Logger, msg: str) -> list[str]:
    """Determine the command based on message of the user.

    Args:
        log -- the instance of Logger
        msg -- message content of the user

    Returns:
        The equivalent command and arguments.
    """
    ...
