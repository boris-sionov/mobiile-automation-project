import subprocess
import logging
import os

# Optional: ensure the allure report directory exists or is cleaned
allure_dir = "reports/allure-reports"
os.makedirs(allure_dir, exist_ok=True)

tests_in_order = [
    "tests/open_all_pages_test.py",
    "tests/enter_some_value_test.py",
    "tests/contact_us_form_test.py",
    "tests/scroll_view_test.py"
]

# Run all tests in one pytest call
subprocess.run([
    "pytest",
    *tests_in_order,
    "-s", "-v",
    f"--alluredir={allure_dir}",
    "--capture=no"
])
