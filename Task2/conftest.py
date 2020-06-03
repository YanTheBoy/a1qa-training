import pytest
from patterns.init_chrome_module import DriverChrome
from patterns.init_firefox_module import DriverFirefox
from data_getter_module import JsonDataGetter

browser_name = JsonDataGetter.browser


@pytest.fixture(scope='session')
def browser():
    if browser_name == 'Chrome' or browser_name == 'chrome':
        driver = DriverChrome()
        driver.fullscreen_window()
        yield driver
        driver.quit()
    elif browser_name == 'firefox' or browser_name == 'Firefox':
        driver = DriverFirefox()
        driver.fullscreen_window()
        yield driver
        driver.quit()






