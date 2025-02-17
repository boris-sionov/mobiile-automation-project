import os
import time

import allure

from base.base_page import BasePage
import cv2
from skimage.metrics import structural_similarity as ssim
from base.general_actions import GeneralActions


class UIVerifications(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)

    # Verify if element appears
    def is_element_display(self, locator, expected):
        try:
            element = self.wait_for_visible(locator)
            actual = element.get_attribute('resource-id')
            assert actual == expected, f"Expected attribute:'{expected}', but got '{actual}'"
            return element.is_displayed()

        except Exception as e:
            self.log.error(f"Element is not found: {locator}, Exception: {e}")
            self.general_actions.screenshot(locator)
            assert False

    # Method to assert text
    def verify_text_in_element(self, locator, expected_text):
        element = self.wait_for_visible(locator)
        actual_text = element.text

        if expected_text == actual_text:
            with allure.step(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'."):
                self.log.info(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'.")
        else:
            with allure.step(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'."):
                self.log.error(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'.")
            assert expected_text == actual_text, f"Expected text: '{expected_text}', but got: '{actual_text}'"

    # Method to check if app is installed.
    def is_app_installed(self, app_package):
        if self.driver.is_app_installed(app_package):
            with allure.step(f"{app_package} is installed continue to tests"):
                self.log.info(f"{app_package} is installed continue to tests")
        else:
            with allure.step(f"{app_package} is not installed"):
                self.log.info(f"{app_package} is not installed")
                self.general_actions.screenshot(app_package)
            assert False

    # Method to get text appears on an element
    def get_element_text(self, locator):
        try:
            element = self.wait_for_visible(locator)  # Use wait to make sure element is visible
            text_in_element = element.text  # Get the text attribute from the element
            self.log.info(f"Text from element with locator: {text_in_element}")
            return text_in_element
        except Exception as e:
            with allure.step(f"Unable to get text from element: {locator}. Exception: {e}"):
                self.log.error(f"Unable to get text from element: {locator}. Exception: {e}")
                self.general_actions.screenshot(locator)
            return None

    def get_element_size(self, locator):
        element = self.wait_for_visible(locator)
        size = element.size
        y = element.location['y']
        return size  # Return size for comparison

    def compare_image(self, locator):
        element = self.wait_for_visible(locator)

        # Read the before image
        before_press = self.general_actions.screenshot("Before_test")
        current_img = cv2.imread(self.screenshot_directory + before_press, cv2.IMREAD_UNCHANGED)

        # Convert the before image to grayscale
        gray1 = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)

        # Perform the action (click element)
        element.click()
        time.sleep(2)

        # Read the after image
        after_press = self.general_actions.screenshot("After_test")
        after_img = cv2.imread(self.screenshot_directory + after_press, cv2.IMREAD_UNCHANGED)

        # Convert the after image to grayscale
        gray2 = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

        # Calculate SSIM between the two images
        score, _ = ssim(gray1, gray2, full=True)
        score = round(score, 3)

        # Log SSIM score
        if score > 0.99:
            with allure.step(f"SSIM Score After pressing on zoom button: {score} "
                             f"is to high, pictures are probably the same."
                             f" KLO button is not changed Zoom didn't do anything."):
                self.log.error(f"SSIM Score After pressing on zoom button: {score} "
                               f"is to high, pictures are probably the same."
                               f" KLO button is not changed Zoom didn't do anything.")
                assert score > 0.99, f"Test if failed: {score} is higher than 0.98"
                raise AssertionError("Test failed")
        else:
            with allure.step(f"Test is passed score is: {score}. "
                             f"SSIM score is changed and lower than 0.98. "
                             f"KLO button is zoomed"):
                self.log.info(f"Test is passed score is: {score}. "
                              f"SSIM score is changed and lower than 0.98. "
                              f"KLO button is zoomed")
