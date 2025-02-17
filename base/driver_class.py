import sys
import urllib3
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.common import WebDriverException
import utilities.custom_logger as CL
from base.general_actions import GeneralActions


class Driver:

    @staticmethod
    def get_driver_method():
        log = CL.custom_logger()
        app_package = 'com.code2lead.kwad'
        appium_server = 'http://127.0.0.1:4723'
        desired_capabilities = {'platformName': 'Android',
                                'platformVersion': '15',
                                'automationName': 'UiAutomator2',
                                'deviceName': 'emulator-5554',
                                'app': '/Users/borissionov/Downloads/Android_Demo_App.apk',
                                'appPackage': app_package,
                                'appActivity': 'com.code2lead.kwad.MainActivity'}

        try:
            capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
            driver = webdriver.Remote(appium_server, options=capabilities_options)
            # log.info("Driver was started successfully")
            # general_actions = GeneralActions(driver)  # Pass driver after initializing
            # general_actions.clean_screenshots_folder()
            # general_actions.clean_allure_folder()

            return driver

        except urllib3.exceptions.MaxRetryError:  # Handling NewConnectionError specifically
            log.critical("Connection error: Unable to connect to Appium server at http://127.0.0.1:4723, Check if "
                         "appium server is running.")
            sys.exit(1)  # Exit script on failure to connect
        except WebDriverException:  # Handle other WebDriver exceptions
            log.critical("Appium Error: Unable to find any device, Check if there is a devices connected")
            sys.exit(1)  # Exit script on failure
        except Exception as e:  # Catch any other unexpected errors
            log.critical(f"Unexpected error: {str(e)}")
            sys.exit(1)  # Exit script on any unexpected error




