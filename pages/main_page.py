import time

import allure

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'enter some value button': self.get_by_locator(LocatorType.ID, 'EnterValue'),
                'contact us button': self.get_by_locator(LocatorType.ID, 'ContactUs'),
                'scroll view button': self.get_by_locator(LocatorType.ID, 'ScrollView'),
                'tab activity button': self.get_by_locator(LocatorType.ID, 'TabView'),
                'zoom button': self.get_by_locator(LocatorType.ID, 'Zoom'),
                'login button': self.get_by_locator(LocatorType.ID, 'Login'),
                'long click button': self.get_by_locator(LocatorType.ID, 'LongClick'),
                'time button': self.get_by_locator(LocatorType.ID, 'Time'),
                'date button': self.get_by_locator(LocatorType.ID, 'Date'),
                'hybrid button': self.get_by_locator(LocatorType.ID, 'hybrid'),
                'pinch button': self.get_by_locator(LocatorType.ID, 'pinch'),
                'drag and drop button': self.get_by_locator(LocatorType.ID, 'drag'),
                'crash button': self.get_by_locator(LocatorType.ID, 'crash'),
                'auto suggestion button': self.get_by_locator(LocatorType.ID, 'autocomlete'),
                'submit button': self.get_by_locator(LocatorType.ID, 'android:id/button1'),
                'cancel button': self.get_by_locator(LocatorType.ID, 'android:id/button2'),

            },
            'text': {
                'appium demo title': self.get_by_locator(LocatorType.TEXT, 'Appium Demo'),
                'enter some value title': self.get_by_locator(LocatorType.TEXT, 'Enter some Value'),
                'contact us title': self.get_by_locator(LocatorType.TEXT, 'Contact Us form'),
                'scroll view title': self.get_by_locator(LocatorType.TEXT, 'ScrollView'),
                'tab view title': self.get_by_locator(LocatorType.TEXT, 'Tab View'),
                'login title': self.get_by_locator(LocatorType.TEXT, 'Login Page'),
                'time activity title': self.get_by_locator(LocatorType.TEXT, 'Time Activity'),
                'date activity title': self.get_by_locator(LocatorType.TEXT, 'Date Activity'),
                'hybrid activity title': self.get_by_locator(LocatorType.TEXT, 'Hybrid Activity'),
                'email text': self.get_by_locator(LocatorType.TEXT, 'Email'),
                'get your password title': self.get_by_locator(LocatorType.ID, 'android:id/alertTitle'),
                'draggable text': self.get_by_locator(LocatorType.ID, 'lbl'),

            },

            'images': {
                'android image': self.get_by_locator(LocatorType.ID, 'imageView'),
            }
        }

    def open_page(self, page_name):
        """Open desired page."""
        page_name = page_name.lower()
        with allure.step(f"Open page: {page_name}"):
            button_locator = self.validate_locator_key(self.locators['buttons'], page_name)
            self.ui_actions.press_auto(button_locator)

    def verify_page_title(self, page_title, expected_title):
        """Verify the page title text matches the expected value."""
        with allure.step(f"Verify text: {expected_title}"):
            title_locator = self.validate_locator_key(self.locators['text'], page_title)
            self.ui_verifications.verify_text_in_element(title_locator, expected_title)

    def verify_zoom(self, page_name):
        """Verify that the image enlarges after pressing the zoom button."""
        with allure.step(f"Verify image zoomed after pressing on {page_name}"):
            button_locator = self.validate_locator_key(self.locators['buttons'], page_name)
            self.ui_verifications.compare_image(button_locator)

    def click_on_button(self, button):
        """Press on a button."""
        with allure.step(f"Pressing on: {button} button"):
            button_locator = self.validate_locator_key(self.locators['buttons'], button)
            self.ui_actions.press(button_locator)

    def press_on_back(self):
        """Go back with device back button."""
        with allure.step(f"Pressing on: back button"):
            self.driver.back()

    def verify_image(self, image):
        """Verify image appears on the screen."""
        image_locator = self.validate_locator_key(self.locators['images'], image)
        self.ui_verifications.is_element_displayed(image_locator)

    def verify_app_crash(self, button, expected_package):
        """Verify that the app crashed after pressing on crash button and reopened  ."""
        locator = self.locators['buttons'].get(button)
        self.ui_verifications.verify_app_crash_and_recovery(locator, expected_package)
