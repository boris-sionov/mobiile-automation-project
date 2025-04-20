import time
import imaplib
import email
import re

from email.utils import parsedate_to_datetime

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
from base.general_actions import GeneralActions


class UIActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.actions = ActionChains(driver)
        self.otp_code = None

    """ UI actions, like tap or swipe etc..."""

    # Press on button or element
    def press(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            element.click()
            with allure.step(f"Clicked element with locator: '{locator}'"):
                self.log.info(f"Clicked element with locator: '{locator}'")
        except Exception as e:
            with allure.step(f"Error while getting element: {locator}. Exception: {e}"):
                self.log.error(f"Error while getting element: {locator}. Exception: {e}")
            # self.general_actions.screenshot(locator)
            assert False

    def press_with_scroll(self, locator, max_attempts=5):
        attempts = 0
        while attempts < max_attempts:

            try:
                element = self.driver.find_element(*locator)
                boolean_value = element.get_attribute('long-clickable') == 'true'
                if element.is_displayed():
                    with allure.step(f"Element {locator} found on attempt without scrolling. Clicking on it."):
                        self.log.info(f"Element {locator} found on attempt without scrolling. Clicking on it.")
                    if boolean_value:
                        self.long_press(locator)
                        return  # Exit function after clicking the element
                    else:
                        element.click()
                        with allure.step(f"Clicked element with locator: {locator}"):
                            self.log.info(f"Clicked element with locator: {locator}")
                        return  # Exit function after clicking the element

            except NoSuchElementException:
                with allure.step(f"Element {locator} not found on attempt {attempts + 1}. Trying to scroll."):
                    self.log.warning(f"Element {locator} not found on attempt {attempts + 1}. Trying to scroll.")

            # Perform scrolling if element is not found
            self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,
                'top': 800,
                'width': 400,
                'height': 800,
                'direction': 'down',
                'percent': 1.0
            })

            attempts += 1

        # If element is not found after max_attempts, raise an exception
        raise Exception(f"Element {locator} not found after {max_attempts} attempts.")

    def long_press(self, locator):
        # Get element button coordination
        duration = 500
        element = self.wait_for_clickable(locator)
        x = element.location['x']
        y = element.location['y']
        width = element.size['width']
        height = element.size['height']
        self.driver.execute_script("mobile: longClickGesture", {
            'x': x + width / 2,  # Center X coordinate
            'y': y + height / 2,  # Center Y coordinate
            'duration': duration,  # Click duration in milliseconds.

        })

        with allure.step(f"Locator {locator} pressed with long click press duration is: {duration}."):
            self.log.info(f"Locator {locator} pressed with long click press duration is: {duration}.")

    # Perform a scroll gesture on the screen.
    def scroll_screen(self):

        try:
            # Execute the scroll gesture via Appium's mobile command
            self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,  # Start position (50% of screen width)
                'top': 800,  # Start position (80% of screen height)
                'width': 400,  # Width of the screen (50%)
                'height': 800,  # Height to scroll (20%)
                'direction': 'up',  # Direction of the scroll (up or down)
                'percent': 0.8  # Distance to scroll (80% of the defined height)
            })
            self.log.info("Performed scroll gesture")
        except Exception as e:
            with allure.step(f"Error performing scroll gesture. Exception: {e}"):
                self.log.error(f"Error performing scroll gesture. Exception: {e}")
                self.general_actions.screenshot("scroll_gesture_error")
            assert False

    # Method to send text to an element
    def fill_in_text(self, locator, text):
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            element.send_keys(text)
            with allure.step(f"Send text element with locator: '{locator} ' and text send is: {text}"):
                self.log.info(f"Send text element with locator: '{locator}' and text send is: {text}")
        except Exception as e:
            with allure.step(f"Unable sent text on element: {locator}, Exception: {e}"):
                self.log.error(f"Unable sent text on element: {locator}, Exception: {e}")
                self.general_actions.screenshot(locator)
            assert False

    def clear_text(self, locator):
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            with allure.step(f"Locator '{locator}' text is cleared"):
                self.log.info(f"Locator '{locator}' text is cleared")
        except Exception as e:
            with allure.step(f"Unable sent clear text on element: {locator}, Exception: {e}"):
                self.log.error(f"Unable sent clear text on element: {locator}, Exception: {e}")
                self.general_actions.screenshot(locator)
            assert False

    def press_with_action_chain(self, locator):
        element = self.wait_for_visible(locator)
        self.actions.move_to_element(element).click().perform()
        time.sleep(5)

    def fill_in_text_with_action_chain(self, text):
        # clear text using action chain
        self.actions.key_down(Keys.COMMAND).send_keys("a").perform()  # Press and hold command + Press on a
        self.actions.key_up(Keys.COMMAND)  # release  command button
        self.actions.send_keys(Keys.BACKSPACE).perform()  # click on backspace
        self.actions.send_keys(text).perform()
        self.log.info(f"Sent {text} using action chain")

    def select_from_options(self, locator, value):
        element = self.wait_for_visible(locator)
        drop_down = Select(element)
        drop_down.select_by_value(value)
        self.log.info(f"Select from dropdown list {value} in locator : {locator}")

    def retrieve_otp_code(self, timeout=60, poll_interval=5):
        # GMX IMAP Settings
        start_time = time.time()
        imap_server = "imap.gmx.com"
        email_address = "boris.freetv@gmx.com"  # Replace with your GMX email
        password = "Israel23-02"  # Replace with your GMX password

        # Start timing to check how long we've been waiting for the OTP

        self.log.info("Connecting to GMX IMAP server...")

        try:
            # Connect to GMX IMAP server using secure SSL
            mail = imaplib.IMAP4_SSL(imap_server)
            mail.login(email_address, password)  # Login to the mail server
            mail.select("inbox")  # Select the inbox folder to check for new emails
            self.log.info("Connected to GMX email account and inbox selected.")
        except Exception as e:
            # Handle connection or login failures
            self.log.error(f"Failed to connect/login: {e}")
            assert False, f"Failed to connect/login to GMX IMAP server: {e}"  # Assert failure

        self.otp_code = None  # Initialize OTP variable

        # Loop to check the inbox for emails within the timeout duration
        while time.time() - start_time < timeout:
            try:
                # Search for all unread emails in the inbox
                status, messages = mail.search(None, "(UNSEEN)")  # Only unread emails
                email_ids = messages[0].split()

                if not email_ids:
                    # If no unread emails found, retry after waiting for the poll_interval duration
                    self.log.info("No new emails yet. Retrying...")
                    time.sleep(poll_interval)
                    continue

                # Process the latest unread email
                latest_email_id = email_ids[-1]  # Get the latest unread email ID
                status, msg_data = mail.fetch(latest_email_id, "(RFC822)")  # Fetch the email data

                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])  # Parse the email message

                        # Get the 'Date' header and convert it to a datetime object
                        email_date = msg.get("Date")
                        email_datetime = parsedate_to_datetime(email_date)

                        # Only process emails received after the test started
                        if email_datetime.timestamp() < start_time:
                            continue  # Skip this email if it was received before the test started

                        body = ""
                        # If the email has multiple parts, extract the text/plain part
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":  # Get plain text part
                                    body = part.get_payload(decode=True).decode()
                                    break
                        else:
                            body = msg.get_payload(decode=True).decode()  # For non-multipart emails

                        # Use regex to find the OTP in the email body
                        otp_match = re.search(r"קוד האימות שלך.*?([\d]+)", body)
                        if otp_match:
                            # If OTP found, extract and log it
                            self.otp_code = otp_match.group(1)
                            self.log.info(f"OTP successfully retrieved: {self.otp_code}")

                            # After extracting OTP, delete the email
                            mail.store(latest_email_id, '+FLAGS', '\\Deleted')  # Mark the email for deletion
                            mail.expunge()  # Permanently remove the email
                            self.log.info("OTP email deleted from inbox.")
                            break  # Exit the loop after processing the OTP
            except Exception as e:
                # Log any errors that occur while fetching or processing emails
                self.log.error(f"Error while reading email: {e}")

            # If OTP is found, break the loop
            if self.otp_code:
                break
            else:
                # Wait for the next poll interval before checking again
                time.sleep(poll_interval)

        # Logout and close the connection to the mail server
        mail.logout()

        # If OTP is not found, log the error and terminate the script
        if not self.otp_code:
            self.log.error("OTP email not received within timeout.")
            assert False, "OTP email not received within timeout."  # Assert failure if OTP is not received

        # Return the OTP if found, else exit the script
        return self.otp_code

