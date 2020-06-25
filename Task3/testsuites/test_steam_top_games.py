import sys
sys.path.append('../')
from browser.browser_engine import BrowserEngine
from BaseElement.steam_store import SteamStorePage, GameGenrePage, AgeRestrictionPage, GamePage
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
        test = SteamStoreAsserts(self.driver)
        test.assert_current_url()

        store_page = SteamStorePage(self.driver)
        store_page.click_menu_genre(TestingData.action_en)
        test.assert_game_genre()

        genre_page = GameGenrePage(self.driver)
        genre_page.click_top_sellers()
        test.assert_top_sellers_opened()

        games_prices = genre_page.get_disc_prices()
        genre_page.get_discount_game('max')

        checkage_page = AgeRestrictionPage(self.driver)
        if checkage_page.check_age_restriction():
            checkage_page.enter_correct_age()
            checkage_page.view_game_page()
        test.assert_gamepage_opened()

        game_page = GamePage(self.driver)
        actual_game_prices = game_page.get_prices()
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
        test = SteamStoreAsserts(self.driver)
        test.assert_current_url()

        store_page = SteamStorePage(self.driver)
        store_page.click_menu_genre(TestingData.indie_en)
        test.assert_game_genre()

        genre_page = GameGenrePage(self.driver)
        genre_page.click_top_sellers()
        test.assert_top_sellers_opened()

        games_prices = genre_page.get_disc_prices()
        genre_page.get_discount_game('min')

        checkage_page = AgeRestrictionPage(self.driver)
        if checkage_page.check_age_restriction():
            checkage_page.enter_correct_age()
            checkage_page.view_game_page()
        test.assert_gamepage_opened()

        game_page = GamePage(self.driver)
        actual_game_prices = game_page.get_prices()
        test.assert_game_prices(actual_game_prices, games_prices)


if __name__ == '__main__':
    unittest.main()
