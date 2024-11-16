import json
from os import path

from settings import TEST_DATA_DIRECTORY


def load_data(file_name: str):
    path_file = path.join(TEST_DATA_DIRECTORY, file_name)
    with open(path_file, "r", encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)
