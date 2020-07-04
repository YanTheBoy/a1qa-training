import time
from logger.logger import Logger


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

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
