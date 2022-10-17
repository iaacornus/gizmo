from subprocess import run, CalledProcessError

from src.utils.clog.clogger import Logger


class Filter:
    def __init__(self, log: Logger) -> None:
        self.log: Logger = log

    def _evlxec(
            self,
            msg: str,
            cmd: str,
            command: str,
            uid: str,
            ref_uid: int
        ) -> tuple[int, str]:
        """Evaluate and execute the command.

        Args:
            msg -- message of the user
            cmd -- command by user
            command -- reference command
            uid -- user id
            ref_uid -- reference user id

        Returns:
            A particular return code for each cases:
                0 - the user does not have enough permission.
                1 - the command found and executed.
                2 - the command not found and not executed.
        """

        if uid != ref_uid:
            return (
                0, "UID not recognized, not executing command."
            )

        if cmd == f"!{command.lower()}":
            try:
                exec_cmd: list[str] = [command]
                exec_cmd.extend(msg.split()[1:])

                if run(exec_cmd).returncode != 0:
                    raise CalledProcessError

            except CalledProcessError as Err:
                self.log.logger(
                    "I", f"Command failed: {command}, {exec_cmd}; {Err}"
                )
            else:
                self.log.logger(
                    "I", f"Command executed: {command}, {exec_cmd}"
                )
                return (1, f"Executed command: **{exec_cmd}**")

        return (2, "Command not found.")

    def _eval_retcode(
            self,
            ret_code: int,
            feedback: str,
            cmd: list[str]
        ) -> tuple[bool, str]:
        """Evaluate the return code and return the given tuple.

        Args:
            ret_code -- the return code
            feedback -- the feedback of evlxec
            cmd -- the given command

        Returns:
            The tuple of a boolean value and a stdout or stderr.
        """

        match ret_code:
            case 1:
                self.log("I", feedback[1])
                return True, feedback[1]
            case 2:
                self.log("e", feedback[1])
                return False, feedback[1]
            case 3:
                stderr: str = f"Command: **{cmd}** not found, skipping"
                self.log("e", stderr)
                return False, stderr

    def filter(
            self,
            msg: str,
            commands: dict[str, str | list[str]],
            uid: int,
            ref_uid: int
        ) -> tuple[bool, str] | None:
        """Determine the command based on message of the user.

        Args:
            log -- the instance of Logger
            msg -- message content of the user
            uid -- user id

            ref_uid -- reference user id
        Returns:
            Whether the message is a correct command and its feedback.
        """

        if not msg.startswith("!"):
            return None

        cmd: str = msg.split()[0].lower()

        command: str | list[str]; mcommand: str; output: tuple[bool, str]
        for command in commands.values():
            if isinstance(command, list):
                for mcommand in command:
                    return self._eval_retcode(
                        self._evlxec(
                            cmd, mcommand, uid, ref_uid
                        )
                    )
            else:
                return self._eval_retcode(
                    self._evlxec(
                        cmd, mcommand, uid, ref_uid
                    )
                )
