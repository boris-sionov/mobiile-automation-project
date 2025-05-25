"""
Test suite for verifying navigation and behavior of all pages in the app.
Each test opens a specific page, verifies its title or functionality,
and then navigates back to the main page.
"""

import time
import allure
import pytest
from utilities.page_factory import PageFactory


@allure.description("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_function")
class TestAllPages(PageFactory):
    """
    Test class for validating all accessible pages in the application.
    Inherits from PageFactory for access to page objects.
    """

    @allure.title("Test 01: Open 'Enter Some Value' page and verify correct title")
    def test01_enter_some_value(self):
        """
        Open 'Enter Some Value' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open 'Enter Some Value' page"):
            self.main_page.open_page('enter some value button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('enter some value title', 'Enter some Value')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 02: Open 'Contact us' page and verify correct title")
    def test02_contact_us(self):
        """
        Open 'Contact Us' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Contact us page"):
            self.main_page.open_page('contact us button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('contact us title', 'Contact Us form')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 03: Open 'Scroll View' page and verify correct title")
    def test03_scroll_view(self):
        """
        Open 'Scroll View' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Scroll View page"):
            self.main_page.open_page('scroll view button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('scroll view title', 'ScrollView')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 04: Open 'Tab Activity' page and verify correct title")
    def test04_tab_activity(self):
        """
        Open 'Tab Activity' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Tab Activity page"):
            self.main_page.open_page('tab activity button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('tab view title', 'Tab View')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 05: Test zoom on KLO button")
    def test05_zoom(self):
        """
        Test zoom functionality using the KLO button.
        """
        with allure.step("Step 1: Press on KLO to zoom it and verify zoom changed"):
            self.main_page.verify_zoom('zoom button')

    @allure.title("Test 06: Open 'Login' page and verify correct title")
    def test06_login(self):
        """
        Open 'Login' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Login page"):
            self.main_page.open_page('login button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('login title', 'Login Page')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 07: Open 'Long Click' page and click cancel")
    def test07_long_click(self):
        """
        Open 'Long Click' page and click on the cancel button.
        """
        with allure.step("Step 1: Open Long Click page"):
            self.main_page.open_page('long click button')
        with allure.step("Step 2: Click on cancel button"):
            self.main_page.click_on_button("cancel button")

    @allure.title("Test 08: Open 'Time' page and verify correct title")
    def test08_time(self):
        """
        Open 'Time' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Time page"):
            self.main_page.open_page('time button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('time activity title', 'Time Activity')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 09: Open 'Date' page and verify correct title")
    def test09_date(self):
        """
        Open 'Date' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Date page"):
            self.main_page.open_page('date button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('date activity title', 'Date Activity')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 10: Open 'Hybrid' page and verify correct title")
    def test10_hybrid(self):
        """
        Open 'Hybrid' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Hybrid page"):
            self.main_page.open_page('hybrid button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('hybrid activity title', 'Hybrid Activity')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 11: Open 'Pinch' page and verify image appears")
    def test11_pinch(self):
        """
        Open 'Pinch' page and verify Android image appears, then return to main page.
        """
        with allure.step("Step 1: Open Pinch page"):
            self.main_page.open_page('pinch button')
        with allure.step("Step 2: Verify Android Image appears"):
            self.main_page.verify_image('android image')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 12: Open 'Drag and drop' page and verify correct title")
    def test12_drag_and_drop(self):
        """
        Open 'Drag and Drop' page and verify the title, then return to main page.
        """
        with allure.step("Step 1: Open Drag and Drop page"):
            self.main_page.open_page('drag and drop button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('draggable text', 'Draggable Text')
        with allure.step("Step 3: Navigate back to main page"):
            self.main_page.press_on_back()

    @allure.title("Test 13: Test crash button behavior")
    def test13_crash(self):
        """
        Click on the crash button and verify that the app crashes (or handle it gracefully).
        """
        with allure.step("Step 1: Verify app crashed"):
            self.main_page.verify_app_crash('crash button', 'com.code2lead.kwad')
