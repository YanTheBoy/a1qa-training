import sys
sys.path.append('../')
from browser.browser_engine import BrowserEngine
from BaseElement.steam_store import HomePage
from BaseElement.steam_store_tests import SteamStoreTests
import unittest
import time

class TestSteamStore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_steam_download(self):
        homepage = HomePage(self.driver)
        test = SteamStoreTests(self.driver)
        test.assert_current_url()
        homepage.click_install()
        homepage.download()
        test.assert_steamclient_downloading()
