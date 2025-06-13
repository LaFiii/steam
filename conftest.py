import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum, StrEnum


class Locale(StrEnum):
    RUSSIAN = "ru"
    ENGLISH = "en"


@pytest.fixture(scope="function", params=[Locale.RUSSIAN, Locale.ENGLISH])
def driver(request):
    lang = request.param
    options = Options()
    options.add_argument(f"--lang={lang}")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
