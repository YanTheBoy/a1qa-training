from logger.logger import Logger
from BaseTest.Base_tests import Asserts
from selenium.webdriver.common.by import By
from CommonFunctions.json_data_getter import JsonDataGetter, AssertData

logger = Logger(logger="BaseTest").getlog()


class CarsComAsserts(Asserts):

    def assert_current_url(self):
        self.assert_current(JsonDataGetter.url)

    def assert_correct_page_opened(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        self.assert_text_on_page(locator)

    def assert_right_car_opened(self, make, model, year):
        car = f'{year} {make} {model}'
        locator = (By.XPATH, f"//*[contains(text(), '{car}')]")
        self.assert_text_on_page(locator)

    def assert_car_trims_opened(self, make, model, year):
        text = AssertData.trims
        text = f'{text} {year} {make} {model}'
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        self.assert_text_on_page(locator)

    def assert_car_params_saved(self, auto):
        self.assert_object_not_none(auto['engine'])
        self.assert_object_not_none(auto['trans'])

    def assert_cars_engine_and_trans(self, frst_auto, snd_auto, autos_details):
        self.assert_occurrence(frst_auto['engine'], autos_details['1_car']['engine'])
        self.assert_occurrence(snd_auto['engine'], autos_details['2_car']['engine'])
        self.assert_occurrence(frst_auto['trans'], autos_details['1_car']['trans'])
        self.assert_occurrence(snd_auto['trans'], autos_details['2_car']['trans'])
