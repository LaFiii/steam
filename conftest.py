import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOCALE_MAP = {"russian": "ru", "english": "en"}


@pytest.fixture(scope="session", params=["russian", "english"])
def browser_lang(request):
    return request.param


@pytest.fixture(scope="session")
def driver(browser_lang):
    options = Options()
    code = LOCALE_MAP[browser_lang]
    options.add_argument(f"--lang={code}")
    options.add_experimental_option("prefs", {
        "intl.accept_languages": code
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
