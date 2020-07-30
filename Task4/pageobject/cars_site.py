from selenium.webdriver.common.by import By
from BaseElement.base_element import BaseElement
from string import Template
import random


class CarsComMainPageLocators:
    research = (By.XPATH, '//*[@id="root"]//nav/ul//a[@data-linkname="header-research"]')


class CarsComMainPage(BaseElement):
    def click_research(self):
        self.click(CarsComMainPageLocators.research)


class CarsComResearchPageLocators:
    all_makes = (By.XPATH, '//*[@id="root"]//select[@name="makeId"]')
    all_models = (By.XPATH, '//*[@id="root"]//select[@name="modelId"]')
    years = (By.XPATH, '//*[@id="root"]//select[@name="year"]')
    search = (By.XPATH, '//*[@id="root"]//input[@value="Search"]')
    comparison = (By.XPATH, '//*[@id="root"]//a[@data-linkname="compare-cars"]')


class CarsComResearchPage(BaseElement):
    def select_make(self):
        all_makes = self.select_dropbox(CarsComResearchPageLocators.all_makes).options
        random_make = get_random_value(all_makes)
        self.select_by_text(CarsComResearchPageLocators.all_makes, random_make)
        return random_make

    def select_model(self):
        all_models = self.select_dropbox(CarsComResearchPageLocators.all_models).options
        random_model = get_random_value(all_models)
        self.select_by_text(CarsComResearchPageLocators.all_models, random_model)
        return random_model

    def select_year(self):
        all_years = self.select_dropbox(CarsComResearchPageLocators.years).options
        random_year = get_random_value(all_years)
        self.select_by_text(CarsComResearchPageLocators.years, random_year)
        return random_year

    def search_auto(self):
        self.click(CarsComResearchPageLocators.search)

    def compare_auto(self):
        self.click(CarsComResearchPageLocators.comparison)


class CarModelPageLocators:
    trims = (By.XPATH, '//*[@id="mmy-specs"]/table//a[@data-linkname="trim-compare"]')


class CarModelPage(BaseElement):
    def open_trims(self):
        self.click(CarModelPageLocators.trims)


class CarTrimsOptionsLocators:
    engine = (By.XPATH, '//*[@id="trim-table"]//div[contains(text(), "-hp")]')
    trans = (By.XPATH, '//*[@id="trim-table"]//div[contains(text(), "-speed")]')
    home = (By.XPATH, '/html/body/header/nav/a[@data-linkname="header-home"]')


class CarTrimsOptions(BaseElement):
    def get_engine_features(self):
        element = self.find_element(CarTrimsOptionsLocators.engine)
        return element.text

    def get_trans_features(self):
        element = self.find_element(CarTrimsOptionsLocators.trans)
        return element.text

    def go_to_homepage(self):
        self.click(CarTrimsOptionsLocators.home)


class SelectCarToComparePageLocators:
    make = (By.XPATH, '//*[@id="make-dropdown"]')
    model = (By.XPATH, '//*[@id="model-dropdown"]')
    year = (By.XPATH, '//*[@id="year-dropdown"]')
    compare_btn = (By.XPATH, '//*[@id="mainAddCarForm"]/button')
    done_btn = (By.XPATH, '//*[@id="researchCompareRoot"]//button[@data-linkname="add-car-select"]')


class SelectCarToComparePage(BaseElement):
    def select_auto(self, auto):
        self.select_make(auto)
        self.select_model(auto)
        self.select_year(auto)

    def select_make(self, auto):
        self.select_by_text(SelectCarToComparePageLocators.make, auto['make'])

    def select_model(self, auto):
        self.select_by_text(SelectCarToComparePageLocators.model, auto['model'])

    def select_year(self, auto):
        self.select_by_text(SelectCarToComparePageLocators.year, auto['year'])

    def compare_car(self):
        self.click(SelectCarToComparePageLocators.compare_btn)

    def add_new_car(self):
        self.click(SelectCarToComparePageLocators.done_btn)


class CarComparisonPageLocators:
    add_car = (By.XPATH, '//*[@id="add-from-your-favorite-cars-link"]/div')
    trans = Template('//*[@id="researchCompareRoot"]//'
                     'cars-compare-compare-info[@header="Transmission"]//'
                     'span[@index="$index"]')
    engine = Template('//*[@id="researchCompareRoot"]//'
                      'cars-compare-compare-info[@header="Engine"]//'
                      'span[@index="$index"]')


class CarComparisonPage(BaseElement):
    def add_another_car(self):
        self.click(CarComparisonPageLocators.add_car)

    def get_car_features(self, index):
        engine = self.get_car_engine(index)
        trans = self.get_car_trans(index)
        return cars_main_details(engine, trans)

    def get_car_trans(self, index):
        car_index = CarComparisonPageLocators.trans.substitute(index=index)
        locator = (By.XPATH, car_index)
        return self.find_element(locator).text

    def get_car_engine(self, index):
        car_index = CarComparisonPageLocators.engine.substitute(index=index)
        locator = (By.XPATH, car_index)
        return self.find_element(locator).text


def get_random_value(values):
    return (random.choice(values[1:])).text


def cars_main_details(eng, trans, make=None, model=None, year=None):
    return {
        'make': make,
        'model': model,
        'year': year,
        'engine': eng,
        'trans': trans
    }
