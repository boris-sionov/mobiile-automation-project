
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class ScrollViewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'no button': self.get_by_locator(LocatorType.ID, 'android:id/button2'),
                'yes button': self.get_by_locator(LocatorType.ID, 'android:id/button1'),
                **{f'button {i}': self.get_by_locator(LocatorType.TEXT, f'BUTTON{i}') for i in range(1, 17)}
            },

            'text': {
                'alert popup title': self.get_by_locator(LocatorType.ID, 'alertTitle'),
                'alert message text': self.get_by_locator(LocatorType.ID, 'android:id/message'),
                'scroll view title': self.get_by_locator(LocatorType.TEXT, 'ScrollView')
            },
        }

    def click_on_button(self, button):
        button_locator = self.validate_locator_key(self.locators['buttons'], button)
        self.ui_actions.press_auto(button_locator)

    def verify_popup_text(self, actual_text_locator, text):
        text_locator = self.validate_locator_key(self.locators['text'], actual_text_locator)
        self.ui_verifications.verify_text_in_element(text_locator, text)

    def verify_popup_not_appear(self, popup):
        popup_locator = self.validate_locator_key(self.locators['text'], popup)
        self.ui_verifications.is_element_not_displayed(popup_locator)

