from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as CL
from utilities.locator_type import LocatorType


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
            raise TimeoutException(f"Element not clickable or not found: {locator}")

    def wait_for_visible(self, locator):
        self.log.info(f"Waiting for element to be visible: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Failed to find visible element: {locator} | Exception: {e}")
            raise TimeoutException(f"Element not visible or not found: {locator}")

    def wait_for_frame(self, index):
        try:
            return self.wait.until(EC.frame_to_be_available_and_switch_to_it(index))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Failed to switch to iframe({index}) | Exception: {e}")
            raise TimeoutException(f"Unable to switch to iframe with index {index}")

    @staticmethod
    def by_text(text: str):
        return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")'

    @staticmethod
    def by_id(resource_id: str):
        return AppiumBy.ID, resource_id

    @staticmethod
    def get_by_locator(by_type: str | Enum, value: str):
        by_type = by_type.value
        if by_type == 'id':
            return AppiumBy.ID, value
        elif by_type == 'text':
            return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{value}")'
        elif by_type == "xpath":
            return AppiumBy.XPATH, value
        elif by_type == "class_name":
            return AppiumBy.CLASS_NAME, value
        elif by_type == "accessibility_id":
            return AppiumBy.ACCESSIBILITY_ID, value
        elif by_type == "description":
            return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{value}")'
        elif by_type == "resource_id":
            return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{value}")'

        else:
            raise ValueError(f"Unsupported locator type: {by_type}")

    @staticmethod
    def validate_locator_key(locator_dictionary, name):
        """
        A unified method to check if the locator exists in the provided dictionary.
        If the locator exists, it returns the corresponding locator tuple.
        If not, raises an error.
        """
        if name not in locator_dictionary:
            BasePage.log.error(f"Locator key '{name}' is missing in the locator dictionary. Please check the dictionary")
            raise KeyError(f"Locator key '{name}' is missing in the locator dictionary. Please check the dictionary")
        return locator_dictionary[name]
