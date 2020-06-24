import sys
sys.path.append('../')
from browser.browser_engine import BrowserEngine
from BaseElement.steam_store import HomePage
from BaseElement.steam_store_asserts import SteamStoreAsserts
from CommonFunctions.json_data_getter import TestingData
import unittest


class TestActionGameDiscount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_steam_games_with_highest_sale(self):
        homepage = HomePage(self.driver)
        test = SteamStoreAsserts(self.driver)
        test.assert_current_url()

        homepage.click_menu_genre(TestingData.action_en)
        test.assert_game_genre()

        homepage.click_top_sellers()
        test.assert_top_sellers_opened()

        games_prices = homepage.get_disc_prices()
        homepage.get_discount_game('max')

        if homepage.check_age_restriction():
            homepage.enter_correct_age()
            homepage.view_game_page()
        test.assert_gamepage_opened()

        actual_game_prices = homepage.get_prices()
        test.assert_game_prices(actual_game_prices, games_prices)


class TestIndieGameDiscount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_steam_games_with_lowest_sale(self):
        homepage = HomePage(self.driver)
        test = SteamStoreAsserts(self.driver)
        test.assert_current_url()

        homepage.click_menu_genre(TestingData.indie_en)
        test.assert_game_genre()

        homepage.click_top_sellers()
        test.assert_top_sellers_opened()

        games_prices = homepage.get_disc_prices()
        homepage.get_discount_game('min')

        if homepage.check_age_restriction():
            homepage.enter_correct_age()
            homepage.view_game_page()
        test.assert_gamepage_opened()

        actual_game_prices = homepage.get_prices()
        test.assert_game_prices(actual_game_prices, games_prices)


if __name__ == '__main__':
    unittest.main()
