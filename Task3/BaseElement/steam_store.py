from selenium.webdriver.common.by import By
from CommonFunctions.json_data_getter import KeyWordByLanguage, TestingData
from BaseEntity.base_element import BaseElement
from selenium.common.exceptions import TimeoutException

keywords = KeyWordByLanguage.keywords


class SteamStorePageLocators:
    install_button = (By.XPATH, '//*[@id="global_action_menu"]//a[@class="header_installsteam_btn_content"]')
    menu = (By.XPATH, '//*[@id="genre_tab"]/span')
    actions = (By.XPATH, '//*[@id="genre_flyout"]//*[normalize-space() = "{}"]'.format(keywords['action']))
    indie = (By.XPATH, '//*[@id="genre_flyout"]//*[normalize-space() = "{}"]'.format(keywords['indie']))


class SteamStorePage(BaseElement):
    def click_install(self):
        self.click(SteamStorePageLocators.install_button)

    def click_menu_genre(self, genre):
        self.move_to_element(SteamStorePageLocators.menu)
        if genre in [TestingData.indie_en, TestingData.indie_ru]:
            self.click(SteamStorePageLocators.indie)
        elif genre in [TestingData.action_en, TestingData.action_ru]:
            self.click(SteamStorePageLocators.actions)


class GameGenrePageLocators:
    top_sellers = (By.XPATH, '//*[@id="tab_select_TopSellers"]/div')
    discount_prices = (By.XPATH, '//*[@id="TopSellersTable"]//div[@class="discount_pct"]/following-sibling::div/div')
    games = (By.XPATH, '//*[@id="TopSellersRows"]/a//div[@class="discount_pct"]')
    header_name = (By.XPATH, '//*[@class="pageheader"]')


class GameGenrePage(BaseElement):
    def click_top_sellers(self):
        self.click(GameGenrePageLocators.top_sellers)

    def get_disc_prices(self):
        discount_game_price = self.find_elements(GameGenrePageLocators.discount_prices)
        return [price.text for price in discount_game_price]

    def get_discount_game(self, value):
        games_with_sale = self.find_elements(GameGenrePageLocators.games)
        game = find_max_or_min_discount(games_with_sale, value)
        self.click_webelement(game)


class AgeRestrictionPageLocators:
    age_wizard = (By.XPATH, '//*[@id="agegate_wizard"]')
    year_field = (By.XPATH, '//*[@id="ageYear"]')
    view_page = (By.XPATH, '//*[@id="app_agegate"]//a[@onclick="ViewProductPage()"]')


class AgeRestrictionPage(BaseElement):
    def check_age_restriction(self):
        try:
            el = self.find_element(AgeRestrictionPageLocators.age_wizard).is_displayed()
            return el
        except TimeoutException:
            return False

    def enter_correct_age(self):
        self.select_value(AgeRestrictionPageLocators.year_field, value=TestingData.year)

    def view_game_page(self):
        self.click(AgeRestrictionPageLocators.view_page)


class GamePageLocators:
    purchase_prices = (By.XPATH, '//*[@class="game_area_purchase_game_wrapper"]//div[@class="discount_prices"]/div')


class GamePage(BaseElement):
    def get_prices(self):
        prices = self.find_elements(GamePageLocators.purchase_prices)
        return [price.text for price in prices]


class SteamClientPageLocators:
    download_button = (By.XPATH, '//*[@id="about_greeting"]//a[@class="about_install_steam_link"]')


class SteamClientPage(BaseElement):
    def download(self):
        self.click(SteamClientPageLocators.download_button)


def find_max_or_min_discount(games, value):
    discounted_games = {game: game.text for game in games}
    if value.lower() == 'max':
        return max(discounted_games.keys(), key=(lambda key: discounted_games[key]))
    elif value.lower() == 'min':
        return min(discounted_games.keys(), key=(lambda key: discounted_games[key]))
