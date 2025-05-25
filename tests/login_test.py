
import allure
import pytest
import utilities.custom_logger as CL
from utilities.page_factory import PageFactory


@allure.description("Login Page Test")
@pytest.mark.usefixtures("setup_class")
class TestLogin(PageFactory):

    @allure.title("Test 01: This test is checking incorrect info filled in the credentials")
    def test01_open_login_page(self):
        self.main_page.open_page('')

    @allure.title("Test 02: This test is checking correct filled in the credentials")
    def test_correct_info(self):
        with allure.step("Step 1: Enter correct info"):
            self.login_page.enter_correct_credentials("admin@gmail.com", "admin123")

    @allure.title("Test 03: This test is checking Enter admin page")
    def test_enter_admin(self):
        with allure.step("Step 1: Verify preview text is changed after pressing on submit button"):
            self.login_page.enter_admin_page("some text to test")




