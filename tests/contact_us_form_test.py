"""
Test suite for verifying the 'Contact Us' form page functionality.
Includes:
- Opening the Contact Us form
- Filling in user details from the config
- Submitting the form
"""

import allure
import pytest
import utilities.custom_logger as CL
from utilities.config import ConfigReader
from utilities.page_factory import PageFactory


@allure.description("Contact Us Form Page")
@pytest.mark.usefixtures("setup_class")
class TestContactUsPage(PageFactory):
    """
    Test class for 'Contact Us' page functionality.
    Uses setup_class fixture to initialize driver and page objects.
    Inherits from PageFactory to access all page object instances.
    """
    log = CL.custom_logger()

    @allure.title("Test 01: Open Contact us page")
    def test01_open_contact_us_page(self):
        """
        Test to open the Contact Us form page and verify its title.
        Steps:
        - Open Contact Us form
        - Verify the page title
        """
        with allure.step("Step 1: Open Contact us page form page"):
            self.main_page.open_page('contact us button')
        with allure.step("Step 2: Verify the page title is correct"):
            self.contact_us_page.verify_page_title(
                'contact us title',
                'Contact Us form')

    @allure.title("Test 02: Fill in form with details")
    def test02_fill_info_form(self):
        """
        Test to fill in the Contact Us form fields with data from config.
        Steps:
        - Fill name
        - Fill email
        - Fill address
        - Fill phone number
        """
        name = ConfigReader.read_config('contact_us_page_tests', 'name')
        email = ConfigReader.read_config('contact_us_page_tests', 'email')
        address = ConfigReader.read_config('contact_us_page_tests', 'address')
        phone_number = ConfigReader.read_config('contact_us_page_tests', 'phone_number')
        with allure.step("Step 1: Fill in name in contact info"):
            self.contact_us_page.fill_text(
                'enter name field', name)
        with allure.step("Step 2: Fill in email in contact info"):
            self.contact_us_page.fill_text(
                'enter email field', email)
        with allure.step("Step 3: Fill in address in contact info"):
            self.contact_us_page.fill_text(
                'enter address field', address)
        with allure.step("Step 4: Fill in phone number in contact info"):
            self.contact_us_page.fill_text(
                'enter mobile field', phone_number)

    @allure.title("Test 03: Click on submit button")
    def test03_click_on_submit(self):
        """
        Test to click the submit button on the Contact Us form.
        """
        self.contact_us_page.click_on_button('submit button')
