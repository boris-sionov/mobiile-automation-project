import allure

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class TabActivity(BasePage):
    """
    Page Object for the Tab activity screen.
    Handles field inputs and button actions using UIActions and UIVerifications.
    """

    def __init__(self, driver):
        """
        Initialize TabActivity with driver and define locators.
        """
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'home': self.get_by_locator(LocatorType.ACCESSIBILITY_ID, 'Home'),
                'sport': self.get_by_locator(LocatorType.ACCESSIBILITY_ID,'Sport'),
                'movie': self.get_by_locator(LocatorType.ACCESSIBILITY_ID, 'Movie'),
            },

            'text': {
                'tab view title': self.get_by_locator(LocatorType.TEXT, 'Tab View'),
                'home fragment': self.get_by_locator(LocatorType.TEXT, 'HomeFragment'),
                'sport fragment': self.get_by_locator(LocatorType.TEXT, 'SportFragment'),
                'movie fragment': self.get_by_locator(LocatorType.TEXT, 'MovieFragment'),
            }
        }

    @allure.step("Fill text '{text}' into '{field_name}' field")
    def fill_text(self, field_name, text):
        """
        Fill the given text into the specified input field.
        :param field_name: Key name of the field in the 'fields' locator dictionary.
        :param text: Text to input into the field.
        """
        field_locator = self.get_page_locator('fields',field_name )
        self.ui_actions.fill_in_text(field_locator, text)

    @allure.step("Click on '{button}' button")
    def click_on_button(self, button):
        """
        Click the specified button using UIActions.
        :param button: Key name of the button in the 'buttons' locator dictionary.
        """
        button_locator = self.get_page_locator('buttons', button)
        self.ui_actions.press(button_locator)

    def verify_page_title(self, page_title, expected_title):
        """Verify that the page title matches the expected title."""
        with allure.step(f"Verify text: {expected_title}"):
            title_locator = self.get_page_locator('text', page_title)
            self.ui_verifications.verify_text_in_element(title_locator, expected_title)
