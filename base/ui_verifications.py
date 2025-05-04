import time

import allure
import cv2
from skimage.metrics import structural_similarity as ssim

from base.base_page import BasePage
from base.files_path import screenshot_directory
from base.general_actions import GeneralActions
from base.ui_actions import UIActions


class UIVerifications(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.ui_actions = UIActions(driver)

    # Verify if element appears
    def is_element_displayed(self, locator):
        try:
            element = self.wait_for_visible(locator)
            self.log.info(f"{element} element found: {element.get_attribute('resource-id')} with resource-id attribute")
            return element.is_displayed()
        except Exception as e:
            self.log.error(f"Element is not found: {locator}, Exception: {e}")
            self.general_actions.screenshot(locator)
            return False

    # Method to assert text
    def verify_text_in_element(self, locator, expected_text):
        element = self.wait_for_visible(locator)
        actual_text = element.text

        if expected_text == actual_text:
            with allure.step(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'."):
                self.log.info(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'.")
        else:
            screenshot_path = screenshot_directory + self.general_actions.screenshot("Text_Verification_Fail")
            with allure.step(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'."):
                allure.attach.file(screenshot_path, name="Text Verification Failure Screenshot", attachment_type=allure.attachment_type.PNG)
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
        return size  # Return size for comparison

    def compare_image(self, locator):
        element = self.wait_for_visible(locator)

        # Capture before image
        before_press = self.general_actions.screenshot("Before_test")
        before_img = cv2.imread(screenshot_directory + before_press, cv2.IMREAD_UNCHANGED)
        gray1 = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)

        # Click and wait so the image will be zoomed
        element.click()
        time.sleep(2)

        # Capture after image
        after_press = self.general_actions.screenshot("After_test")
        after_img = cv2.imread(screenshot_directory + after_press, cv2.IMREAD_UNCHANGED)
        gray2 = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

        # SSIM comparison
        score, diff = ssim(gray1, gray2, full=True)
        score = round(score, 3)
        diff = (diff * 255).astype("uint8")
        cv2.imwrite(screenshot_directory + "diff.png", diff)

        if score > 0.99:
            with allure.step(f"FAIL: SSIM {score} is too high — no visible change"):
                self.log.error(f"FAIL: SSIM {score} is too high — zoom may have failed.")
                assert score < 0.98, f"FAIL: SSIM {score} is too high"
        else:
            with allure.step(f"PASS: SSIM {score} is low — zoom succeeded"):
                self.log.info(f"PASS: SSIM {score} is low — change detected.")

    def verify_app_crash_and_recovery(self, locator, expected_package, wait_time=2):
        before_crash_package = self.driver.current_package
        self.log.info(f"App package before pressing crash button: {before_crash_package}")

        self.ui_actions.press_auto(locator)
        time.sleep(wait_time)

        after_crash_package = self.driver.current_package
        if after_crash_package != expected_package:
            self.log.warning(
                f"App appears crashed. Current package: {after_crash_package}. Reopening {expected_package}")

            self.driver.activate_app(expected_package)
            time.sleep(wait_time)

            reopened_package = self.driver.current_package
            self.log.info(f"App package after reopening: {reopened_package}")

            assert reopened_package == expected_package, \
                f"App failed to reopen. Current package: {reopened_package}"
            self.log.info("App recovered successfully after crash.")
        else:
            self.log.info("App did not crash after pressing the button.")
