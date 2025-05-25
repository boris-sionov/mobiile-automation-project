from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.safari.service import Service as SafariService

from utilities.config import ConfigReader


class BrowserInit:
    # Class-level headless flag loaded from config.ini
    headless = ConfigReader.read_config_bool("web", "headless")

    @staticmethod
    def init_chrome():
        """Initialize Chrome browser with optional headless mode."""
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        if BrowserInit.headless:
            options.add_argument("--headless=new")  # modern headless mode
        return webdriver.Chrome(service=ChromeService(), options=options)

    @staticmethod
    def init_edge():
        """Initialize Edge browser with optional headless mode."""
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        if BrowserInit.headless:
            options.add_argument("--headless=new")
        return webdriver.Edge(service=EdgeService(), options=options)

    @staticmethod
    def init_firefox():
        """Initialize Firefox browser with optional headless mode."""
        options = FirefoxOptions()
        if BrowserInit.headless:
            options.add_argument("--headless")  # classic headless
        return webdriver.Firefox(service=FirefoxService(), options=options)

    @staticmethod
    def init_safari():
        """Initialize Safari browser (headless mode is not supported)."""
        return webdriver.Safari(service=SafariService())
