import pytest
import time

from utilities.page_factory import PageFactory
from base.driver_class import Driver
import utilities.custom_logger as CL

# Initialize Logger
log = CL.custom_logger()


@pytest.fixture(scope="class")
def setup_class(request):
    log.info("Opening the tested application - Starting Automation tests")

    # Clear Allure reports before the test run
    CL.clear_allure_reports()

    # Initialize the driver
    driver = Driver().get_driver_method()

    request.cls.driver = driver

    # Dynamically create all PageFactory pages and assign to request.cls
    for page_name, page_class in PageFactory.__annotations__.items():
        page_instance = page_class(request.cls.driver)
        setattr(request.cls, page_name, page_instance)

    yield driver

    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Killing the application - Tests are done")


@pytest.fixture(scope="function")
def setup_function(request):
    log.info("Opening the tested application")

    # Clear Allure reports before the test run
    CL.clear_allure_reports()

    # Initialize the driver
    driver = Driver().get_driver_method()

    request.cls.driver = driver

    # Dynamically create all PageFactory pages and assign to request.cls
    for page_name, page_class in PageFactory.__annotations__.items():
        page_instance = page_class(request.cls.driver)
        setattr(request.cls, page_name, page_instance)

    yield driver

    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Killing the application - Tests are done")
