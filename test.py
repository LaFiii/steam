import pytest
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

LOGIN_PAGE_BTN = (By.XPATH, "//*[contains(@class,'global_action_link') and contains(@href,'/login')]")
USERNAME_FIELD = (By.XPATH, "//input[@type='text']")
PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
SUBMIT_BTN = (By.XPATH, "//button[@type='submit' and contains(normalize-space(.), 'Войти')]")
ERROR_MESSAGE = (By.XPATH, "//*[contains(@href,'HelpWithLogin')]/preceding-sibling::div[1]")
UNIQUE_LOCATOR = (By.XPATH, '//*[contains(@class, "btn_green_white_innerfade")]')
TIME = 10
URL = "https://store.steampowered.com/"


@pytest.fixture
def login_page(driver):
    driver.get(URL)
    return driver


def test_auth(login_page):
    fake = Faker()

    login_str = fake.user_name()
    pwd_str = fake.password()
    wait = WebDriverWait(login_page, TIME)

    wait.until(EC.visibility_of_element_located(UNIQUE_LOCATOR))
    wait.until(EC.element_to_be_clickable(LOGIN_PAGE_BTN)).click()
    wait.until(EC.visibility_of_element_located(USERNAME_FIELD)).send_keys(login_str)
    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(pwd_str)
    wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()
    time.sleep(1)
    error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
    assert "Пожалуйста, проверьте" in error.text
