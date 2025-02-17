# import unittest
# import allure
# import pytest
# import utilities.custom_logger as CL
#
#
# @allure.description("This my first test")
# @pytest.mark.usefixtures("before_class")
# class TestContactUsPage(unittest.TestCase):
#     log = CL.custom_logger()
#     mainPage = None
#     contactUsPage = None
#     loginPage = None
#
#     @allure.title("Test 01: Open Contact us page")
#     @pytest.mark.run(order=1)
#     def test_open_contact_us_page(self):
#         CL.allure_step_logs("Step 1: Open contact us page")
#         self.log.info("Starting test open contact page")
#         self.contactUsPage.open_contact_us()
#         # CL.allure_step_logs("Step 2: Verify page is opened")
#         # self.contactUsPage.verify_contact_page()
#         # self.log.info("Test is done")
#
#     @allure.title("Test 02: Fill in form with details")
#     @pytest.mark.run(order=2)
#     def test_fill_info_form(self):
#         CL.allure_step_logs("Step 1: Fill information in the form")
#         self.log.info("Starting test")
#         self.contactUsPage.fill_in_details('Boris Sionov', 'boris@mail.com', 'My Street address 8, Israel', '050303000')
#         CL.allure_step_logs("Step 2: Press on Submit button")
#         self.contactUsPage.press_on_submit()
#         self.log.info("Test is done")
