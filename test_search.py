import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


@pytest.mark.parametrize("lang", ["russian", "english"])
@pytest.mark.parametrize("game, expected_count", [
    ("The Witcher", 10),
    ("Fallout", 20)])
def test_search_and_filter(driver, lang, game, expected_count):
    main_page = MainPage(driver)
    main_page.open(lang=lang)
    main_page.search(game)
    main_page.sort_by_price()
    results_page = SearchResultsPage(driver)
    results_page.assert_results_count(expected_count)
