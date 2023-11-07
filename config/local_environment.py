import os
from config.constants import (DEFAULT_COMPONENT, DEFAULT_EXECUTION, DEFAULT_BROWSER,
                              DEFAULT_SCREEN_SIZE, DEFAULT_PLATFORM)


def get_component():
    return os.environ.get("COMPONENT") or DEFAULT_COMPONENT


def get_execution():
    return os.environ.get("EXECUTION") or DEFAULT_EXECUTION


def get_browser():
    return os.environ.get("BROWSER") or DEFAULT_BROWSER


def get_screen_size():
    return os.environ.get("SCREEN_SIZE") or DEFAULT_SCREEN_SIZE


def get_platform():
    return os.environ.get("PLATFORM") or DEFAULT_PLATFORM


def get_sl_username():
    return os.environ.get("SL_USERNAME")


def get_sl_accesskeye():
    return os.environ.get("SL_ACCESSKEY")
