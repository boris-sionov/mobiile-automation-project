import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
from base.general_actions import GeneralActions


class UIActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.actions = ActionChains(driver)
        self.otp_code = None

    """ UI actions, like tap or swipe etc..."""

    # Press on button or element
    def press(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            element.click()
            with allure.step(f"Clicked element with locator: '{locator}'"):
                self.log.info(f"Clicked element with locator: '{locator}'")
        except Exception as e:
            with allure.step(f"Error while getting element: {locator}. Exception: {e}"):
                self.log.error(f"Error while getting element: {locator}. Exception: {e}")
            # self.general_actions.screenshot(locator)
            assert False

    def long_press(self, locator):
        # Get element button coordination
        duration = 500
        element = self.wait_for_clickable(locator)
        x = element.location['x']
        y = element.location['y']
        width = element.size['width']
        height = element.size['height']
        self.driver.execute_script("mobile: longClickGesture", {
            'x': x + width / 2,  # Center X coordinate
            'y': y + height / 2,  # Center Y coordinate
            'duration': duration,  # Click duration in milliseconds.

        })

        with allure.step(f"Locator {locator} pressed with long click press duration is: {duration}."):
            self.log.info(f"Locator {locator} pressed with long click press duration is: {duration}.")

    # Perform a scroll gesture on the screen.
    def scroll_screen(self):

        try:
            # Execute the scroll gesture via Appium's mobile command
            self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,  # Start position (50% of screen width)
                'top': 800,  # Start position (80% of screen height)
                'width': 400,  # Width of the screen (50%)
                'height': 800,  # Height to scroll (20%)
                'direction': 'up',  # Direction of the scroll (up or down)
                'percent': 0.8  # Distance to scroll (80% of the defined height)
            })
            self.log.info("Performed scroll gesture")
        except Exception as e:
            with allure.step(f"Error performing scroll gesture. Exception: {e}"):
                self.log.error(f"Error performing scroll gesture. Exception: {e}")
                self.general_actions.screenshot("scroll_gesture_error")
            assert False

    # Method to send text to an element
    def fill_in_text(self, locator, text):
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
        element = self.wait_for_visible(locator)
        self.actions.move_to_element(element).click().perform()
        time.sleep(5)

    def fill_in_text_with_action_chain(self, text):
        # clear text using action chain
        self.actions.key_down(Keys.COMMAND).send_keys("a").perform()  # Press and hold command + Press on a
        self.actions.key_up(Keys.COMMAND)  # release  command button
        self.actions.send_keys(Keys.BACKSPACE).perform()  # click on backspace
        self.actions.send_keys(text).perform()
        self.log.info(f"Sent {text} using action chain")

    def select_from_options(self, locator, value):
        element = self.wait_for_visible(locator)
        drop_down = Select(element)
        drop_down.select_by_value(value)
        self.log.info(f"Select from dropdown list {value} in locator : {locator}")

    def press_auto(self, locator, try_scroll=True, max_attempts=5):
        attempts = 0

        while attempts < max_attempts:
            try:
                element = self.driver.find_element(*locator)
                long_clickable = element.get_attribute('long-clickable') == 'true'

                if element.is_displayed():
                    if long_clickable:
                        self.long_press(locator)
                    else:
                        element.click()
                        with allure.step(f"Clicked element with locator: {locator}"):
                            self.log.info(f"Clicked element with locator: {locator}")
                    return

            except Exception:
                pass

            if try_scroll:
                with allure.step(f"Attempt {attempts + 1}: Scrolling to find {locator}"):
                    self.log.warning(f"Element {locator} not visible. Attempt {attempts + 1}. Scrolling...")
                self.driver.execute_script("mobile: scrollGesture", {
                    'left': 100,
                    'top': 800,
                    'width': 400,
                    'height': 800,
                    'direction': 'down',
                    'percent': 1.0
                })

            attempts += 1

        raise Exception(f"Element {locator} not found or not clickable after {max_attempts} attempts.")
