import os


def get_no_var():
    return os.environ.get("NO_VAR") or "DEFAULT_VALUE_1"


def get_var_one():
    return os.environ.get("VAR_ONE") or "DEFULT_VALUE_2"
