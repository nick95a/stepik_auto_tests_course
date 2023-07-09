from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "empty.txt")
    
    # Переходим на страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполняем поля
    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("Ivan")

    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("Ivanov")
    
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("IvanIvanov@mail.ru")
    
    attachment_field = browser.find_element(By.ID, "file")
    attachment_field.send_keys(file_path)
    
    # Отправляем форму
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()