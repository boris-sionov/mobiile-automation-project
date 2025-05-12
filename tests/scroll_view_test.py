import allure
import pytest
from utilities.page_factory import PageFactory


@allure.description("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_class")
class TestScrollView(PageFactory):
    @allure.title("Test 01: Open 'Scroll View' page and verify correct title")
    def test01_scroll_view(self):
        with allure.step("Step 1: Open Scroll View page"):
            self.main_page.open_page('scroll view button')

        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('scroll view title', 'ScrollView')

    @allure.title("Test 02: Press on Button")
    def test02_tap_on_button1(self):
        with allure.step("Step 1: Open Scroll View page"):
            self.scroll_view_page.click_on_button('button 1')

    def test03_verify_correct_popup_title(self):
        with allure.step("Step 1: Verify correct title text appears"):
            self.scroll_view_page.verify_popup_text('alert popup title', 'Alert popup')
        with allure.step("Step 2: Verify correct message text appears"):
            self.scroll_view_page.verify_popup_text('alert message text', 'Are you sure? what to close')

    def test04_click_on_no_button(self):
        with allure.step("Step 1: Click on No button"):
            self.scroll_view_page.click_on_button('no button')
        with allure.step("Step 2: Verify popup closed"):
            self.scroll_view_page.verify_popup_not_appear('scroll view title')

    def test05_click_on_button16(self):
        with allure.step("Step 1: Click on button 16 - with scrolling the screen"):
            self.scroll_view_page.click_on_button('button 16')
        with allure.step("Step 2: Verify popup alert title"):
            self.scroll_view_page.verify_popup_text('alert popup title', 'Alert popup')
        with allure.step("Step 3: Verify popup message"):
            self.scroll_view_page.verify_popup_text('alert popup title', 'Alert popup')
        with allure.step("Step 4: Click on No button"):
            self.scroll_view_page.click_on_button('no button')




