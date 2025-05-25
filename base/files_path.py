import os

""" 
This module defines the absolute paths used throughout the project for reports, logs, configuration, and APK files.
"""

# Define the root directory of your project
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# File paths
screenshot_directory = os.path.join(root_dir, 'reports', 'screenshots') + "/"  # Path to store screenshot images
allure_report_directory = os.path.join(root_dir, 'reports', 'allure-reports') + "/"  # Path for Allure report output
log_file_path = os.path.join(root_dir, 'reports', 'logs', 'log.log')  # Path to the log file
config_file_path = os.path.join(root_dir, 'configuration', 'config.ini')  # Path to the main config file
apk_file_path = os.path.join(root_dir, 'utilities', 'Android_Demo_App.apk')  # Path to the Android demo APK file
