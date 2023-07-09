from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    # Переходим на страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    # Задаем ожидание до становления цены $100
    desired_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    
    # Нажимаем на кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()  
    
    # Достаем значение x и заполняем им форму
    
    x = int(browser.find_element(By.ID, "input_value").text)
    function_result = calc(x)    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(function_result)
    
    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()  
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()