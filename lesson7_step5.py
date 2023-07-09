from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text
    expression_value = calc(x_value)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(expression_value)
    
    # Отмечаем checkbox
    checkbox = browser.find_element(By.CSS_SELECTOR, "[type = 'checkbox']")
    checkbox.click()
    
    # Отмечаем radiobutton
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    radiobutton.click()

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