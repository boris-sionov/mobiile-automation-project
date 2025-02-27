import configparser
import os
import sys

# Define root_dir
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define common directories
screenshot_directory = os.path.join(root_dir, 'reports', 'screenshots')
allure_report_directory = os.path.join(root_dir, 'reports', 'allure-reports')
log_file = os.path.join(root_dir, 'reports', 'logs', 'log.log')


class ConfigReader:

    @staticmethod
    def read_config(section, key):

        config = configparser.ConfigParser()
        config.read(root_dir + '/configuration/config.ini')

        # Check that the Section & key exists
        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
