from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage


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
        self.driver = driver

    def open_contact_us(self):
        self.press(self.contact_us_form_btn)

    def verify_contact_page(self):
        page_title = self.is_element_display('text', self.contact_us_title)
        assert page_title
        text = self.get_element_text('text',self.contact_us_title)
        self.log.info(f"{text} title verified")

    def fill_in_details(self, name, email, address, phone_number):
        self.fill_in_text(name, 'id', self.enter_name)
        self.fill_in_text(email, 'id', self.enter_email)
        self.fill_in_text(address, 'id', self.enter_address)
        self.fill_in_text(phone_number, 'id', self.enter_mobile_number)
        self.log.info("All text are filled in successfully")

    def press_on_submit(self):
        self.press('id', self.submit_btn)
        text = self.get_element_text('id', self.submit_btn)
        self.log.info(f"{text} button is press with success")
