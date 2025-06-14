from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MainPage(BasePage):
    UNIQUE_LOCATOR = (By.XPATH, '//*[contains(@class, "btn_green_white_innerfade")]')
    SEARCH_LOCATOR = (By.ID, "store_nav_search_term")
    BTN_LOCATOR = (By.ID, "store_search_link")
    SORT_LOCATOR = (By.ID, "sort_by_trigger")
    PRICE_LOCATOR = (By.ID, "Price_DESC")
    LOADING_LOCATOR = (By.ID, "searchtag_tmpl")
    CONTAINER_LOCATOR = (By.ID, "search_result_container")

    def search(self, game_name):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_LOCATOR)).send_keys(game_name, Keys.ENTER)

    def wait_for_container_opacity(self):
        self.wait.until(
            lambda d: "opacity" not in (d.find_element(*self.CONTAINER_LOCATOR).get_attribute("style") or ""))

    def sort_by_price(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_LOCATOR)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_LOCATOR)).click()
        self.wait_for_container_opacity()