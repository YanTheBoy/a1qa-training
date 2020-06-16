from selenium import webdriver
from logger.logger import Logger
from CommonFunctions.json_data_getter import JsonDataGetter


logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        browser = JsonDataGetter.browser
        logger.info("You had select %s browser." % browser)
        url = JsonDataGetter.url
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('intl.accept_languages', JsonDataGetter.lang)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "application/octet-stream,text/csv")
            driver = webdriver.Firefox(firefox_profile=profile)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            options = webdriver.ChromeOptions()
            prefs = {
                'safebrowsing.enabled': 'false',
                'intl.accept_languages': JsonDataGetter.lang
            }
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=options)
            logger.info("Starting Chrome browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
