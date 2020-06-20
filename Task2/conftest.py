import pytest
from patterns.browser_factory import init_browser
from data_getter_module import JsonDataGetter

browser_name = JsonDataGetter.browser


@pytest.fixture(scope='session')
def browser():
    driver = init_browser(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()
