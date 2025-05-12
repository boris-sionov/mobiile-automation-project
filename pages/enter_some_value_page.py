
import allure
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class EnterSomeValuePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'submit button': self.get_by_locator(LocatorType.ID, 'Btn1'),
            },

            'fields': {
                'enter some value field': self.get_by_locator(LocatorType.CLASS_NAME, 'android.widget.EditText')
            },

            'text': {
                'enter some value title': self.get_by_locator(LocatorType.TEXT, 'Enter some Value'),
                'preview text': self.get_by_locator(LocatorType.ID, 'Tv1'),
            }

        }

    def fill_text(self, field_name, text):
        field_locator = self.validate_locator_key(self.locators['fields'], field_name)
        self.ui_actions.fill_in_text(field_locator, text)

    def click_on_button(self, button):
        button_locator = self.validate_locator_key(self.locators['buttons'], button)
        self.ui_actions.press(button_locator)

    def verify_preview_text(self, actual_text_locator, text):
        text_locator = self.validate_locator_key(self.locators['text'], actual_text_locator)
        self.ui_verifications.verify_text_in_element(text_locator, text)
