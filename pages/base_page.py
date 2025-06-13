from selenium.webdriver.support.ui import WebDriverWait
from config_reader import ConfigReader


class BasePage:
    def __init__(self, driver, timeout=None):
        self.driver = driver
        real_timeout = timeout or ConfigReader.get_timeout()
        self.wait = WebDriverWait(driver, real_timeout)
