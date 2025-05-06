import allure
import pytest

from configuration.config import ConfigReader
from utilities.page_factory import PageFactory


@allure.description("All Pages Test - Open all pages and verify correct page is opened")
@pytest.mark.usefixtures("setup_class")
class TestEnterSomeValue(PageFactory):

    @allure.title("Test 01: Open 'Enter Some Value' page and verify correct title")
    def test01_open_enter_some_value_page(self):
        with allure.step("Step 1: Open 'Enter Some Value' page"):
            self.main_page.open_page('enter some value button')

        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('enter some value title', 'Enter some Value')

    def test02_validate_preview_text(self):
        self.enter_some_value_page.verify_preview_text('preview text', 'Preview')

    def test03_fill_some_text(self):
        with allure.step("Step 1: Enter some text"):
            text_test = ConfigReader.read_config('enter_some_value_page_tests','text_for_test')
            self.enter_some_value_page.fill_text('enter some value field', text_test)

    def test04_click_on_submit(self):
        with allure.step("Step 1: Click on Submit button:"):
            self.enter_some_value_page.click_on_button('submit button')

    def test05_verify_preview_text_after_submit(self):
        text_test = ConfigReader.read_config('enter_some_value_page_tests', 'text_for_test')
        self.enter_some_value_page.verify_preview_text('preview text', text_test)
