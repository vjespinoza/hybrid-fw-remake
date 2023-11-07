from typing import Callable

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


_WEB_DRIVERS = {
    "chrome": lambda: webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    "firefox": lambda: webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())),
    "edge": lambda: webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
}


def get_web_driver(browser) -> WebDriver:
    local_driver: Callable[[], WebDriver] = _WEB_DRIVERS[browser]
    dvr = local_driver()
    return dvr
