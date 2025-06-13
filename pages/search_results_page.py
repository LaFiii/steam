from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SearchResultsPage(BasePage):
    RESULT_ROWS = (By.XPATH, '//*[@id="search_resultsRows"]')

    def get_results_count(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ROWS))
        return len(rows)

    def assert_results_count(self, expected_count: int):
        actual = self.get_results_count()
        assert actual <= expected_count, f"Ожидали {expected_count} результатов, получили {actual}"
