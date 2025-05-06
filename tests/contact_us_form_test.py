import allure
import pytest
import utilities.custom_logger as CL
from configuration.config import ConfigReader
from utilities.page_factory import PageFactory


@allure.description("Contact Us Form Page")
@pytest.mark.usefixtures("setup_class")
class TestContactUsPage(PageFactory):
    log = CL.custom_logger()

    @allure.title("Test 01: Open Contact us page")
    def test01_open_contact_us_page(self):
        with allure.step("Step 1: Open Contact us page form page"):
            self.main_page.open_page('contact us button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.main_page.verify_page_title('contact us title', 'Contact Us form')

    @allure.title("Test 02: Fill in form with details")
    def test02_fill_info_form(self):
        name = ConfigReader.read_config('contact_us_page_tests', 'name')
        email = ConfigReader.read_config('contact_us_page_tests', 'email')
        address = ConfigReader.read_config('contact_us_page_tests', 'address')
        phone_number = ConfigReader.read_config('contact_us_page_tests', 'phone_number')
        with allure.step("Step 1: Fill in name in contact info"):
            self.contact_us_page.fill_in_details('enter name field', name)
        with allure.step("Step 2: Fill in email in contact info"):
            self.contact_us_page.fill_in_details('enter email field', email)
        with allure.step("Step 3: Fill in address in contact info"):
            self.contact_us_page.fill_in_details('enter address field', address)
        with allure.step("Step 4: Fill in phone number in contact info"):
            self.contact_us_page.fill_in_details('enter mobile field', phone_number)

    def test03_click_on_submit(self):
        self.contact_us_page.click_on_button('submit button')
