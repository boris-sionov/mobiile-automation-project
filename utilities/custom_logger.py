import logging
import os
import sys
import time

import allure
import shutil
import colorlog

# Define log file location
LOG_FILE = "../reports/logs/log.log"
ALLURE_REPORTS_DIR = "../reports/allure-reports"

# Define date format
date_format = '%d/%b/%Y %H:%M:%S %A'


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
    file_handler = logging.FileHandler(LOG_FILE, mode="w")  # Overwrites old logs
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
    with open(LOG_FILE, "a") as f:
        f.write(f"{text}\n")


def attach_logs_to_allure():
    """Attach the log file to Allure reports"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                allure.attach(f.read(), name="Test Logs", attachment_type=allure.attachment_type.TEXT)
        else:
            logging.warning(f"Log file not found: {LOG_FILE}")
    except Exception as e:
        logging.error(f"Failed to attach log file: {e}")


def clear_allure_reports():
    """Clear Allure reports before each test run"""
    if os.path.exists(ALLURE_REPORTS_DIR):
        for filename in os.listdir(ALLURE_REPORTS_DIR):
            file_path = os.path.join(ALLURE_REPORTS_DIR, filename)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove directory
                else:
                    os.remove(file_path)  # Remove file
            except Exception as e:
                logging.error(f"Failed to delete {file_path}: {e}")
        logging.info(f"Allure reports folder has been cleared.")
    else:
        logging.info(f"Allure reports folder '{ALLURE_REPORTS_DIR}' does not exist.")
