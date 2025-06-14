from selenium.webdriver.support.ui import WebDriverWait
from config_reader import ConfigReader
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    UNIQUE_LOCATOR = None

    def __init__(self, driver, timeout=None):
        self.driver = driver
        real_timeout = timeout or ConfigReader.get_timeout()
        self.wait = WebDriverWait(driver, real_timeout)

    def wait_for_open(self):
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_LOCATOR))
