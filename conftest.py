import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum


class Locale(Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"


@pytest.fixture(scope="session", params=[Locale.RUSSIAN, Locale.ENGLISH])
def driver(request):
    lang = request.param
    options = Options()
    code = lang.value
    options.add_argument(f"--lang={code}")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
