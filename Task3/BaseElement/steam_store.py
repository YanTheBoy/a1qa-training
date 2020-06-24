from selenium.webdriver.common.by import By
from CommonFunctions.json_data_getter import KeyWordByLanguage, TestingData
from BaseEntity.base_element import BaseElement
from selenium.common.exceptions import TimeoutException

keywords = KeyWordByLanguage.keywords


class HomePage(BaseElement):
    install_button = (By.XPATH, '//*[@id="global_action_menu"]/div[1]/a')
    download_button = (By.XPATH, '//*[@id="about_greeting"]/div[4]/div[1]/a')
    menu = (By.XPATH, '//*[@id="genre_tab"]/span/a[1]')
    actions = (By.XPATH, '//*[@id="genre_flyout"]//*[normalize-space() = "{}"]'.format(keywords['action']))
    indie = (By.XPATH, '//*[@id="genre_flyout"]//*[normalize-space() = "{}"]'.format(keywords['indie']))
    top_sellers = (By.XPATH, '//*[@id="tab_select_TopSellers"]/div')
    games = (By.XPATH, '//*[@id="TopSellersRows"]/a//div[@class="discount_pct"]')
    year_field = (By.XPATH, '//*[@id="ageYear"]')
    age_wizard = (By.XPATH, '//*[@id="agegate_wizard"]')
    view_page = (By.XPATH, '//*[@id="app_agegate"]//a[@onclick="ViewProductPage()"]')
    discount_prices = (By.XPATH, '//*[@id="TopSellersTable"]//div[@class="discount_pct"]/following-sibling::div/div')
    purchase_prices = (By.XPATH, '//*[@class="game_area_purchase_game_wrapper"]//div[@class="discount_prices"]/div')
    header_name = (By.XPATH, '//*[@class="pageheader"]')

    def check_age_restriction(self):
        try:
            el = self.find_element(self.age_wizard).is_displayed()
            return el
        except TimeoutException:
            return False

    def click_install(self):
        self.click(self.install_button)

    def download(self):
        self.click(self.download_button)

    def click_menu_genre(self, genre):
        self.move_to_element(self.menu)
        if genre in [TestingData.indie_en, TestingData.indie_ru]:
            self.click(self.indie)
        elif genre in [TestingData.action_en, TestingData.action_ru]:
            self.click(self.actions)

    def click_top_sellers(self):
        self.click(self.top_sellers)

    def get_discount_game(self, value):
        games_with_sale = self.find_elements(self.games)
        game = find_max_or_min_discount(games_with_sale, value)
        self.click_webelement(game)

    def enter_correct_age(self):
        self.select_value(self.year_field, value=TestingData.year)

    def view_game_page(self):
        self.click(self.view_page)

    def get_prices(self):
        prices = self.find_elements(self.purchase_prices)
        return [price.text for price in prices]

    def get_disc_prices(self):
        discount_game_price = self.find_elements(self.discount_prices)
        return [price.text for price in discount_game_price]


def find_max_or_min_discount(games, value):
    discounted_games = {game: game.text for game in games}
    if value.lower() == 'max':
        return max(discounted_games.keys(), key=(lambda key: discounted_games[key]))
    elif value.lower() == 'min':
        return min(discounted_games.keys(), key=(lambda key: discounted_games[key]))
