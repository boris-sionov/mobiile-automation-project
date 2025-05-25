import time

import allure
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException
)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
from base.general_actions import GeneralActions


class UIActions(BasePage):
    """
    Provides reusable UI interaction methods for web/mobile automation such as clicking,
    sending text, scrolling, long-pressing, and selecting dropdowns.
    """

    def __init__(self, driver):
        """
        Initializes UIActions with the provided WebDriver instance.

        :param driver: WebDriver instance used to interact with the browser or app
        """
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.actions = ActionChains(driver)

    def press_on_element(self, locator):
        """
        Clicks on an element after ensuring it is clickable.

        :param locator: Tuple (By, value) used to locate the element
        """
        try:
            element = self.wait_for_clickable(locator)
            element.click()
            with allure.step(f"Clicked element with locator: '{locator}'"):
                self.log.info(f"Clicked element with locator: '{locator}'")
        except Exception as e:
            with allure.step(f"Error while getting element: {locator}. Exception: {e}"):
                self.log.error(f"Error while getting element: {locator}. Exception: {e}")
            assert False

    def long_press(self, locator):
        """
        Performs a long press gesture on the element located by the given locator.

        :param locator: Tuple (By, value) for locating the element
        """
        duration = 500
        element = self.wait_for_clickable(locator)
        x = element.location['x']
        y = element.location['y']
        width = element.size['width']
        height = element.size['height']
        self.driver.execute_script("mobile: longClickGesture", {
            'x': x + width / 2,
            'y': y + height / 2,
            'duration': duration,
        })

        with allure.step(f"Locator {locator} pressed with long click press duration is: {duration}."):
            self.log.info(f"Locator {locator} pressed with long click press duration is: {duration}.")

    def scroll_screen(self, direction):
        """
        Performs a scroll gesture from bottom to top of the screen using Appium's mobile command.
        """
        try:
            self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,
                'top': 800,
                'width': 400,
                'height': 800,
                'direction': direction,
                'percent': 1.0
            })
            self.log.info("Performed scroll gesture")
        except Exception as e:
            with allure.step(f"Error performing scroll gesture. Exception: {e}"):
                self.log.error(f"Error performing scroll gesture. Exception: {e}")
                self.general_actions.screenshot("scroll_gesture_error")
            assert False

    def fill_in_text(self, locator, text):
        """
        Clears existing text and sends new text to an input field.

        :param locator: Tuple (By, value) for locating the element
        :param text: Text string to input
        """
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            element.send_keys(text)
            with allure.step(f"Send text element with locator: '{locator} ' and text send is: {text}"):
                self.log.info(f"Send text element with locator: '{locator}' and text send is: {text}")
        except Exception as e:
            with allure.step(f"Unable sent text on element: {locator}, Exception: {e}"):
                self.log.error(f"Unable sent text on element: {locator}, Exception: {e}")
                self.general_actions.screenshot(locator)
            assert False

    def clear_text(self, locator):
        """
        Clears text in the input field located by the given locator.

        :param locator: Tuple (By, value) for locating the element
        """
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            with allure.step(f"Locator '{locator}' text is cleared"):
                self.log.info(f"Locator '{locator}' text is cleared")
        except Exception as e:
            with allure.step(f"Unable sent clear text on element: {locator}, Exception: {e}"):
                self.log.error(f"Unable sent clear text on element: {locator}, Exception: {e}")
                self.general_actions.screenshot(locator)
            assert False

    def press_with_action_chain(self, locator):
        """
        Performs a click on an element using Selenium's ActionChains.

        :param locator: Tuple (By, value) to locate the element
        """
        element = self.wait_for_visible(locator)
        self.actions.move_to_element(element).click().perform()
        time.sleep(5)

    def fill_in_text_with_action_chain(self, text):
        """
        Clears and inputs text using keyboard key sequences with ActionChains.

        :param text: Text string to input
        """
        self.actions.key_down(Keys.COMMAND).send_keys("a").perform()
        self.actions.key_up(Keys.COMMAND)
        self.actions.send_keys(Keys.BACKSPACE).perform()
        self.actions.send_keys(text).perform()
        self.log.info(f"Sent {text} using action chain")

    def select_from_options(self, locator, value):
        """
        Selects an option from a dropdown menu by its value attribute.

        :param locator: Tuple (By, value) for locating the select element
        :param value: Value attribute of the option to select
        """
        element = self.wait_for_visible(locator)
        drop_down = Select(element)
        drop_down.select_by_value(value)
        self.log.info(f"Select from dropdown list {value} in locator : {locator}")

    def press(self, locator, try_scroll=True, max_attempts=6):
        """
        Attempts to press on an element. If not visible and try_scroll is enabled, will scroll alternately
        (down → up → down...) and retry.

        :param locator: Tuple (By, value) to locate the element
        :param try_scroll: Whether to attempt scrolling if element not found (default: True)
        :param max_attempts: Max number of attempts to find and interact with the element (default: 6)
        :raises Exception: If the element cannot be interacted with after all attempts
        """
        direction = 'down'

        for attempt in range(max_attempts):
            try:
                element = self.driver.find_element(*locator)

                if element.is_displayed():
                    with allure.step(f"Attempt {attempt + 1}: Element is visible. Performing click"):
                        long_clickable = element.get_attribute('long-clickable') == 'true'
                        if long_clickable:
                            self.long_press(locator)
                        else:
                            self.press_on_element(locator)
                    return
            except (NoSuchElementException, StaleElementReferenceException, WebDriverException):
                    self.log.warning(f"[Attempt {attempt + 1}] Element not found or not ready: {locator}")

            if try_scroll:
                self.log.info(f"[Attempt {attempt + 1}] Scrolling {direction} to locate {locator}")
                with allure.step(f"Attempt {attempt + 1}: Scrolling {direction}"):
                    self.scroll_screen(direction)
                direction = 'up' if direction == 'down' else 'down'

        raise Exception(f"Element {locator} not found or not clickable after {max_attempts} attempts.")

