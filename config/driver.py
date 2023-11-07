from typing import Callable, Tuple
from utils.utilities import browser_resolution

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


_WEB_DRIVERS = {
    "chrome": lambda screen_size: _chrome_driver(browser_resolution(screen_size)),
    "firefox": lambda screen_size: _firefox_driver(browser_resolution(screen_size)),
    "edge": lambda screen_size: _edge_driver(browser_resolution(screen_size))
}


def get_web_driver(browser: str, screen_size: str) -> WebDriver:
    web_driver: Callable[[str], WebDriver] = _WEB_DRIVERS[browser]
    driver = web_driver(screen_size)
    return driver


def _chrome_driver(resolution: Tuple) -> WebDriver:
    options = ChromeOptions()
    options.add_experimental_option("mobileEmulation", {
        "deviceMetrics": {
            "width": resolution[0],
            "height": resolution[1],
            "pixelRatio": 3.0,
        },
        "userAgent": resolution[2]
    })
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options)


def _edge_driver(resolution: Tuple) -> WebDriver:
    options = EdgeOptions()
    options.add_experimental_option("mobileEmulation", {
        "deviceMetrics": {
            "width": resolution[0],
            "height": resolution[1],
            "pixelRatio": 3.0,
        },
        "userAgent": resolution[2]
    })
    return webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()), options=options)


def _firefox_driver(resolution: Tuple) -> WebDriver:
    options = FirefoxOptions()
    options.set_preference("general.useragent.override", resolution[2])
    options.add_argument(f"--width={resolution[0]}")
    options.add_argument(f"--height={resolution[1]}")
    return webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options)
