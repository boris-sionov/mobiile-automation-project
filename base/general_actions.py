import os
import time

import utilities.custom_logger as CL
from base.base_page import BasePage


class GeneralActions(BasePage):
    screenshot_directory = '.././screenshots/'
    allure_report_directory = '../reports/allure-reports'

    def __init__(self, driver):
        super().__init__(driver)
        self.log = CL.custom_logger()
        self.time_format = time.strftime("%d-%b-%Y %H:%M:%S")

    def clean_screenshots_folder(self):
        # log = CL.custom_logger()

        if os.path.exists(self.screenshot_directory):
            try:
                for file_name in os.listdir(self.screenshot_directory):
                    file_path = os.path.join(self.screenshot_directory, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                self.log.info("Cleaned old screenshots from the folder.")
            except Exception as e:
                self.log.error(f"Error while cleaning screenshots folder: {str(e)}")
        else:
            self.log.error(f"Screenshot folder does not exist: {self.screenshot_directory}")

    def clean_allure_folder(self):
        # log = CL.custom_logger()

        if os.path.exists(self.screenshot_directory):
            try:
                for file_name in os.listdir(self.allure_report_directory):
                    file_path = os.path.join(self.allure_report_directory, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                self.log.info("Cleaned old Allure-reports from the folder.")
            except Exception as e:
                self.log.error(f"Error while cleaning Allure-reports folder: {str(e)}")
        else:
            self.log.error(f"Allure-reports folder does not exist: {self.screenshot_directory}")

        # Take a screenshot
    def screenshot(self, screenshot_name):

        # Create the screenshot name with timestamp
        file_name = f"{screenshot_name}_{self.time_format}.png"
        screenshot_path = self.screenshot_directory + file_name

        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot saved to Path: " + screenshot_path)
            return file_name  # Return the file name
        except Exception as e:
            self.log.error(f"Unable to save screenshot to the Path: {screenshot_path}. Error: {str(e)}")
