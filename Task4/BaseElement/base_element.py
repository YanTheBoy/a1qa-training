import sys
from BaseEntity.base_page import BasePage
from logger.logger import Logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


logger = Logger(logger="BasePage").getlog()


class BaseElement(BasePage):

    def move_to_element(self, selector):
        el = self.find_element(selector)
        try:
            builder = ActionChains(self.driver)
            builder.move_to_element(el).perform()
            logger.info("Moving cursor to element")
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            sys.exit('No such Element Exception')

    def select_dropbox(self, selector):
        logger.info("Trying to select dropbox.")
        return Select(self.find_element(selector))

    def select_value(self, *selector, value):
        logger.info(f"Trying to select '{value}'.")
        el = Select(self.find_element(*selector))
        el.select_by_value(value)

    def select_by_text(self, selector, text):
        logger.info(f"Selecting '{text}' element.")
        element = Select(self.find_element(selector))
        element.select_by_visible_text(text)

    def find_elements(self, selector, time=5):
        try:
            elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(selector),
                                                              message=f"Can't find elements by locator")
            logger.info("Looking up element...")
            return elements
        except NoSuchElementException:
            logger.error("NoSuchElementException")
            sys.exit('No such Element Exception')

    def find_element(self, selector, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(selector),
                                                             message=f"Can't find element by locator")
            logger.info("Looking up element...")
            return element
        except NoSuchElementException:
            logger.error("NoSuchElementException.")
            sys.exit('No such Element Exception')

    def find_clickable_element(self, selector, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(selector),
                                                             message=f"Can't find element by locator")
            logger.info("Looking up element...")
            return element
        except NoSuchElementException:
            logger.error("NoSuchElementException.")
            sys.exit('No such Element Exception')

    def click(self, selector):
        el = self.find_clickable_element(selector)
        try:
            el.click()
            logger.info("The element  was clicked.")
        except NameError:
            logger.error("Failed to click the element.")
            sys.exit('Click Error')
