import sys
import urllib3
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.common import WebDriverException
import utilities.custom_logger as CL
from base.browser_init import BrowserInit
from utilities.config import ConfigReader

# Initialize Logger
log = CL.custom_logger()


def get_browser(browser_type):
    # lowercase browsers names
    browser_type = browser_type.lower()

    # Handle empty or None values
    if not browser_type:
        log.info("Browser type is empty. Defaulting to chrome.")
        browser_type = "chrome"

    # Handle browsers and init them
    browsers = {
        "chrome": BrowserInit.init_chrome,
        "firefox": BrowserInit.init_firefox,
        "ff": BrowserInit.init_firefox,
        "edge": BrowserInit.init_edge,
        "safari": BrowserInit.init_safari
    }

    # Handle invalid browser name
    if browser_type not in browsers:
        log.info(f"Invalid browser type: '{browser_type}'. Defaulting to chrome.")
        browser_type = "chrome"

    log.info(f"Running Web Automation on {browser_type}")
    return browsers[browser_type]()  # Call the function to initialize the browser


class Driver:

    @staticmethod
    def get_driver_method():
        log.info("Starting driver initialization")
        platform = ConfigReader.read_config('general', 'platform')
        platform = platform.lower()

        if platform == 'web':
            log.info(f"Running automation tests on {platform} platform")
            # Get browser type from config
            browser_type = ConfigReader.read_config('web', 'browser')
            driver = get_browser(browser_type)

            # Navigate to test site
            driver.maximize_window()
            test_site_url = ConfigReader.read_config('web', 'url')
            driver.get(test_site_url)

            return driver

        elif platform == 'android':
            print(f"You choose to run automation on {platform}")
            root_dir = sys.path[0]  # Convert root_dir to a Path object
            relative_app_path = ConfigReader.read_config("capabilities", "app_path")
            appium_server = ConfigReader.read_config("capabilities", "appium_server")

            desired_capabilities = \
                {'platformName': ConfigReader.read_config("capabilities", "platform_name"),
                 'platformVersion': ConfigReader.read_config("capabilities", "platform_version"),
                 'automationName': ConfigReader.read_config("capabilities", "automation_name"),
                 'deviceName': ConfigReader.read_config("capabilities", "device_name"),
                 'app': root_dir + '/' + relative_app_path,
                 'appPackage': ConfigReader.read_config("capabilities", "app_package"),
                 'appActivity': ConfigReader.read_config("capabilities", "app_activity")
                 }

            try:
                capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
                driver = webdriver.Remote(appium_server, options=capabilities_options)
                return driver

            except urllib3.exceptions.MaxRetryError:  # Handling NewConnectionError specifically
                log.critical(f"Connection error: Unable to connect to Appium server at {appium_server}. Ensure Appium "
                             f"is running.")
                sys.exit(1)  # Exit script on failure to connect
            except WebDriverException as e:  # Handle other WebDriver exceptions
                log.critical(f"Appium Error: {str(e)}. Ensure a device is connected and Appium is running.")
                sys.exit(1)  # Exit script on failure
            except Exception as e:  # Catch any other unexpected errors
                log.critical(f"Unexpected error: {str(e)}")
                sys.exit(1)  # Exit script on any unexpected error

        elif platform == 'ios':
            log.info("Running automation on iOS device")

        else:
            log.critical(f"Invalid platform '{platform}'. Please specify 'web' or 'android' in config.")
            sys.exit(1)
