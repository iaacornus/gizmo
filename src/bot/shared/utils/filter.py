from subprocess import run, CalledProcessError

from src.utils.clog.clogger import Logger


def filter(
        log: Logger,
        msg: str,
        commands: dict[str, str | list[str]],
        uid: int,
        ref_uid: int
    ) -> str | None:
    """Determine the command based on message of the user.

    Args:
        log -- the instance of Logger
        msg -- message content of the user
        commands -- the reference for commands
        uid -- user id
        ref_uid -- reference user id

    Returns:
        Whether the message is a correct command and its feedback.
    """

    def evlxec(
            cmd: str,
            command: str
        ) -> tuple[bool, list[str]]:
        """Evaluate and execute the command.

        Args:
            cmd -- command by user
            command -- reference command

        Returns:
            A boolean and a stdout or stderr
        """

        try:
            exec_cmd: list[str] = [command]
            exec_cmd.extend(msg.split()[1:])

            if cmd == f"!{command.lower()}":
                if run(exec_cmd).returncode != 0:
                    raise CalledProcessError(1, exec_cmd)
            else:
                raise CalledProcessError(1, exec_cmd)
        except CalledProcessError as Err:
            log.logger(
                "I", f"Command failed: {command}, {exec_cmd}; {Err}"
            )
        else:
            log.logger(
                "I", f"Command executed: {command}, {exec_cmd}"
            )
            return True, exec_cmd

        return False, exec_cmd

    if (not msg.startswith("!")) or (uid != ref_uid):
        return None

    cmd: str = msg.split()[0].lower()

    command: str | list[str]
    mcommand: str
    fback: tuple[bool, list[str]]

    for command in commands.values():
        if isinstance(command, list):
            for mcommand in command:
                if (fback := evlxec(cmd, mcommand))[0]:
                    return f"Executed command: **{fback[1]}**"
        else:
            if (fback := evlxec(cmd, command))[0]:
                return f"Executed command: **{fback[1]}**"

    log.logger("e", "Command not found.")
    return "Command not found."
