from selenium import webdriver
import time
import random
from faker import Faker

fake = Faker()


def data_generator():
    username = fake.user_name()
    password = fake.password(
        length=random.randint(2, 50)
    )
    return username, password


login_str, pwd_str = data_generator()
driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/")
time.sleep(5)
login_btn = driver.find_element("xpath", "//*[contains(@class,'global_action_link') and contains(@href,'/login')]")
login_btn.click()
time.sleep(10)
login = driver.find_element("xpath", "//*[@type='text']")
login.send_keys(login_str)
password = driver.find_element("xpath", "//*[@type='password']")
password.send_keys(pwd_str)
time.sleep(5)
login_btn = driver.find_element("xpath", "//*[@type='submit' and contains(text(), 'Войти')]")
login_btn.click()
time.sleep(10)
error = driver.find_element("xpath",
                            "//*[contains(text(),'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")
if error:
    print("Ошибка входа: неверный логин/пароль")
else:
    print("Сообщение об ошибке не найдено")
