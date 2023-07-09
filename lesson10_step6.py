from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    # Переходим на страницу
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
     # Нажимаем на кнопку
    submit_button = browser.find_element(By.ID, "button")
    submit_button.click()  

    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()