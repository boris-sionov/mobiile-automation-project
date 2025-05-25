import allure
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


@allure.epic("Input Forms")
@allure.feature("Enter Some Value Page")
class EnterSomeValuePage(BasePage):
    """
    Page Object for the 'Enter Some Value' screen.
    Handles input actions, button presses, and text verifications.
    """

    def __init__(self, driver):
        """
        Initialize EnterSomeValuePage with driver and define locators.
        """
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

    @allure.step("Fill text '{text}' into '{field_name}' field")
    def fill_text(self, field_name, text):
        """
        Fill the given text into the specified input field.
        """
        field_locator = self.validate_locator_key(self.locators['fields'], field_name)
        self.ui_actions.fill_in_text(field_locator, text)

    @allure.step("Click on '{button}' button")
    def click_on_button(self, button):
        """
        Click the specified button using UIActions.
        """
        button_locator = self.get_page_locator('buttons', button)
        self.ui_actions.press(button_locator)

    @allure.step("Verifying title '{expected_title}' for page element: {page_title}")
    def verify_page_title(self, page_title, expected_title):
        """Verify that the page title matches the expected title."""
        with allure.step(f"Verifying title '{expected_title}' for page element: {page_title}"):
            title_locator = self.get_page_locator('text', page_title)
            self.ui_verifications.verify_text_in_element(title_locator, expected_title)

    @allure.step("Verify preview text in '{actual_text_locator}' equals '{text}'")
    def verify_preview_text(self, actual_text_locator, text):
        """
        Verify that the expected text is present in the given text element.
        """
        text_locator = self.get_page_locator('text', actual_text_locator)
        self.ui_verifications.verify_text_in_element(text_locator, text)
