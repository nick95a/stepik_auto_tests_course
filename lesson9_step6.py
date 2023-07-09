from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    # Переходим на страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
     # Нажимаем на кнопку
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()  
    
    # Заполнить вкладки и перейти на новую
    
    old_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Достаем значение x и заполняем им форму
    
    x = int(browser.find_element(By.ID, "input_value").text)
    function_result = calc(x)    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(function_result)
    
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