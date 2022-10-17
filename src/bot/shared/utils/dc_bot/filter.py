from subprocess import run, CalledProcessError

from src.utils.clog.clogger import Logger


def filter(
        log: Logger, msg: str, commands: dict[str, str | list[str]]
    ) -> tuple[bool, str] | None:
    """Determine the command based on message of the user.

    Args:
        log -- the instance of Logger
        msg -- message content of the user

    Returns:
        Whether the message is a correct command and its feedback.
    """

    def evlxec(log: Logger, cmd: str, command: str) -> str | None:
        """Evaluate and execute the command.

        Args:
            log -- instance of Logger
            cmd -- command by user
            command -- reference command

        Returns:
            The matched command, else None.
        """

        if cmd == f"!{command.lower()}":
            try:
                exec_cmd: list[str] = [command]
                exec_cmd.extend(msg.split()[1:])

                if run(exec_cmd).returncode != 0:
                    raise CalledProcessError

            except CalledProcessError as Err:
                log.logger(
                    "I", f"Command failed: {command}, {exec_cmd}; {Err}"
                )
            else:
                log.logger(
                    "I", f"Command executed: {command}, {exec_cmd}"
                )
                return f"Executed command: **{exec_cmd}**"

        return None

    if not msg.startswith("!"):
        return None

    cmd: str = msg.split()[0].lower()

    command: str | list[str]; microcommand: str
    for command in commands.values():
        if isinstance(command, list):
            for microcommand in command:
                if (
                        feedback := evlxec(log, cmd, microcommand)
                    ) is not None:
                    return True, feedback
        else:
            if (
                    feedback := evlxec(log, cmd, command)
                ) is not None:
                return True, feedback

    stderr: str = f"Command: **{cmd}** not found, skipping"
    log.logger("e", stderr)
    return False, stderr
