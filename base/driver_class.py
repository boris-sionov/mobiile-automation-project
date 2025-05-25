import os
import sys
import urllib3
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.common import WebDriverException
import utilities.custom_logger as CL
from base.browser_init import BrowserInit
from pathlib import Path
from utilities.config import ConfigReader

# Initialize Logger
log = CL.custom_logger()

appium_service = AppiumService()


def get_browser(browser_type):
    """
    Initialize and return a WebDriver instance based on the specified browser type.
    Supported browsers: chrome, firefox, ff, edge, safari.
    Defaults to Chrome if browser_type is empty or unrecognized.

    :param browser_type: str - Browser name from config
    :return: WebDriver instance
    """
    browser_type = browser_type.lower()

    if not browser_type:
        log.info("Browser type is empty. Defaulting to chrome.")
        browser_type = "chrome"

    browsers = {
        "chrome": BrowserInit.init_chrome,
        "firefox": BrowserInit.init_firefox,
        "ff": BrowserInit.init_firefox,
        "edge": BrowserInit.init_edge,
        "safari": BrowserInit.init_safari
    }

    if browser_type not in browsers:
        log.warning(f"Invalid browser type: '{browser_type}'. Defaulting to chrome.")
        browser_type = "chrome"

    log.info(f"Running Web Automation on {browser_type}")
    return browsers[browser_type]()  # Call the function to initialize the browser


class Driver:
    """
    Driver class responsible for initializing drivers for Web and Android platforms
    based on configurations provided in the config file.
    """

    @staticmethod
    def get_driver_method():
        """
        Initialize and return the appropriate driver based on the platform type.
        For 'web': launches browser and opens the target URL.
        For 'android': launches Appium session using UiAutomator2.
        For 'ios': logs a warning (placeholder).
        If platform is invalid, exits with a critical error.

        :return: WebDriver instance
        """
        log.info("Starting driver initialization")
        platform = ConfigReader.read_config('general', 'platform')
        platform = platform.lower()
        log.info(f"Running automation tests on {platform} platform")

        if platform == 'web':
            browser_type = ConfigReader.read_config('web', 'browser')
            driver = get_browser(browser_type)

            driver.maximize_window()
            test_site_url = ConfigReader.read_config('web', 'url')
            driver.get(test_site_url)

            return driver

        elif platform == 'android':
            root_dir = sys.path[0]
            relative_app_path = ConfigReader.read_config("capabilities", "app_path")
            full_app_path = str(Path(root_dir) / relative_app_path)

            appium_server = ConfigReader.read_config("capabilities", "appium_server")
            app_package = ConfigReader.read_config("capabilities", "app_package")
            app_activity = ConfigReader.read_config("capabilities", "app_activity")

            desired_capabilities = {
                'platformName': ConfigReader.read_config("capabilities", "platform_name"),
                'platformVersion': ConfigReader.read_config("capabilities", "platform_version"),
                'automationName': ConfigReader.read_config("capabilities", "automation_name"),
                'deviceName': ConfigReader.read_config("capabilities", "device_name"),
                'app': full_app_path,
            }

            if app_package:
                desired_capabilities['appPackage'] = app_package
            if app_activity:
                desired_capabilities['appActivity'] = app_activity

            try:
                capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
                driver = webdriver.Remote(appium_server, options=capabilities_options)
                return driver

            except urllib3.exceptions.MaxRetryError:
                Driver.exit_with_error(
                    f"Connection error: Unable to connect to Appium server at {appium_server}. Ensure Appium is running.")
            except WebDriverException as e:
                Driver.exit_with_error(f"Appium Error: {str(e)}. Ensure a device is connected and Appium is running.")
            except Exception as e:
                Driver.exit_with_error(f"Unexpected error: {str(e)}")

        elif platform == 'ios':
            """
            Placeholder for iOS driver support.
            """
            log.warning("iOS platform support is not yet implemented.")
            pass

        else:
            Driver.exit_with_error(f"Invalid platform '{platform}'. Please specify 'web' or 'android' in config.")

    @staticmethod
    def exit_with_error(message):
        """
        Log a critical error message and terminate the test execution.

        :param message: str - Critical error message to be logged before exit.
        """
        log.critical(message)
        sys.exit(1)
