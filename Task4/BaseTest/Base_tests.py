from BaseElement.base_element import BaseElement
from logger.logger import Logger

logger = Logger(logger="BaseTest").getlog()


class Asserts(BaseElement):

    def assert_current(self, link):
        logger.info(f"Checking '{link}' is current page.")
        assert link in self.current_url(), 'Incorrect url was opened.'
        logger.info("Right url opened test successfully complete.")

    def assert_text_on_page(self, locator):
        logger.info("Looking text on page..")
        assert self.find_element(locator), 'The element is not found.'
        logger.info("Text successfully found on page.")

    def assert_occurrence(self, first_object, second_object):
        logger.info("Comparing two objects")
        assert first_object in second_object, 'Values is not equal.'
        logger.info("Comparing values successfully.")

    def assert_object_not_none(self, entity):
        logger.info("Checking object for 'None'.")
        assert entity is not None, 'The object is None'
        logger.info("Object is not None")
