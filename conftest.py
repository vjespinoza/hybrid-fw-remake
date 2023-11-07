import pytest


@pytest.fixture()
def web_driver():
    print("Web Driver")


@pytest.fixture()
def mobile_driver():
    print("Mobile Driver")
