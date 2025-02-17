import time

import allure
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)

    # Buttons
    enter_some_value_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue')   # Locate element by id
    contact_us_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/ContactUs')   # Locate element by id
    scroll_view_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/ScrollView')   # Locate element by id
    tab_activity_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/TabView')   # Locate element by id
    zoom_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Zoom')   # Locate element by id
    login_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Login')   # Locate element by id
    long_click_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/LongClick')   # Locate element by id
    time_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Time')   # Locate element by id
    date_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Date')   # Locate element by id
    hybrid_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/hybrid')   # Locate element by id
    pinch_in_out_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/pinch')   # Locate element by id
    drag_and_drop_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/drag')   # Locate element by id
    crash_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/crash')   # Locate element by id
    auto_suggestion_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/autocomlete')   # Locate element by id

    # Text
    appium_demo_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Appium Demo")')        # Locate element by text
    enter_some_value_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter some Value")')  # Locate element by text
    contact_us_form_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contact Us form")')   # Locate element by text
    scroll_view_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ScrollView")')   # Locate element by text
    tab_view_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tab View")')   # Locate element by text
    login_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login Page")')   # Locate element by text
    time_activity_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Time Activity")')   # Locate element by text
    date_activity_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Date Activity")')   # Locate element by text
    hybrid_activity_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Hybrid Activity")')   # Locate element by text

    # Long Press test
    get_your_password_title = (AppiumBy.ID, 'android:id/alertTitle')
    email_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Email")')
    submit_btn = (AppiumBy.ID, 'android:id/button1')
    cancel_btn = (AppiumBy.ID, 'android:id/button2')

    # Drop and drag test
    drag_text = (AppiumBy.ID, 'com.code2lead.kwad:id/lbl')

    # Pinch in/out test
    android_image = (AppiumBy.ID, 'com.code2lead.kwad:id/imageView')

    # Zoom test
    klo_image = (AppiumBy.ID, 'com.code2lead.kwad:id/imageView')

    def open_enter_some_value_page(self, expected):
        with allure.step(f"Pressing on {expected} button "):
            self.ui_actions.press(self.enter_some_value_btn)
        with allure.step(f"Verify text: {expected}"):
            self.ui_verifications.verify_text_in_element(self.enter_some_value_title, expected)
        with allure.step(f"Page {self.ui_verifications.get_element_text(self.enter_some_value_title)} is opened "):
            self.log.info(f"Page is opened {self.ui_verifications.get_element_text(self.enter_some_value_title)}")

    def open_contact_us_page(self, expected):
        with allure.step(f"Pressing on {expected} button: "):
            self.ui_actions.press(self.contact_us_btn)
        with allure.step(f"Verify text: {expected}"):
            self.ui_verifications.verify_text_in_element(self.contact_us_form_title, expected)
        with allure.step(f"Page is opened {self.ui_verifications.get_element_text(self.contact_us_form_title)}"):
            self.log.info(f"Page is opened {self.ui_verifications.get_element_text(self.contact_us_form_title)}")

    def open_scroll_view_page(self, expected):
        with allure.step(f"Pressing on button: {expected}"):
            self.ui_actions.press(self.scroll_view_btn)
        with allure.step(f"Verify text: {expected}"):
            self.ui_verifications.verify_text_in_element(self.scroll_view_title, expected)
        with allure.step(f"Page is opened {self.ui_verifications.get_element_text(self.scroll_view_title)}"):
            self.log.info(f"Page is opened {self.ui_verifications.get_element_text(self.scroll_view_title)}")

    def open_tab_view_page(self, expected):
        self.ui_actions.press(self.tab_activity_btn)
        self.ui_verifications.verify_text_in_element(self.tab_view_title, expected)

    def open_zoom_page(self):
        self.ui_verifications.compare_image(self.zoom_btn)

    def open_login_page(self, expected):
        with allure.step("Pressing on Login page button:"):
            self.ui_actions.press(self.login_btn)
            with allure.step(f"Verify Login page: {expected} is opened"):
                self.ui_verifications.verify_text_in_element(self.login_title, expected)

    def open_long_click_page(self, expected):
        self.ui_actions.press_with_scroll(self.long_click_btn)
        self.ui_verifications.verify_text_in_element(self.get_your_password_title, expected)
        time.sleep(3)
        self.ui_actions.press(self.cancel_btn)

    def open_time_page(self, expected):
        self.ui_actions.press_with_scroll(self.time_btn)
        self.ui_verifications.verify_text_in_element(self.time_activity_title, expected)

    def open_date_page(self, expected):
        self.ui_actions.press_with_scroll(self.date_btn)
        self.ui_verifications.verify_text_in_element(self.date_activity_title, expected)

    def open_hybrid_page(self, expected):
        self.ui_actions.press_with_scroll(self.hybrid_btn)
        self.ui_verifications.verify_text_in_element(self.hybrid_activity_title, expected)

    def open_pinch_in_out_page(self, expected):
        self.ui_actions.press_with_scroll(self.pinch_in_out_btn)
        self.ui_verifications.is_element_display(self.android_image, expected)

    def open_drag_and_drop_page(self, expected):
        self.ui_actions.press_with_scroll(self.drag_and_drop_btn)
        self.ui_verifications.verify_text_in_element(self.drag_text, expected)

    def open_crash_page(self):
        before_crash_pack = self.driver.current_package
        self.log.info(f"App package before pressing on crash button: {before_crash_pack}")
        self.ui_actions.press_with_scroll(self.crash_btn)
        time.sleep(2)
        after_crash_pack = self.driver.current_package
        if after_crash_pack != 'com.code2lead.kwad':
            self.log.info(f"App is crashed current package changed to: {after_crash_pack}. "
                          f"Trying to reopen app {before_crash_pack}")
            self.driver.activate_app('com.code2lead.kwad')
            time.sleep(2)
            reopen_app = self.driver.current_package
            self.log.info(f"App package after reopen the app: {reopen_app}")
            if reopen_app == 'com.code2lead.kwad':
                self.log.info(f"App Reopened {reopen_app}")
            time.sleep(2)

    def open_auto_suggestion_page(self, expected):
        self.ui_actions.press_with_scroll(self.auto_suggestion_btn)
        self.ui_verifications.verify_text_in_element(self.auto_suggestion_btn, expected)