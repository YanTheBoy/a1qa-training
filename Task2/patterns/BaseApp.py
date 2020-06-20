from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_getter_module import JsonDataGetter
from selenium.webdriver.common.action_chains import ActionChains

url = JsonDataGetter.url


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = url
        self.ActionChains = ActionChains

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_implicitly(self, time):
        return self.driver.implicitly_wait(time)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def change_window_to_page(self, page):
        if page == 'main':
            main_page = self.driver.window_handles[0]
            return self.driver.switch_to.window(main_page)
        elif page == 'authorization':
            auth_page = self.driver.window_handles[1]
            return self.driver.switch_to.window(auth_page)

    def make_action_click(self, element):
        return ActionChains(self.driver).move_to_element(element).click().perform()
