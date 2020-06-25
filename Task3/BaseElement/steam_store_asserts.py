from logger.logger import Logger
from BaseTest.Base_tests import Asserts
from CommonFunctions.json_data_getter import JsonDataGetter, TestingData
from BaseElement.steam_store import GameGenrePageLocators


logger = Logger(logger="BaseTest").getlog()


class SteamStoreAsserts(Asserts):

    def assert_current_url(self):
        self.assert_current(JsonDataGetter.url)

    def assert_game_genre(self):
        genres = TestingData.indie_heading + TestingData.action_heading
        header = GameGenrePageLocators.header_name
        self.assert_equal_game_genre(header, genres)

    def assert_top_sellers_opened(self):
        tab = 'TopSellers'
        self.assert_tab_opened(tab_name=tab)

    def assert_gamepage_opened(self):
        self.assert_current(TestingData.gamapege)

    def assert_game_prices(self, price_from_mainpage, price_from_gamepage):
        game_price = [price for price in price_from_mainpage if price in price_from_gamepage]
        self.assert_equal(game_price, price_from_mainpage)

    def assert_steamclient_downloading(self):
        self.assert_file_exist(TestingData.client)
