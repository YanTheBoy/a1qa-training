from .init_firefox_module import DriverFirefox
from .init_chrome_module import DriverChrome


def init_browser(browser_name):
    if browser_name.lower() == 'chrome':
        return start_chrome_browser()
    if browser_name.lower() == 'firefox':
        return start_firefox_browser()


def start_chrome_browser():
    return DriverChrome()


def start_firefox_browser():
    return DriverFirefox()
