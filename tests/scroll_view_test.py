"""Test module for Scroll View screen functionalities using pytest and Allure."""
import random
import time

import allure
import pytest
from utilities.page_factory import PageFactory


@allure.description("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_class")
class TestScrollView(PageFactory):
    """Test suite for verifying Scroll View interactions."""

    @allure.title("Test 01: Open 'Scroll View' page and verify correct title")
    def test01_scroll_view(self):
        """Open Scroll View page and validate its title."""
        with allure.step("Step 1: Open Scroll View page"):
            self.main_page.open_page('scroll view button')

        with allure.step("Step 2: Verify the page title is correct"):
            self.scroll_view_page.verify_page_title(
                'scroll view title',
                'ScrollView')

    @allure.title("Test 02: Press on Button 1")
    def test02_tap_on_button1(self):
        """Click on Button 1 in Scroll View page."""
        with allure.step("Step 1: Open Scroll View page"):
            self.scroll_view_page.click_on_button('button 1')

    @allure.title("Test 03: Verify popup appears with correct title")
    def test03_verify_correct_popup_title(self):
        """Verify the popup alert title and message are correct after clicking Button 1."""
        with allure.step("Step 1: Verify correct title text appears"):
            self.scroll_view_page.verify_popup_text(
                'alert popup title',
                'Alert popup')
        with allure.step("Step 2: Verify correct message text appears"):
            self.scroll_view_page.verify_popup_text(
                'alert message text',
                'Are you sure? what to close')

    @allure.title("Test 04: Press on No button")
    def test04_click_on_no_button(self):
        """Click on No button from popup and verify it closes."""
        with allure.step("Step 1: Click on No button"):
            self.scroll_view_page.click_on_button('no button')
        with allure.step("Step 2: Verify popup closed"):
            self.scroll_view_page.verify_popup_not_appear('alert popup title')

    @allure.title("Test 05: Press on Button 16")
    def test05_click_on_button16(self):
        """Click on Button 16 (with scroll), verify popup content, and close it."""
        with allure.step("Step 1: Click on button 16 - with scrolling the screen"):
            self.scroll_view_page.click_on_button('button 16')
        with allure.step("Step 2: Verify popup alert title"):
            self.scroll_view_page.verify_popup_text(
                'alert popup title',
                'Alert popup')
        with allure.step("Step 3: Verify popup message"):
            self.scroll_view_page.verify_popup_text(
                'alert popup title',
                'Alert popup')
        with allure.step("Step 4: Click on No button"):
            self.scroll_view_page.click_on_button('no button')

    @allure.title("Test 06:Press on Random button")
    def test06_click_on_rando_button(self):
        """Click on Random Button in Scroll View page."""
        random_number = random.randint(1,16)
        with allure.step("Step 1: Press on generated random button"):
            self.scroll_view_page.click_on_button(f"button {random_number}")
        with allure.step("Step 2: Verify popup alert title"):
            self.scroll_view_page.verify_popup_text(
                'alert popup title',
                'Alert popup')

    @allure.title("Test 07:Press on Yes button")
    def test07_click_on_rando_button(self):
        """Click on Yes in Alert popup and verify navigated back to main page."""
        with allure.step("Step 1: Click on Yes button"):
            self.scroll_view_page.click_on_button('Yes button')
        with allure.step("Step 2: Verify main page appearance"):
            self.main_page.verify_page_title(
                'appium demo title',
                'Appium Demo')
