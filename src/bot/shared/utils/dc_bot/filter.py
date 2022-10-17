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

    def _evlxec(
            msg: str,
            cmd: str,
            command: str
        ) -> str:
        """Evaluate and execute the command.

        Args:
            msg -- message of the user
            cmd -- command by user
            command -- reference command

        Returns:
            A boolean and a stdout or stderr
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

        return "Command not found."

    if not msg.startswith("!") or uid != ref_uid:
        return None

    cmd: str = msg.split()[0].lower()

    command: str | list[str]; mcommand: str; output: tuple[bool, str]
    for command in commands.values():
        if isinstance(command, list):
            for mcommand in command:
                return _evlxec(cmd, mcommand, uid, ref_uid)
        else:
            return _evlxec(cmd, mcommand, uid, ref_uid)
