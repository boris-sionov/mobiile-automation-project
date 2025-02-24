import os

# Define the root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define the directories based on the root directory
screenshot_directory = os.path.join(root_dir, 'reports', 'screenshots')
allure_report_directory = os.path.join(root_dir, 'reports', 'allure-reports')
log_file_path = os.path.join(root_dir, 'reports', 'logs', 'log.log')
config_file_path = os.path.join(root_dir, 'configuration', 'config.ini')
apk_file_path = os.path.join(root_dir, 'utilities', 'Android_Demo_App.apk')
