import allure

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class ScrollViewPage(BasePage):
    """Page object for the Scroll View page."""

    def __init__(self, driver):
        """
        Initialize the ScrollViewPage with driver, actions, verifications, and locators.
        """
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

    @allure.step("Click on '{button}' button")
    def click_on_button(self, button):
        """
        Click on a button by name.

        Args:
            button (str): Key for the button locator in the dictionary.
        """
        button_locator = self.get_page_locator('buttons', button)
        self.ui_actions.press(button_locator)

    @allure.step("Verify popup text '{expected_text}' is displayed at '{actual_text_locator}'")
    def verify_popup_text(self, actual_text_locator, expected_text):
        """
        Verify that the popup text matches the expected text.

        Args:
            actual_text_locator (str): Key for the text element locator.
            expected_text (str): Expected text value.
        """
        text_locator = self.get_page_locator('text', actual_text_locator)
        self.ui_verifications.verify_text_in_element(text_locator, expected_text)

    @allure.step("Verifying title '{expected_title}' for page element: {page_title}")
    def verify_page_title(self, page_title, expected_title):
        """Verify that the page title matches the expected title."""
        title_locator = self.get_page_locator('text', page_title)
        self.ui_verifications.verify_text_in_element(title_locator, expected_title)


    @allure.step("Verify popup '{popup}' is not displayed")
    def verify_popup_not_appear(self, popup):
        """
        Verify that a popup element does not appear.

        Args:
            popup (str): Key for the popup text element locator.
        """
        popup_locator = self.get_page_locator('text', popup)
        self.ui_verifications.is_element_not_displayed(popup_locator)
