import os
import sys
from pathlib import Path

import urllib3
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.common import WebDriverException
import utilities.custom_logger as CL
from utilities.config import ConfigReader


class Driver:

    @staticmethod
    def get_driver_method():
        log = CL.custom_logger()
        root_dir = sys.path[0]  # Convert root_dir to a Path object
        relative_app_path = ConfigReader.read_config("capabilities", "app_path")

        # Read all required capabilities from the config file
        platform_name = ConfigReader.read_config("capabilities", "platform_name")
        platform_version = ConfigReader.read_config("capabilities", "platform_version")
        automation_name = ConfigReader.read_config("capabilities", "automation_name")
        device_name = ConfigReader.read_config("capabilities", "device_name")
        app_path = root_dir + '/' + relative_app_path
        app_package = ConfigReader.read_config("capabilities", "app_package")
        app_activity = ConfigReader.read_config("capabilities", "app_activity")
        appium_server = ConfigReader.read_config("capabilities", "appium_server")
        desired_capabilities = \
            {'platformName': platform_name,
             'platformVersion': platform_version,
             'automationName': automation_name,
             'deviceName': device_name,
             'app': app_path,
             'appPackage': app_package,
             'appActivity': app_activity
             }

        try:
            capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
            driver = webdriver.Remote(appium_server, options=capabilities_options)

            return driver

        except urllib3.exceptions.MaxRetryError:  # Handling NewConnectionError specifically
            log.debug("App Path:", app_path)
            log.critical("Connection error: Unable to connect to Appium server at http://127.0.0.1:4723, Check if "
                         "appium server is running.")
            sys.exit(1)  # Exit script on failure to connect
        except WebDriverException:  # Handle other WebDriver exceptions
            # print("Current Working Directory:", os.getcwd())
            log.critical(f"Appium Error: Unable to find any device, Check if there is a devices connected: {app_path}")
            sys.exit(1)  # Exit script on failure
        except Exception as e:  # Catch any other unexpected errors
            log.critical(f"Unexpected error: {str(e)}")
            sys.exit(1)  # Exit script on any unexpected error




