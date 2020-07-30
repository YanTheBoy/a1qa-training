import sys
sys.path.append('../')
import unittest
from pageobject.cars_site import *
from browser.browser_engine import BrowserEngine
from pageobject.cars_site_asserts import CarsComAsserts
from CommonFunctions.json_data_getter import AssertData


class TestCarsComparison(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_two_cars_comparison(self):
        site_asserts = CarsComAsserts(self.driver)
        site_asserts.assert_current_url()
        main_page = CarsComMainPage(self.driver)
        main_page.click_research()
        site_asserts.assert_correct_page_opened(AssertData.research)

        def get_car_features():
            research = CarsComResearchPage(self.driver)
            auto_make = research.select_make()
            auto_model = research.select_model()
            auto_year = research.select_year()
            research.search_auto()
            site_asserts.assert_right_car_opened(auto_make, auto_model, auto_year)

            car_page = CarModelPage(self.driver)
            car_page.open_trims()
            site_asserts.assert_car_trims_opened(auto_make, auto_model, auto_year)

            trims_page = CarTrimsOptions(self.driver)
            auto_details = cars_main_details(
                trims_page.get_engine_features(),
                trims_page.get_trans_features(),
                auto_make,
                auto_model,
                auto_year,
            )
            trims_page.go_to_homepage()
            site_asserts.assert_current_url()
            return auto_details

        first_car_to_compare = get_car_features()
        site_asserts.assert_car_params_saved(first_car_to_compare)
        print(first_car_to_compare)

        main_page.click_research()
        site_asserts.assert_correct_page_opened(AssertData.research)
        second_car_to_compare = get_car_features()
        site_asserts.assert_car_params_saved(second_car_to_compare)
        print(second_car_to_compare)

        main_page.click_research()
        site_asserts.assert_correct_page_opened(AssertData.research)
        research_page = CarsComResearchPage(self.driver)
        research_page.compare_auto()
        site_asserts.assert_correct_page_opened(AssertData.comparison)

        car_to_compare_page = SelectCarToComparePage(self.driver)
        car_to_compare_page.select_auto(first_car_to_compare)
        car_to_compare_page.compare_car()
        site_asserts.assert_right_car_opened(
            first_car_to_compare['make'],
            first_car_to_compare['model'],
            first_car_to_compare['year']
        )

        comparison_page = CarComparisonPage(self.driver)
        comparison_page.add_another_car()
        car_to_compare_page.select_auto(second_car_to_compare)
        car_to_compare_page.add_new_car()
        site_asserts.assert_right_car_opened(
            second_car_to_compare['make'],
            second_car_to_compare['model'],
            second_car_to_compare['year']
        )

        cars = {}
        for car in range(len((first_car_to_compare, second_car_to_compare))):
            cars[f'{car+1}_car'] = comparison_page.get_car_features(car)
        site_asserts.assert_cars_engine_and_trans(first_car_to_compare, second_car_to_compare, cars)


if __name__ == '__main__':
    unittest.main()
