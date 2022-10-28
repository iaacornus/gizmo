from os.path import dirname
from typing import TextIO


def remove_spec_char() -> None:
    BASE_PATH: str = "/".join(dirname(__file__))[:-2]
    PATH: str = f"{BASE_PATH}/assets/templates/README"

    try:
        temp: TextIO
        with open("proj_struct.temp", "r", encoding="UTF-8") as temp:
            lines: list[str] = temp.readlines()

        readme: TextIO; line: str
        with open(PATH, "a", encoding="UTF-8") as readme:
            for line in lines:
                new_line: str = (
                        line
                            .replace("└──", "`--")
                            .replace("├──", "+--")
                            .replace("│  ", "|  ")
                    )
                readme.write(f"{new_line}\n")

    except FileNotFoundError:
        pass
