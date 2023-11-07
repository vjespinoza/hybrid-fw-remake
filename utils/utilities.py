import json
from typing import Any, Tuple
from config.constants import BROWSER_RESOLUTIONS


def extract_json_data(file: str) -> Any:
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def browser_resolution(screen_size: str) -> Tuple[int, int, str]:
    data = extract_json_data(file=BROWSER_RESOLUTIONS)
    width = data[screen_size]['resolution'][0]
    height = data[screen_size]['resolution'][1]
    user_agent = data[screen_size]['user_agent']
    return width, height, user_agent
