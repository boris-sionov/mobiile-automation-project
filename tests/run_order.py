import subprocess

# Define your tests in the order you want
tests_in_order = [
    "tests/open_all_pages_test.py",
    "tests/contact_us_form_test.py",
    "tests/login_test.py",
]

# Run them one by one
for test_file in tests_in_order:
    subprocess.run(["pytest", test_file])
