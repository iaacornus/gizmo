from glob import glob
from pathlib import Path
from os import mkdir
from os.path import isfile, dirname, exists
from typing import NoReturn

from src.utils.log.clogger import Logger


def index_dir(log: Logger, PATH: str = None) -> None | NoReturn:
    """Index the all the files inside a directory and output it
    on a file.

    Args:
        PATH -- path that will be indexed, defaults to none.
    """

    if PATH is None:
        BASE_PATH: str = dirname(__file__).split("/")[:-3]
        PATH: str = "/".join(BASE_PATH)
        log.logger("I", f"No path given, using {PATH} as path ...")

    HOME: Path = Path.home()
    INDEX_PATH: str = f"{HOME}/.sayu/"

    if not exists(INDEX_PATH):
        mkdir(INDEX_PATH)

    try:
        with open(
                f"{INDEX_PATH}/file_index", "w", encoding="UTF-8"
            ) as index:

            file: str
            for file in glob(f"{PATH}/**", recursive=True):
                if (
                        not isfile(file)
                        or file.startswith(f"{PATH}/venv")
                        or file.endswith("__init__.py")
                        or "__pycache__" in file
                    ):
                    continue
                index.write(f"{file}\n")
    except (FileNotFoundError, PermissionError) as Err:
        log.logger("e", f"{Err} encountered, aborting ... ")
        raise SystemExit

    return None
