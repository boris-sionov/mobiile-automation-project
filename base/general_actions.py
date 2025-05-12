import inspect
import os
import time

import utilities.custom_logger as CL
from base.base_page import BasePage
from base.files_path import screenshot_directory
from configuration.config import ConfigReader


class GeneralActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = CL.custom_logger()
        self.time_format = time.strftime(ConfigReader.read_config("date", "files_time_format"))

    def clean_screenshots_folder(self):
        # log = CL.custom_logger()

        if os.path.exists(screenshot_directory):
            try:
                for file_name in os.listdir(screenshot_directory):
                    file_path = os.path.join(screenshot_directory, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                self.log.info("Cleaned old screenshots from the folder.")
            except Exception as e:
                self.log.error(f"Error while cleaning screenshots folder: {str(e)}")
        else:
            self.log.error(f"Screenshot folder does not exist: {screenshot_directory}")

        # Take a screenshot
    def screenshot(self, screenshot_name):

        # Create the screenshot name with timestamp
        file_name = f"{screenshot_name}_{self.time_format}.png"
        screenshot_path = os.path.join(screenshot_directory, file_name)

        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot saved to Path: " + screenshot_path)
            return file_name  # Return the file name
        except Exception as e:
            self.log.error(f"Unable to save screenshot to the Path: {screenshot_path}. Error: {str(e)}")

    def generate_screenshot_name(self, suffix: str) -> str:
        # Get current test method name from the stack
        for frame_record in inspect.stack():
            if frame_record.function.startswith("test"):
                test_name = frame_record.function
                break
        else:
            test_name = "unknown_test"

        # Build file name
        file_name = f"{test_name}_{suffix}.png"
        return file_name

    def switch_to_frame(self, index):
        """
        Wait until the iframe at the given index is available and switch to it.
        :param index: Index of the iframe
        """
        try:
            self.log.info(f"Waiting for iframe at index {index} to be available and switch to it.")
            self.wait_for_frame(index)
            self.log.info(f"Switched to iframe at index {index} successfully.")
        except Exception as e:
            self.log.error(f"Failed to switch to iframe({index}). Error: {str(e)}")
            assert False, f"Failed to switch to iframe({index}). Error: {str(e)}"
