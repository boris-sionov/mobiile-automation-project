from appium.webdriver.webdriver import WebDriver

from pages.contact_us_for_page import ContactForm
from pages.login_page import LoginPage
from pages.main_page import MainPage


class PageFactory:

    main_page: MainPage
    login_page: LoginPage
    driver: WebDriver




    #
    #
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.main_page = None
    #     self.contact_us_page = None
    #     self.login_page = None
    #
    # def init_pages(self):
    #     self.contact_us_page = ContactForm(self.driver)
    #     self.main_page = MainPage(self.driver)
    #     self.login_page = LoginPage(self.driver)
    #
    #     # Initialize other pages here
    #     return self  # Return self to allow method chaining
