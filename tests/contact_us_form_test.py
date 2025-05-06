import allure
import pytest
import utilities.custom_logger as CL
from utilities.page_factory import PageFactory


@allure.description("Contact Us Form Page")
@pytest.mark.usefixtures("setup_class")
class TestContactUsPage(PageFactory):
    log = CL.custom_logger()

    @allure.title("Test 01: Open Contact us page")
    def test_open_contact_us_page(self):
        with allure.step("Step 1: Open Contact us page form page"):
            self.main_page.open_page('contact us button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('contact us title', 'Contact Us form')

    @allure.title("Test 02: Fill in form with details")
    def test_fill_info_form(self):
        CL.allure_step_logs("Step 1: Fill information in the form")
        self.contact_us_page.fill_in_details('Boris Sionov', 'boris@mail.com', 'My Street address 8, Israel', '050303000')
        CL.allure_step_logs("Step 2: Press on Submit button")
        self.contact_us_page.press_on_submit()
