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
        self.log.info(f"Waiting for element to be clickable: {locator}")
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Failed to find clickable element: {locator} | Exception: {e}")
            assert False, f"Element not clickable or not found: {locator}"

    def wait_for_visible(self, locator):
        self.log.info(f"Waiting for element to be visible: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Failed to find visible element: {locator} | Exception: {e}")
            assert False, f"Element not visible or not found: {locator}"

    def wait_for_frame(self, index):
        try:
            return self.wait.until(EC.frame_to_be_available_and_switch_to_it(index))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Failed to switch to iframe({index}) | Exception: {e}")
            assert False, f"Unable to switch to iframe with index {index}"


