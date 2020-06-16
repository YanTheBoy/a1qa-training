from BaseEntity.base_page import BasePage
from selenium.webdriver.common.by import By
from logger.logger import Logger
from BaseTest.Base_tests import Tests


logger = Logger(logger="BaseTest").getlog()


class SteamStoreTests(Tests):
    header_name = (By.XPATH, '//*[@class="pageheader"]')
    top_sellers = (By.XPATH, '//*[@id="tab_select_TopSellers"]/div')

    def assert_current_url(self):
        self.assert_current('https://store.steampowered.com/')

    def assert_game_genre(self):
        genres = [
            'Browsing Action',
            'Browsing Indie',
            'Просмотр по метке «Инди»',
            'Просмотр по метке «Экшен»'
        ]
        self.assert_equal_game_genre(*self.header_name, genres=genres)

    def assert_top_sellers_opened(self):
        tab = 'TopSellers'
        self.assert_tab_opened(tab_name=tab)

    def assert_gamepage_opened(self):
        self.sleep(1.5)
        self.assert_current('https://store.steampowered.com/app/')

    def assert_game_prices(self, price_from_mainpage, price_from_gamepage):
        game_price = [price for price in price_from_mainpage if price in price_from_gamepage]
        self.assert_equal(game_price, price_from_mainpage)

    def assert_steamclient_downloading(self):
        self.assert_file_exist('SteamSetup.exe')

