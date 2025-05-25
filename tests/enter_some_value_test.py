"""
Test suite for verifying the 'Enter Some Value' page functionality.
"""

import allure
import pytest

from utilities.config import ConfigReader
from utilities.page_factory import PageFactory


@allure.epic("Enter Some Value Page Tests")
@allure.feature("Functional Testing")
@allure.suite("Main Page Suite")
@allure.title("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_class")
class TestEnterSomeValue(PageFactory):
    """
    Test class for 'Enter Some Value' page.
    Inherits from PageFactory to access page objects.
    Uses setup_class fixture to initialize driver and pages.
    """

    @allure.title("Test 01: Open 'Enter Some Value' page and verify correct title")
    def test01_open_enter_some_value_page(self):
        with allure.step("Step 1: Open 'Enter Some Value' page"):
            self.main_page.open_page('enter some value button')

        with allure.step("Step 2: Verify the page title is correct"):
            self.enter_some_value_page.verify_page_title(
                'enter some value title',
                'Enter some Value')

    @allure.title("Test 02: Validate default preview text")
    def test02_validate_preview_text(self):
        self.enter_some_value_page.verify_preview_text(
            'preview text',
            'Preview')

    @allure.title("Test 03: Fill in some text from config file")
    def test03_fill_some_text(self):
        with allure.step("Step 1: Enter some text"):
            text_test = ConfigReader.read_config(
                'enter_some_value_page_tests',
                'text_for_test')
            self.enter_some_value_page.fill_text(
                'enter some value field', text_test)

    @allure.title("Test 04: Click on Submit button")
    def test04_click_on_submit(self):
        with allure.step("Step 1: Click on Submit button:"):
            self.enter_some_value_page.click_on_button('submit button')

    @allure.title("Test 05: Verify preview text is updated after submission")
    def test05_verify_preview_text_after_submit(self):
        text_test = ConfigReader.read_config('enter_some_value_page_tests', 'text_for_test')
        self.enter_some_value_page.verify_preview_text('preview text', text_test)
