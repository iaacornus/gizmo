from src.utils.clog.clogger import Logger


def filter(
        log: Logger, msg: str, commands: dict[str, str | list[str]]
    ) -> str | None:
    """Determine the command based on message of the user.

    Args:
        log -- the instance of Logger
        msg -- message content of the user

    Returns:
        The feedback to command.
    """

    def eval_cmd(log: Logger, cmd: str, command: str) -> str | None:
        """Evaluate the command.

        Args:
            log -- instance of Logger
            cmd -- command by user
            command -- reference command

        Returns:
            The matched command, else None.
        """

        if cmd == f"!{command.lower()}":
            log.logger("I", f"Command executed: {command}, {cmd}")
            exec_cmd: list[str] = [command]
            exec_cmd.extend(msg.split()[1:])
            return f"Executed command: **{exec_cmd}**"

    if not msg.startswith("!"):
        return

    cmd: str = msg.split()[0].lower()

    command: str; microcommand: str
    for command in commands.values():
        if isinstance(command, list):
            for microcommand in command:
                if (
                        feedback := eval_cmd(log, cmd, microcommand)
                    ) is not None:
                    return feedback
        else:
            if (
                    feedback := eval_cmd(log, cmd, command)
                ) is not None:
                return feedback

    stderr: str = f"Command: **{cmd}** not found, skipping"
    log.logger("e", stderr)
    return stderr
