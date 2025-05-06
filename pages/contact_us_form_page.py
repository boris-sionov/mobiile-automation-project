from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'submit button': self.get_by_locator(LocatorType.ID, 'Btn2'),
            },

            'fields': {
                'enter name field': self.get_by_locator(LocatorType.XPATH, 'com.code2lead.kwad:id/Et2'),
                'enter email field': self.get_by_locator(LocatorType.XPATH, 'com.code2lead.kwad:id/Et3'),
                'enter address field': self.get_by_locator(LocatorType.XPATH, 'com.code2lead.kwad:id/Et6'),
                'enter mobile field': self.get_by_locator(LocatorType.XPATH, 'com.code2lead.kwad:id/Et7'),
            }
        }

    def fill_in_details(self,field_name, text):
        field_locator = self.validate_locator_key(self.locators['fields'], field_name)
        self.ui_actions.fill_in_text(field_locator, text)

    def click_on_button(self, button):
        button_locator = self.validate_locator_key(self.locators['buttons'], button)
        self.ui_actions.press(button_locator)
