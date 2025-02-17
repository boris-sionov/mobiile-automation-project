import time
import unittest

import allure
import pytest
import utilities.custom_logger as CL
from utilities.page_factory import PageFactory


@allure.description("Login Page Test")
@pytest.mark.usefixtures("setup_class")
class TestLogin(PageFactory):

    @allure.title("Test 01: This test is checking incorrect info filled in the credentials")
    @pytest.mark.run(order=1)
    def test_incorrect_info(self):
        CL.allure_step_logs("Step 1: Open Login page")
        self.main_page.open_login_page('Login Page')
        CL.allure_step_logs("Step 2: Enter incorrect email and password")
        self.login_page.enter_incorrect_credentials("mail@gmail.com", "adb123", "Wrong Credentials")

    @allure.title("Test 02: This test is checking correct filled in the credentials")
    @pytest.mark.run(order=2)
    def test_correct_info(self):
        CL.allure_step_logs("Step 1: Enter correct info")
        self.login_page.enter_correct_credentials("admin@gmail.com", "admin123")

    @allure.title("Test 03: This test is checking Enter admin page")
    @pytest.mark.run(order=3)
    def test_enter_admin(self):
        CL.allure_step_logs("Step 1: Verify preview text is changed after pressing on submit button")
        self.login_page.enter_admin_page("some text to test")




