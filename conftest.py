import pytest
from config.driver import get_web_driver
from config.local_environment import get_browser, get_screen_size


@pytest.fixture()
def web_driver():
    print("Web Driver")
    driver = get_web_driver(get_browser(), get_screen_size())
    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
    yield driver
    driver.quit()


@pytest.fixture()
def mobile_driver():
    print("Mobile Driver")
