from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MainPage(BasePage):
    URL = "https://store.steampowered.com/"
    UNIQUE_LOCATOR = (By.XPATH, '//*[contains(@class, "btn_green_white_innerfade")]')
    SEARCH_LOCATOR = (By.XPATH, '//*[@id="store_nav_search_term"]')
    BTN_LOCATOR = (By.XPATH, '//*[@id="store_search_link"]')
    SORT_LOCATOR = (By.XPATH, '//*[@id="sort_by_trigger"]')
    PRICE_LOCATOR = (By.XPATH, '//*[@id="Price_DESC"]')

    def open(self, lang: str = "russian"):
        url = f"{self.URL}?l={lang}"
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_LOCATOR))

    def search(self, game_name):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_LOCATOR)).send_keys(game_name, Keys.ENTER)

    def sort_by_price(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_LOCATOR)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_LOCATOR)).click()
