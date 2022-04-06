import configparser
import os
from pathlib import Path

from .path_log_files import logs_path


def parse_log_files():

    path = Path(logs_path())
    for f in path.iterdir():
        print(f, f.name, f.suffix)

    print('парсим файлы')
