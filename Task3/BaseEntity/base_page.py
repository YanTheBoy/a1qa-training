import sys
import time
from logger.logger import Logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


logger = Logger(logger="BasePage").getlog()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def current_url(self):
        url = self.driver.current_url
        logger.info("Getting current url")
        return url

    def move_to_element(self, *selector):
        el = self.find_element(*selector)
        try:
            builder = ActionChains(self.driver)
            builder.move_to_element(el).perform()
            logger.info("Moving cursor to element")
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            sys.exit('No such Element Exception')

    def select_value(self, *selector, value):
        el = Select(self.find_element(*selector))
        el.select_by_value(value)

    def find_element(self, *selector):
        try:
            element = self.driver.find_element(*selector)
            logger.info("Looking up element...")
            return element
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            sys.exit('No such Element Exception')

    def find_elements(self, *selector):
        try:
            elements = self.driver.find_elements(*selector)
            logger.info("Looking up element...")
            return elements
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            sys.exit('No such Element Exception')

    def click(self, *selector):
        el = self.find_element(*selector)
        try:
            el.click()
            logger.info("The element  was clicked.")
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
            sys.exit('Click Error')

    @staticmethod
    def click_webelement(webelement):
        webelement.click()
        logger.error("Clicked on webelement")

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
