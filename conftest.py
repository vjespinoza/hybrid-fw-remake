import pytest
from config.driver import get_web_driver
from config.local_environment import get_browser


@pytest.fixture()
def web_driver():
    driver = get_web_driver(get_browser())
    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
    print("Web Driver")


@pytest.fixture()
def mobile_driver():
    print("Mobile Driver")
