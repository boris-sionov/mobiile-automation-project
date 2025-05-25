import inspect
import os
import time

import utilities.custom_logger as CL
from base.base_page import BasePage
from base.files_path import screenshot_directory
from utilities.config import ConfigReader


class GeneralActions(BasePage):
    """Class for general reusable actions like screenshot handling and frame switching."""

    def __init__(self, driver):
        """Initialize GeneralActions with driver, logger, and time format."""
        super().__init__(driver)
        self.log = CL.custom_logger()
        self.time_format = time.strftime(ConfigReader.read_config("date", "files_time_format"))

    def clean_screenshots_folder(self):
        """Delete all files in the screenshot directory to ensure it's clean before test run."""
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

    def screenshot(self, screenshot_name):
        """Take a screenshot with a timestamped name and save it to the screenshot folder.

        Args:
            screenshot_name (str): The base name of the screenshot file.

        Returns:
            str: The generated file name (with timestamp).
        """
        file_name = f"{screenshot_name}_{self.time_format}.png"
        screenshot_path = os.path.join(screenshot_directory, file_name)

        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot saved to Path: " + screenshot_path)
            return file_name
        except Exception as e:
            self.log.error(f"Unable to save screenshot to the Path: {screenshot_path}. Error: {str(e)}")

    def generate_screenshot_name(self, suffix: str) -> str:
        """Generate a screenshot name using the current test function name and a custom suffix.

        Args:
            suffix (str): Custom suffix to append to the screenshot name.

        Returns:
            str: Generated screenshot file name.
        """
        for frame_record in inspect.stack():
            if frame_record.function.startswith("test"):
                test_name = frame_record.function
                break
        else:
            test_name = "unknown_test"

        file_name = f"{test_name}_{suffix}.png"
        return file_name

    def switch_to_frame(self, index):
        """Wait for an iframe by index and switch to it.

        Args:
            index (int): Index of the iframe to switch to.

        Raises:
            AssertionError: If switching to the iframe fails.
        """
        try:
            self.log.info(f"Waiting for iframe at index {index} to be available and switch to it.")
            self.wait_for_frame(index)
            self.log.info(f"Switched to iframe at index {index} successfully.")
        except Exception as e:
            self.log.error(f"Failed to switch to iframe({index}). Error: {str(e)}")
            assert False, f"Failed to switch to iframe({index}). Error: {str(e)}"
