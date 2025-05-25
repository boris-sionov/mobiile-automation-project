"""Test module for Tab Activity screen functionalities using pytest and Allure."""

import allure
import pytest
from utilities.page_factory import PageFactory


@allure.description("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_class")
class TestTabActivity(PageFactory):
    """Test suite for verifying Tab Activity interactions."""

    @allure.title("Test 01: Open 'Tab Activity' page and verify correct title")
    def test01_scroll_view(self):
        """Open Tab Activity page and validate its title."""
        with allure.step("Step 1: Open Tab Activity page"):
            self.main_page.open_page('Tab Activity Button')

        with allure.step("Step 2: Verify the page title is correct"):
            self.tab_activity_page.verify_page_title(
                'tab vieW title',
                'Tab View')

