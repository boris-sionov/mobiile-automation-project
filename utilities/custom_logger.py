import logging
import os
import sys

import allure
import shutil
import colorlog
from base.files_path import log_file_path, allure_report_directory
from configuration.config import ConfigReader

# Define date format
date_format = ConfigReader.read_config("date", "logs_time_format")


def custom_logger():
    logger = logging.getLogger("App_Run_Test")
    logger.setLevel(logging.DEBUG)

    # Remove existing handlers to prevent duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console Handler - logs that appear on console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - [%(levelname)s] : %(message)s",
        datefmt=date_format,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )
    console_handler.setFormatter(console_formatter)

    # File Handler (For Allure Logs) - logs that appear in allure results
    file_handler = logging.FileHandler(log_file_path, mode="w")  # Overwrites old logs
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] : %(message)s",
        datefmt=date_format
    )
    file_handler.setFormatter(file_formatter)

    # Add Handlers
    logger.addHandler(console_handler)  # Console Output
    logger.addHandler(file_handler)  # Log File Output

    return logger


def allure_step_logs(text):
    """Logs messages to Allure reports"""
    with allure.step(text):  # Ensures timestamps in Allure logs
        pass

    # Append message to log file
    with open(log_file_path, "a") as f:
        f.write(f"{text}\n")


# def attach_logs_to_allure():
#     """Attach the log file to Allure reports"""
#     try:
#         if os.path.exists(log_file_path):
#             with open(log_file_path, "r") as f:
#                 allure.attach(f.read(), name="Test Logs", attachment_type=allure.attachment_type.TEXT)
#         else:
#             logging.warning(f"Log file not found: {log_file_path}")
#     except Exception as e:
#         logging.error(f"Failed to attach log file: {e}")


def clear_allure_reports():
    """Clear Allure reports before test run"""
    if os.path.exists(allure_report_directory):
        for filename in os.listdir(allure_report_directory):
            file_path = os.path.join(allure_report_directory, filename)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove directory
                else:
                    os.remove(file_path)  # Remove file
            except Exception as e:
                logging.error(f"Failed to delete {file_path}: {e}")
        logging.info(f"Allure reports folder has been cleared.")
    else:
        logging.info(f"Allure reports folder '{allure_report_directory}' does not exist.")
