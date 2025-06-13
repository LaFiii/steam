import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from config_reader import ConfigReader


@pytest.mark.parametrize("game, expected_count", [("The Witcher", 10), ("Fallout", 20)])
def test_search_and_filter(driver, game, expected_count):
    driver.get(ConfigReader.get_base_url())
    main_page = MainPage(driver)
    main_page.wait_for_open()
    main_page.search(game)
    main_page.sort_by_price()
    results_page = SearchResultsPage(driver)
    actual_count = results_page.get_results_count()
    assert actual_count >= expected_count, (
        f"Ожидали минимум {expected_count} результатов, получили {actual_count}")
    prices = results_page.get_prices()[:5]
    assert prices == sorted(prices, reverse=True), f"Цены не по убыванию: {prices}"