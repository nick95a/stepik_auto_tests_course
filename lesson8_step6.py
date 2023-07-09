from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0, 100)")

    # Извлечем значение x
    x = int(browser.find_element(By.ID, "input_value").text)
    
    
    # Считаем значение функции и заполняем поле
    function_result = calc(x)    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(function_result)
    
    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Отмечаем radiobutton
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Находим элемент и отправляем форму
    submit_button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()