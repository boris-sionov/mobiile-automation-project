import allure

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class MainPage(BasePage):
    """Main page object containing UI actions and verifications for buttons, texts, and images."""

    def __init__(self, driver):
        """Initialize MainPage with driver and setup locators."""
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

    @allure.step("Opening page: {page_name}")
    def open_page(self, page_name):
        """Open the page by clicking the button associated with page_name."""
        button_locator = self.get_page_locator('buttons', page_name)
        self.ui_actions.press(button_locator)

    @allure.step("Verifying title '{expected_title}' for page element: {page_title}")
    def verify_page_title(self, page_title, expected_title):
        """Verify that the page title matches the expected title."""
        title_locator = self.get_page_locator('text', page_title)
        self.ui_verifications.verify_text_in_element(title_locator, expected_title)

    @allure.step("Verifying zoom functionality by pressing: {page_name}")
    def verify_zoom(self, page_name):
        """Verify that zoom functionality works by checking if the image enlarges."""
        button_locator = self.get_page_locator('buttons', page_name)
        self.ui_verifications.compare_image(button_locator)

    @allure.step("Clicking on button: {button}")
    def click_on_button(self, button):
        """Click a button identified by its name."""
        button_locator = self.get_page_locator('buttons', button)
        self.ui_actions.press(button_locator)

    @allure.step("Pressing device back button")
    def press_on_back(self):
        """Press the back button on the device."""
        self.driver.back()

    @allure.step("Verifying that image is displayed: {image}")
    def verify_image(self, image):
        """Check that the given image is displayed on the screen."""
        image_locator = self.get_page_locator('images', image)
        self.ui_verifications.is_element_displayed(image_locator)

    @allure.step("Verifying app crash and recovery after pressing: {button}")
    def verify_app_crash(self, button, expected_package):
        """Verify the app crashes and recovers when pressing a specific button."""
        locator = self.locators['buttons'].get(button)
        self.ui_verifications.verify_app_crash_and_recovery(locator, expected_package)
