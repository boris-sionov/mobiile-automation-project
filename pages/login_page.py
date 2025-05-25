import allure
from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications
from utilities.locator_type import LocatorType


class LoginPage(BasePage):
    """
    Page Object Model for the Login Page.
    Includes login functionality, credential verification, and admin entry.
    """

    def __init__(self, driver):
        """
        Initialize LoginPage with driver and define button locators.
        """
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
        self.locators = {
            'buttons': {
                'submit button': self.get_by_locator(LocatorType.ID, 'Btn1'),
            }
        }

    # Buttons
    login_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn3')

    # Text
    login_page_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login Page")')
    enter_email_box = (AppiumBy.ID, 'com.code2lead.kwad:id/Et4')
    enter_psw_box = (AppiumBy.ID, 'com.code2lead.kwad:id/Et5')
    wrong_credentials = (AppiumBy.ID, 'com.code2lead.kwad:id/Tv8')

    # Admin page
    enter_admin_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Admin")')
    enter_admin_box = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    submit_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn_admin_sub')
    preview_text = (AppiumBy.ID, 'com.code2lead.kwad:id/Tv_admin')

    @allure.step("Attempt login with incorrect credentials: {email} / {password}")
    def enter_incorrect_credentials(self, email, password, expected):
        """
        Attempt login with incorrect credentials and verify the expected error text.
        """
        with allure.step(f"Enter email: {email}"):
            self.ui_actions.fill_in_text(self.enter_email_box, email)
        with allure.step(f"Enter password: {password}"):
            self.ui_actions.fill_in_text(self.enter_psw_box, password)
        with allure.step("Click Login button"):
            self.ui_actions.press(self.login_btn)
        with allure.step(f"Verify error message: {expected}"):
            self.ui_verifications.verify_text_in_element(self.wrong_credentials, expected)

    @allure.step("Login with correct credentials: {email} / {password}")
    def enter_correct_credentials(self, email, password):
        """
        Log in with correct credentials.
        """
        with allure.step("Clear existing email and password fields"):
            self.ui_actions.clear_text(self.enter_email_box)
            self.ui_actions.clear_text(self.enter_psw_box)
        with allure.step(f"Enter email: {email}"):
            self.ui_actions.fill_in_text(self.enter_email_box, email)
        with allure.step(f"Enter password: {password}"):
            self.ui_actions.fill_in_text(self.enter_psw_box, password)
        with allure.step("Click Login button"):
            self.ui_actions.press(self.login_btn)

    @allure.step("Enter admin screen and verify text change with input: {text}")
    def enter_admin_page(self, text):
        """
        Fill in text in the admin field and verify preview text changes after submission.
        """
        before_press = self.ui_verifications.get_element_text(self.preview_text)
        self.log.info(f"Before pressing submit, preview text: '{before_press}'")

        with allure.step(f"Fill text into admin field: {text}"):
            self.ui_actions.fill_in_text(self.enter_admin_box, text)

        with allure.step("Click Submit button"):
            self.ui_actions.press(self.submit_btn)

        after_press = self.ui_verifications.get_element_text(self.preview_text)
        self.log.info(f"After pressing submit, preview text: '{after_press}'")

        with allure.step(f"Verify preview text changed from '{before_press}' to '{after_press}'"):
            assert before_press != after_press, "Text did not change"
