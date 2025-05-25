import configparser
import os
import sys
import allure

# Define root_dir
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define common directories
screenshot_directory = os.path.join(root_dir, 'reports', 'screenshots')
allure_report_directory = os.path.join(root_dir, 'reports', 'allure-reports')
log_file = os.path.join(root_dir, 'reports', 'logs', 'log.log')


class ConfigReader:
    """
    Utility class to read values from config.ini file.
    """

    @staticmethod
    @allure.step("Reading config value from section '{section}', key '{key}'")
    def read_config(section, key):
        """
        Reads a string value from the configuration file.

        :param section: The section in config.ini
        :param key: The key within the section
        :return: String value from the config
        :raises KeyError: If section or key does not exist
        """
        config = configparser.ConfigParser()
        config.read(root_dir + '/configuration/config.ini')

        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")

    @staticmethod
    @allure.step("Reading boolean config value from section '{section}', key '{key}'")
    def read_config_bool(section, key):
        """
        Reads a boolean value from the configuration file.

        :param section: The section in config.ini
        :param key: The key within the section
        :return: Boolean value from the config
        :raises KeyError: If section or key does not exist
        """
        config = configparser.ConfigParser()
        config.read(root_dir + '/configuration/config.ini')

        if config.has_section(section) and config.has_option(section, key):
            return config.getboolean(section, key)
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
