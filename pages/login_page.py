import time

import allure
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)
    # Buttons
    login_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn3')  # Locate element by id

    # Text
    login_page_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login Page")')  # Locate element by text
    enter_email_box = (AppiumBy.ID, 'com.code2lead.kwad:id/Et4')  # Locate element by id
    enter_psw_box = (AppiumBy.ID, 'com.code2lead.kwad:id/Et5')  # Locate element by id
    wrong_credentials = (AppiumBy.ID, 'com.code2lead.kwad:id/Tv8')  # Locate element by id

    # Enter admin page
    enter_admin_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Admin")')  # Locate element by text
    enter_admin_box = (AppiumBy.CLASS_NAME, 'android.widget.EditText')  # Locate element by class
    submit_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn_admin_sub')
    preview_text = (AppiumBy.ID, 'com.code2lead.kwad:id/Tv_admin')

    def enter_incorrect_credentials(self, email, password, expected):
        with allure.step(f"Enter {email} text to email text box"):
            self.ui_actions.fill_in_text(self.enter_email_box, email)
            with allure.step(f"Enter {password} text to password text box"):
                self.ui_actions.fill_in_text(self.enter_psw_box, password)
            with allure.step("Pressing on a button: Login"):
                self.ui_actions.press(self.login_btn)
                self.ui_verifications.verify_text_in_element(self.wrong_credentials, expected)

    def enter_correct_credentials(self, email, password):
        with allure.step(f"Enter {email} text to email text box"):
            self.ui_actions.fill_in_text(self.enter_email_box, email)
            with allure.step(f"Enter {password} text to password text box"):
                self.ui_actions.fill_in_text(self.enter_psw_box, password)
            with allure.step("Pressing on a button: Login"):
                self.ui_actions.press(self.login_btn)

    def enter_admin_page(self, text):
        before_press = self.ui_verifications.get_element_text(self.preview_text)
        self.log.info(f"Before enter some text in the box and pressing and pressing submit text appears: "
                      f" '{before_press}'")
        with allure.step(f"Fill {text} text to enter admin text box"):
            self.ui_actions.fill_in_text(self.enter_admin_box, text)
            self.ui_actions.press(self.submit_btn)
            after_press = self.ui_verifications.get_element_text(self.preview_text)
            with allure.step(f"After pressing submit text appears: '{after_press}'"):
                self.log.info(f"After pressing submit text appears: '{after_press}'")
            with allure.step(f"Text is changed from: '{before_press}' to: '{after_press}'"):
                self.log.info(f"Text is changed from: '{before_press}' to: '{after_press}'")
                assert before_press != after_press, f"Text is not changed"
