from appium.webdriver.webdriver import WebDriver

from pages.contact_us_form_page import ContactForm
from pages.enter_some_value_page import EnterSomeValuePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class PageFactory:

    main_page: MainPage
    login_page: LoginPage
    contact_us_page: ContactForm
    enter_some_value_page: EnterSomeValuePage


