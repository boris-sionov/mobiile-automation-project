from enum import Enum
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as CL


class BasePage:
    """
    BasePage is a foundational class for page objects that provides:
    - Wait utilities for synchronization
    - Locator strategies
    - Logging for better test debugging
    """
    log = CL.custom_logger()

    def __init__(self, driver):
        """
        Initializes BasePage with WebDriver and WebDriverWait.

        :param driver: WebDriver instance (Appium or Selenium)
        """
        self.driver = driver
        self.locators = {}
        self.wait = WebDriverWait(
            self.driver,
            5,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException,
                TimeoutException
            ]
        )

    def wait_for_clickable(self, locator):
        """
        Waits until the element is clickable.

        :param locator: Tuple (By, locator)
        :return: WebElement
        :raises TimeoutException: if not clickable in time
        """
        self.log.info(f"Waiting for element to be clickable: {locator}")
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Element not clickable: {locator} | Exception: {e}")
            raise TimeoutException(f"Element not clickable or not found: {locator}")

    def wait_for_visible(self, locator):
        """
        Waits until the element is visible.

        :param locator: Tuple (By, locator)
        :return: WebElement
        :raises TimeoutException: if not visible in time
        """
        self.log.info(f"Waiting for element to be visible: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Element not visible: {locator} | Exception: {e}")
            raise TimeoutException(f"Element not visible or not found: {locator}")

    def wait_for_not_visible(self, locator):
        """
        Waits until the element becomes invisible.

        :param locator: Tuple (By, locator)
        :return: True if invisible, else False
        """
        self.log.info(f"Waiting for element to disappear: {locator}")
        try:
            return self.wait.until_not(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.log.warning(f"Element still visible: {locator} | Exception: {e}")
            return False

    def wait_for_frame(self, index):
        """
        Waits for an iframe and switches to it.

        :param index: Index of the iframe
        :return: True if successful
        :raises TimeoutException: if frame is not available
        """
        try:
            return self.wait.until(EC.frame_to_be_available_and_switch_to_it(index))
        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Unable to switch to iframe({index}) | Exception: {e}")
            raise TimeoutException(f"Unable to switch to iframe with index {index}")

    @staticmethod
    def get_by_locator(by_type: str | Enum, value: str):
        """
        Returns locator tuple based on strategy.

        :param by_type: Locator strategy (str or Enum)
        :param value: Locator value
        :return: Tuple (By, value)
        :raises ValueError: for unsupported strategies
        """

        if isinstance(by_type, Enum):
            by_type = by_type.value
            by_type = by_type.lower()

        # Normalize by_type
        by_type = by_type.lower()

        match by_type:
            case 'id':
                return AppiumBy.ID, value
            case 'text':
                return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{value}")'
            case 'xpath':
                return AppiumBy.XPATH, f'//android.widget.EditText[@resource-id="{value}"]'
            case 'class_name':
                return AppiumBy.CLASS_NAME, value
            case 'accessibility_id':
                return AppiumBy.ACCESSIBILITY_ID, value
            case 'description':
                return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{value}")'
            case 'resource_id':
                return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{value}")'
            case _:
                raise ValueError(f"Unsupported locator type: {by_type}")

    @staticmethod
    def validate_locator_key(locator_dictionary, name):
        """
        Validates if a key exists in the locator dictionary.

        :param locator_dictionary: Dictionary of locators
        :param name: Key to check
        :return: Locator tuple
        :raises KeyError: if key is missing
        """
        if name not in locator_dictionary:
            BasePage.log.error(f"Missing locator key '{name}' in dictionary.")
            raise KeyError(f"Locator key '{name}' is missing in the dictionary.")
        # name = name.lower()
        return locator_dictionary[name]

    @allure.step("Get locator from section '{section}' and key '{key}'")
    def get_page_locator(self, section, key):
        """
        Retrieves a locator from the locators' dictionary.

        :param section: Section in locator dictionary (e.g., 'buttons')
        :param key: Key in that section
        :return: Locator tuple
        :raises AttributeError, ValueError
        """
        if not hasattr(self, 'locators'):
            raise AttributeError("This page does not define 'self.locators'")

        if section not in self.locators:
            raise ValueError(f"Section '{section}' not found in locators")

        key = key.lower()
        if key not in self.locators[section]:

            raise ValueError(f"Key '{key}' not found in section '{section}'")
        return self.locators[section][key]
