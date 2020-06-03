from patterns.BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_SITE_NAME = (By.NAME, "application-name")
    LOCATOR_YANDEX_ENTER_BUTTON = (By.XPATH, '//div[@data-apiary-widget-name="@MarketNode/HeaderNav"]//a')
    LOCATOR_YANDEX_LOGIN_BUTTON = (By.XPATH, '//div[@class="passp-button passp-sign-in-button"]//button')
    LOCATOR_YANDEX_LOGIN_FIELD = (By.ID, 'passp-field-login')
    LOCATOR_YANDEX_PASS_FIELD = (By.ID, 'passp-field-passwd')
    LOCATOR_YANDEX_H1 = (By.TAG_NAME, 'h1')
    LOCATOR_YANDEX_MAIN_PAGE = (By.ID, 'logoPartMarket')
    LOCATOR_YANDEX_OPEN_CATS = (By.XPATH, '//div[@data-zone-name="all-categories"]')
    LOCATOR_YANDEX_TOP_CATEGORIES = (By.XPATH, '//div[@data-zone-name="all-categories"]/'
                                               'following-sibling::div//span')
    LOCATOR_YANDEX_POPUP_SEARCH = (By.CLASS_NAME, 'popup2__content')
    LOCATOR_YANDEX_FIND_CATS = (By.CSS_SELECTOR, 'button > a > span')
    LOCATOR_YANDEX_EXIT_BUTTON = (By.XPATH, '//a/span/span[text()="Выйти"]')


class SearchHelper(BasePage):
    def wait(self, time):
        return self.wait_implicitly(time)

    def change_window(self, page):
        return self.change_window_to_page(page)

    def check_site_open(self):
        tag = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SITE_NAME)
        return tag.get_attribute('content')

    def click_enter_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ENTER_BUTTON).click()

    def click_enter(self):
        element = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ENTER_BUTTON)
        return self.make_action_click(element)

    def click_exit(self):
        element = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_EXIT_BUTTON)
        return self.make_action_click(element)

    def click_login_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_LOGIN_BUTTON).click()

    def find_enter_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ENTER_BUTTON).is_displayed()

    def enter_login(self, login):
        login_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_LOGIN_FIELD)
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        pass_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PASS_FIELD)
        pass_field.send_keys(password)
        return pass_field

    def check_user_login(self):
        return len(self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_ENTER_BUTTON))

    def get_top_categories(self):
        categories = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_TOP_CATEGORIES)
        visible_categories = [category.text for category in categories if category.text != '']
        return visible_categories

    def go_to_selected_category(self, category):
        locator = (By.XPATH, f'//span[text()="{category}"]')
        return self.find_element(locator).click()

    def get_h1_text(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_H1).text

    def go_to_main_page(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_MAIN_PAGE).click()

    def open_categories_tray(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_OPEN_CATS).click()

    def hide_popup_search_field(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_POPUP_SEARCH).click()

    def get_all_categories(self):
        return self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_FIND_CATS)

    def click_on_user_icon(self, login):
        login = login.split('@')[0]
        locator = (By.XPATH, f'//div[text()="{login}"]/../following-sibling::button')
        return self.find_element(locator).click()

    def click_exit_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_EXIT_BUTTON).click()
