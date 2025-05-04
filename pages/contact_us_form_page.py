from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications


class ContactForm(BasePage):
    # Buttons
    contact_us_form_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/ContactU1s')  # Locate element by id
    submit_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn2')  # Locate element by id

    # Text
    contact_us_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contact Us form")')  # Locate element by text
    enter_name = (AppiumBy.ID, 'com.code2lead.kwad:id/Et2')  # Locate element by id
    enter_email = (AppiumBy.ID, 'com.code2lead.kwad:id/Et3')  # Locate element by id
    enter_address = (AppiumBy.ID, 'com.code2lead.kwad:id/Et6')  # Locate element by id
    enter_mobile_number = (AppiumBy.ID, 'com.code2lead.kwad:id/Et7')  # Locate element by id

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)

    def open_contact_us(self):
        self.ui_actions.press(self.contact_us_form_btn)

    def verify_contact_page(self):
        page_title = self.ui_verifications.is_element_display(self.contact_us_title, "text")
        assert page_title
        text = self.ui_verifications.get_element_text(self.contact_us_title)
        self.log.info(f"{text} title verified")

    def fill_in_details(self, name, email, address, phone_number):
        self.ui_actions.fill_in_text(self.enter_name, name)
        self.ui_actions.fill_in_text(self.enter_email, email)
        self.ui_actions.fill_in_text(self.enter_address, address)
        self.ui_actions.fill_in_text(self.enter_mobile_number, phone_number)
        self.ui_actions.log.info("All text are filled in successfully")

    def press_on_submit(self):
        self.ui_actions.press(self.submit_btn)
        text = self.ui_verifications.get_element_text(self.submit_btn)
        self.log.info(f"{text} button is press with success")
