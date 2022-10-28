from os.path import dirname
from typing import TextIO


def remove_spec_char() -> None:
    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-2])
    PATH: str = f"{BASE_PATH}/assets/templates/README"

    try:
        temp: TextIO
        with open(
                f"{BASE_PATH}/proj_struct.temp",
                "r",
                encoding="UTF-8"
            ) as temp, open(
                PATH,
                "r",
                encoding="UTF-8"
            ) as template:
            lines: list[str] = temp.readlines()
            readme_temp: list[str] = template.readlines()

        readme: TextIO; line: str
        with open(
                f"{BASE_PATH}/README", "w", encoding="UTF-8"
            ) as readme:
            for line in readme_temp:
                readme.write(line)

            for line in lines:
                new_line: str = (
                        line
                            .replace("└──", "`--")
                            .replace("├──", "+--")
                            .replace("│  ", "|  ")
                    )
                readme.write(new_line)

    except FileNotFoundError:
        pass


if __name__ == "__main__":
    remove_spec_char()
