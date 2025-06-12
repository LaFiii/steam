import pytest
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LOGIN_PAGE_BTN = (By.XPATH, "//*[contains(@class,'global_action_link') and contains(@href,'/login')]")
USERNAME_FIELD = (By.XPATH, "//input[@type='text']")
PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
SUBMIT_BTN = (By.XPATH, "//button[@type='submit' and contains(normalize-space(.), 'Войти')]")
ERROR_MESSAGE = (By.XPATH,
                 "//*[contains(text(),'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")


@pytest.mark.parametrize("run_id", range(5))
def test(driver, run_id):
    fake = Faker()
    login_str = fake.user_name()
    pwd_str = fake.password()
    wait = WebDriverWait(driver, 10)
    url = "https://store.steampowered.com/"

    driver.get(url)
    wait.until(EC.element_to_be_clickable(LOGIN_PAGE_BTN)).click()
    wait.until(EC.visibility_of_element_located(USERNAME_FIELD)).send_keys(login_str)
    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(pwd_str)
    wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()

    try:
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
    except TimeoutException:
        pytest.fail("Ожидали сообщение об ошибке логина, но его не было")
    else:
        assert "Пожалуйста, проверьте" in error.text
