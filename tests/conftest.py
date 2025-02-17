import pytest
import time

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utilities.page_factory import PageFactory
from base.driver_class import Driver
import utilities.custom_logger as CL

# Initialize Logger
log = CL.custom_logger()


@pytest.fixture(scope="class")
def setup_class(request):
    log.info("Opening the tested application - Starting Automation tests")

    # Initialize the driver
    driver = Driver().get_driver_method()

    request.cls.driver = driver
    request.cls.main_page = MainPage(request.cls.driver)
    request.cls.login_page = LoginPage(request.cls.driver)




    # page_factory = PageFactory(driver).init_pages()
    # for page_name in dir(page_factory):
    #     if not page_name.startswith('_'):
    #         setattr(request.cls, page_name, getattr(page_factory, page_name))

    yield driver

    # Attach logs to Allure after the test
    CL.attach_logs_to_allure()

    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Killing the application - Tests are done")


@pytest.fixture(scope="function")
def setup_function(request):
    log.info("Opening the tested application - Starting Automation tests")

    # Clear Allure reports before the test run
    CL.clear_allure_reports()

    # Initialize the driver
    driver = Driver().get_driver_method()

    request.cls.driver = driver

    # Initialize PageFactory and assign pages dynamically
    page_factory = PageFactory(driver).init_pages()
    for page_name in dir(page_factory):
        if not page_name.startswith('_'):
            setattr(request.cls, page_name, getattr(page_factory, page_name))

    yield driver

    # Attach logs to Allure after the test
    CL.attach_logs_to_allure()

    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Killing the application - Tests are done")
