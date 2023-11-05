import os

VAR_ONE = os.environ.get("VAR_ONE")
VAR_TWO = os.environ.get("VAR_TWO")


def test_env_vars():
    print(VAR_ONE)
    print(VAR_TWO)
