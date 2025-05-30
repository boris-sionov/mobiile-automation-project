import allure
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class ContactForm(BasePage):
    """
    Page Object for the Contact Form screen.
    Handles field inputs and button actions using UIActions and UIVerifications.
    """

    def __init__(self, driver):
        """
        Initialize ContactForm with driver and define locators.
        """
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
            },

            'text':{
                'contact us title': self.get_by_locator(LocatorType.TEXT, 'Contact Us form'),
            }

        }

    @allure.step("Fill text '{text}' into '{field_name}' field")
    def fill_text(self, field_name, text):
        """
        Fill the given text into the specified input field.
        :param field_name: Key name of the field in the 'fields' locator dictionary.
        :param text: Text to input into the field.
        """
        field_locator = self.get_page_locator('fields', field_name)
        self.ui_actions.fill_in_text(field_locator, text)

    @allure.step("Click on '{button}' button")
    def click_on_button(self, button):
        """
        Click the specified button using UIActions.
        :param button: Key name of the button in the 'buttons' locator dictionary.
        """
        button_locator = self.get_page_locator('buttons', button)
        self.ui_actions.press(button_locator)

    @allure.step("Verifying title '{expected_title}' for page element: {page_title}")
    def verify_page_title(self, page_title, expected_title):
        """Verify that the page title matches the expected title."""
        with allure.step(f"Verifying title '{expected_title}' for page element: {page_title}"):
            title_locator = self.get_page_locator('text', page_title)
            self.ui_verifications.verify_text_in_element(title_locator, expected_title)
