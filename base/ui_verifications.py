import time
import allure
import cv2
from selenium.common import TimeoutException, NoSuchElementException
from skimage.metrics import structural_similarity as ssim

from base.base_page import BasePage
from base.files_path import screenshot_directory
from base.general_actions import GeneralActions
from base.ui_actions import UIActions


class UIVerifications(BasePage):
    """
    A class for various UI verification methods.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.ui_actions = UIActions(driver)

    @allure.step("Verify if element '{locator}' is displayed")
    def is_element_displayed(self, locator):
        """
        Checks if the given element is displayed on the screen.

        :param locator: The locator for the UI element.
        :return: True if element is visible, else False.
        """
        try:
            element = self.wait_for_visible(locator)
            self.log.info(f"{element} element found: {element.get_attribute('resource-id')}")
            return element.is_displayed()
        except Exception as e:
            self.log.error(f"Element not found: {locator}, Exception: {e}")
            self.general_actions.screenshot(locator)
            return False

    @allure.step("Verify element '{locator}' is not displayed")
    def is_element_not_displayed(self, locator):
        """
        Verifies that the element is not displayed on the screen.

        :param locator: The locator for the UI element.
        """
        try:
            self.wait_for_not_visible(locator)
            self.log.info(f"Confirmed element {locator} is not displayed.")
            return True
        except (TimeoutException, NoSuchElementException):
            self.log.error(f"Element {locator} is still visible after timeout.")
            file_name = self.general_actions.generate_screenshot_name("element_not_displayed")
            self.general_actions.screenshot(file_name)
            assert False, f"Element {locator} is still displayed after timeout!"

    @allure.step("Verify text in element '{locator}' is '{expected_text}'")
    def verify_text_in_element(self, locator, expected_text):
        """
        Verifies the text in an element matches the expected text.

        :param locator: The locator for the UI element.
        :param expected_text: Expected string text.
        """
        element = self.wait_for_visible(locator)
        actual_text = element.text

        if expected_text == actual_text:
            self.log.info(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'.")
        else:
            screenshot_path = screenshot_directory + self.general_actions.screenshot("Text_Verification_Fail")
            allure.attach.file(screenshot_path, name="Text Verification Failure Screenshot",
                               attachment_type=allure.attachment_type.PNG)
            self.log.error(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'.")
            assert expected_text == actual_text, f"Expected text: '{expected_text}', but got: '{actual_text}'"

    @allure.step("Check if app '{app_package}' is installed")
    def is_app_installed(self, app_package):
        """
        Verifies if the app is installed on the device.

        :param app_package: The app's package name.
        """
        if self.driver.is_app_installed(app_package):
            self.log.info(f"{app_package} is installed. Continuing tests.")
        else:
            self.log.info(f"{app_package} is not installed.")
            self.general_actions.screenshot(app_package)
            assert False

    @allure.step("Get text from element '{locator}'")
    def get_element_text(self, locator):
        """
        Retrieves the text from the given element.

        :param locator: The locator for the UI element.
        :return: Text content of the element.
        """
        try:
            element = self.wait_for_visible(locator)
            text_in_element = element.text
            self.log.info(f"Text from element: {text_in_element}")
            return text_in_element
        except Exception as e:
            self.log.error(f"Unable to get text from element: {locator}. Exception: {e}")
            self.general_actions.screenshot(locator)
            return None

    @allure.step("Get size of element '{locator}'")
    def get_element_size(self, locator):
        """
        Gets the size of a UI element.

        :param locator: The locator for the UI element.
        :return: Dictionary with element width and height.
        """
        element = self.wait_for_visible(locator)
        return element.size

    @allure.step("Compare image state before and after pressing element '{locator}'")
    def compare_image(self, locator):
        """
        Compares two screenshots before and after a press action to validate visual changes using SSIM.

        :param locator: The locator for the UI element.
        """
        element = self.wait_for_visible(locator)

        before_press = self.general_actions.screenshot("Before_test")
        before_img = cv2.imread(screenshot_directory + before_press, cv2.IMREAD_UNCHANGED)
        gray1 = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)

        element.click()
        time.sleep(2)

        after_press = self.general_actions.screenshot("After_test")
        after_img = cv2.imread(screenshot_directory + after_press, cv2.IMREAD_UNCHANGED)
        gray2 = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

        score, diff = ssim(gray1, gray2, full=True)
        score = round(score, 3)
        diff = (diff * 255).astype("uint8")
        cv2.imwrite(screenshot_directory + "diff.png", diff)

        if score > 0.99:
            self.log.error(f"FAIL: SSIM {score} is too high — zoom may have failed.")
            assert score < 0.98, f"FAIL: SSIM {score} is too high"
        else:
            self.log.info(f"PASS: SSIM {score} is low — change detected.")

    @allure.step("Verify app crash and recovery using element '{locator}' and expected package '{expected_package}'")
    def verify_app_crash_and_recovery(self, locator, expected_package, wait_time=2):
        """
        Verifies app crashes and recovers properly.

        :param locator: Locator for the button expected to cause crash.
        :param expected_package: Package name to verify after recovery.
        :param wait_time: Wait duration between crash and recovery attempts.
        """
        before_crash_package = self.driver.current_package
        self.log.info(f"App package before crash: {before_crash_package}")

        self.ui_actions.press(locator)
        time.sleep(wait_time)

        after_crash_package = self.driver.current_package
        if after_crash_package != expected_package:
            self.log.warning(f"App crashed. Reopening {expected_package}")
            self.driver.activate_app(expected_package)
            time.sleep(wait_time)

            reopened_package = self.driver.current_package
            self.log.info(f"App package after reopening: {reopened_package}")

            assert reopened_package == expected_package, \
                f"App failed to reopen. Current package: {reopened_package}"
            self.log.info("App recovered successfully after crash.")
        else:
            self.log.info("App did not crash after pressing the button.")
