from BaseEntity.base_element import BaseElement
from logger.logger import Logger
import os
import getpass

logger = Logger(logger="BaseTest").getlog()


class Asserts(BaseElement):

    def assert_current(self, link):
        assert link in self.current_url(), 'Incorrect url was opened.'
        logger.info("Right url opened test successfully complete.")

    def assert_equal_game_genre(self, selector, genres):
        x = self.find_element(selector).text
        assert x in genres, 'Incorrect game genre was opened.'
        logger.info("Right game genre opened test successfully complete.")

    def assert_tab_opened(self, tab_name):
        assert tab_name in self.current_url(), 'Incorrect tab was opened'
        logger.info("Right page tab opened succesfully.")

    def assert_equal(self, first_value, second_value):
        assert all(elem in second_value for elem in first_value), 'Values is not equal.'
        logger.info("Comparing values successfully.")

    def assert_file_exist(self, filename):
        user = getpass.getuser()
        filepath = os.path.join("C:\\Users", user, "Downloads", filename)
        assert os.path.isfile(filepath), 'File was not downloaded.'
        logger.info("File was downloaded successfully.")
