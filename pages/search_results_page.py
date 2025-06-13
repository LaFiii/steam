from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SearchResultsPage(BasePage):
    RESULT_ROWS = (By.XPATH, '//*[@id="search_resultsRows"]/a')
    PRICE_LABEL = (By.XPATH, '//*[contains(@class, "discount_final_price")]')

    def get_results_count(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ROWS))
        return len(rows)

    def assert_results_count(self, expected_min_count: int):
        actual = self.get_results_count()
        assert actual >= expected_min_count, (
            f"Ожидали минимум {expected_min_count} результатов, получили {actual}")

    def get_prices(self, top_n: int = None) -> list[float]:
        elems = self.wait.until(EC.presence_of_all_elements_located(self.PRICE_LABEL))
        prices = [float("".join(ch for ch in el.text if ch.isdigit() or ch == ".").replace(",", "."))
            for el in elems
            if el.text.strip()
                  ]
        return prices

    def assert_results_descending(self, top_n):
        prices = self.get_prices(top_n)
        assert prices == sorted(prices, reverse=True), f"Цены не по убыванию: {prices}"
