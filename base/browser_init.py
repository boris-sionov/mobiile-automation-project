from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.service import Service as SafariService


class BrowserInit:

    @staticmethod
    def init_chrome():
        options = Options()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(service=Service(), options=options)

    @staticmethod
    def init_edge():
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        return webdriver.Edge(service=EdgeService(), options=options)

    @staticmethod
    def init_firefox():
        options = FirefoxOptions()
        return webdriver.Firefox(service=FirefoxService(), options=options)

    @staticmethod
    def init_safari():
        driver = webdriver.Safari(service=SafariService())
        return driver
