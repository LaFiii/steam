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
        prices = []
        for el in elems:
            price_str = "".join(ch for ch in el.text if ch.isdigit() or ch in ",.")
            if not price_str or not any(ch.isdigit() for ch in price_str):
                continue
            try:
                prices.append(float(price_str.replace(",", ".")))
            except ValueError:
                continue
        return prices[:top_n] if top_n else prices
