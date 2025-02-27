from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as CL
import time


class BasePage:
    log = CL.custom_logger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                                  ignored_exceptions=[ElementNotVisibleException,
                                                      ElementNotSelectableException,
                                                      NoSuchElementException, TimeoutException])

    # Method to wait for an element to be clickable
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Method to wait for an element to be visible
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

