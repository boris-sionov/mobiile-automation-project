import allure
from selenium.common import NoSuchElementException
from base.base_page import BasePage
from base.general_actions import GeneralActions


class UIActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)

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

    def press_with_scroll(self, locator, max_attempts=5):
        attempts = 0
        while attempts < max_attempts:

            try:
                element = self.driver.find_element(*locator)
                boolean_value = element.get_attribute('long-clickable') == 'true'
                if element.is_displayed():
                    with allure.step(f"Element {locator} found on attempt without scrolling. Clicking on it."):
                        self.log.info(f"Element {locator} found on attempt without scrolling. Clicking on it.")
                    # self.log.debug(f"Element long click is: {boolean_value}")
                    if boolean_value:
                        self.long_press(locator)
                        return  # Exit function after clicking the element
                    else:
                        element.click()
                        with allure.step(f"Clicked element with locator: {locator}"):
                            self.log.info(f"Clicked element with locator: {locator}")
                        return  # Exit function after clicking the element

            except NoSuchElementException:
                with allure.step(f"Element {locator} not found on attempt {attempts + 1}. Trying to scroll."):
                    self.log.warning(f"Element {locator} not found on attempt {attempts + 1}. Trying to scroll.")

            # Perform scrolling if element is not found
            self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,
                'top': 800,
                'width': 400,
                'height': 800,
                'direction': 'down',
                'percent': 1.0
            })

            attempts += 1

        # If element is not found after max_attempts, raise an exception
        raise Exception(f"Element {locator} not found after {max_attempts} attempts.")

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
            # 'element': locator,  # Reference element ID instead of the element itself
            'duration': duration,  # Click duration in milliseconds.
            # 'radius': 20,  # Optional: Set the radius of the touch area
            # 'fingerCount': 1,  # Optional: Number of fingers for the gesture
            # 'speed': 1.0  # Optional: Gesture speed
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
            with allure.step(f"Send text element with locator: '{locator}' and text send is: {text}"):
                self.log.info(f"Send text element with locator: '{locator}' and text send is: {text}")
        except Exception as e:
            with allure.step(f"Unable sent text on element: {locator}, Exception: {e}"):
                self.log.error(f"Unable sent text on element: {locator}, Exception: {e}")
                self.general_actions.screenshot(locator)
            assert False
