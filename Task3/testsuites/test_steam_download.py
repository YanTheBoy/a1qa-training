import sys
sys.path.append('../')
from browser.browser_engine import BrowserEngine
from BaseElement.steam_store import SteamStorePage, SteamClientPage
from BaseElement.steam_store_asserts import SteamStoreAsserts
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
        homepage = SteamStorePage(self.driver)
        test = SteamStoreAsserts(self.driver)
        test.assert_current_url()
        homepage.click_install()

        client_page = SteamClientPage(self.driver)
        client_page.download()
        time.sleep(5)
        test.assert_steamclient_downloading()
