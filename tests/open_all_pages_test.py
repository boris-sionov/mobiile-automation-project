import time
import unittest

import allure
import pytest
import utilities.custom_logger as CL
from utilities.page_factory import PageFactory


@allure.description("All Pages Test")
@pytest.mark.usefixtures("setup_class")
class TestAllPages(PageFactory):
    @allure.title("Test 01: This test is checking that all pages opened and verify correct title of each page")
    def test_all_pages(self):
        # CL.allure_step_logs("Step 1: Open Enter some value page")
        with allure.step("Step 1: Open Enter some value page"):
            self.main_page.open_enter_some_value_page('Enter some Value')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 2: Open Contact us page form page"):
            self.main_page.open_contact_us_page('Contact Us form')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 3: Open Scroll View page"):
            self.main_page.open_scroll_view_page('ScrollView')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 4: Open Tab activity page"):
            self.main_page.open_tab_view_page('Tab View')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 5: Open Zoom page"):
            self.main_page.open_zoom_page()

        with allure.step("Step 6: Open Login page"):
            self.main_page.open_login_page('Login Page')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 7: Open Long click page"):
            self.main_page.open_long_click_page('Get your password')

        with allure.step("Step 8: Open Time page"):
            self.main_page.open_time_page('Time Activity')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 9: Open Date page"):
            self.main_page.open_date_page("Date Activity")
        time.sleep(2)
        self.driver.back()

        with allure.step("Step 10: Open Hybrid page"):
            self.main_page.open_hybrid_page("Hybrid Activity")
        time.sleep(2)
        self.driver.back()

        with allure.step("Step 11: Open Pinch in out page"):
            self.main_page.open_pinch_in_out_page('com.code2lead.kwad:id/imageView')
        time.sleep(1)
        self.driver.back()

        with allure.step("Step 12: Open Drag and drop page"):
            self.main_page.open_drag_and_drop_page("Draggable Text")
        time.sleep(2)
        self.driver.back()

        with allure.step("Step 13: Open Crash page"):
            self.main_page.open_crash_page()

        # CL.allure_step_logs("Step 14: Open Auto Suggestion page")
        # self.mainPage.auto_suggestion_btn("Hybrid Activity")
        # time.sleep(2)
        # self.driver.back()





