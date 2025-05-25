"""
Pytest configuration file for setting up drivers and page objects.
Includes:
- Session-level setup for Appium server and logging
- Class/function-level setup for independent driver/page objects
- Custom logger and Allure report clearing
"""

import pytest
import os
from appium.webdriver.appium_service import AppiumService

from base.files_path import config_file_path
from utilities.config import ConfigReader
from utilities.page_factory import PageFactory
from base.driver_class import Driver
import utilities.custom_logger as CL
from utilities.custom_logger import clear_allure_reports

# Ensure config file exists
if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"\n[ERROR] Missing required config file at: {config_file_path}\n")

# Logger
log = CL.custom_logger()

# Shared AppiumService
appium_service = AppiumService()

def attach_driver_and_pages(request):
    driver = Driver().get_driver_method()
    request.cls.driver = driver
    for page_name, page_class in PageFactory.__annotations__.items():
        setattr(request.cls, page_name, page_class(driver))
    return driver


@pytest.fixture(scope="session", autouse=True)
def clear_reports_before_tests():
    """Clears Allure reports before tests start."""
    # log.debug("allure")
    clear_allure_reports()


@pytest.fixture(scope="session", autouse=True)
def manage_appium_server():
    """
    Start Appium server if platform is not web.
    Stop it at the end of session.
    """
    platform = ConfigReader.read_config("general", "platform").lower()

    log.info(f"Starting test session, Platform: {platform}")

    if platform != "web":
        if not appium_service.is_running:
            log.info("Starting Appium server...")
            appium_service.start()
            log.info(f"Appium server running: {appium_service.is_running}")
        else:
            log.info("Appium server already running")

    yield
    log.info("Ending test session - initiating teardown")

    if platform != "web" and appium_service.is_running:
        log.info("Stopping Appium server...")
        appium_service.stop()
        log.info("Appium server stopped")
    else:
        log.warning("Appium server was not running or not required")

    log.info("Test session complete")


@pytest.fixture(scope="class")
def setup_class(request):
    """
    Class-level driver and page object setup.
    - Runs once per test class
    - Attaches driver and PageFactory pages to the class
    """
    log.info("Launching application - [Class Scope]")
    driver = attach_driver_and_pages(request)

    yield driver

    log.info("Closing application - [Class Scope]")
    driver.quit()


@pytest.fixture(scope="function")
def setup_function(request):
    """
    Function-level driver and page object setup.
    - New driver before each test
    - Clean teardown after each test
    """
    log.info("Launching application - [Function Scope]")
    driver = attach_driver_and_pages(request)

    yield driver

    log.info("Closing application - [Function Scope]")
    driver.quit()
