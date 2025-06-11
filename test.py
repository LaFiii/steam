from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException

fake = Faker()
login_str = fake.user_name()
pwd_str = fake.password()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://store.steampowered.com/"

driver.get(url)
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//*[contains(@class,'global_action_link') and contains(@href,'/login')]")))
login_btn.click()
login = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
login.send_keys(login_str)
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
password.send_keys(pwd_str)
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,
        "//button[@type='submit' and contains(normalize-space(.), 'Войти')]")))
login_btn.click()
try:
    short_wait = WebDriverWait(driver,5)
    short_wait.until(EC.visibility_of_element_located((By.XPATH,
        "//*[contains(text(),'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")))
    print("Ошибка входа: неверный логин/пароль")
except (TimeoutException,NoSuchElementException):
    print("Сообщение об ошибке не найдено")
finally:
    driver.quit()