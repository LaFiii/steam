from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SearchResultsPage(BasePage):
    RESULT_ROWS = (By.XPATH, '//*[@id="search_resultsRows"]/a')
    PRICE_LABEL = (By.XPATH, '//*[contains(@class, "discount_final_price")]')

    def get_results_count(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ROWS))
        return len(rows)

    def get_prices(self, top_n: int = None) -> list[float]:
        elems = self.wait.until(EC.presence_of_all_elements_located(self.PRICE_LABEL))
        prices = [float("".join(ch for ch in el.text if ch.isdigit() or ch == ".").replace(",", "."))
                  for el in elems
                  if el.text.strip()
                  ]
        return prices
