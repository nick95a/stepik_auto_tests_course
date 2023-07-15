from selenium import webdriver
from selenium.webdriver.common.by import By
import time, unittest, warnings

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    
class Test_Lesson6_Step12(unittest.TestCase):
    
    def test_page1(self):
        
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name_input = browser.find_element(By.XPATH, "//body/div/form/div[1]//input")
            first_name_input.send_keys("Ivan")
            last_name_input = browser.find_element(By.XPATH, "//body/div/form/div[1]/div[2]/input")
            last_name_input.send_keys("Ivanov")
            email_input = browser.find_element(By.XPATH, "//body/div/form/div[1]/div[3]/input")
            email_input.send_keys("ivanivanov@mail.ru")
            phone_input = browser.find_element(By.XPATH, "//body/div/form/div[2]/div[1]/input")
            phone_input.send_keys("89123456789")
            address_input = browser.find_element(By.XPATH, "//body/div/form/div[2]/div[2]/input")
            address_input.send_keys("Somewhere in mother Russia...")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text is different")
            
            time.sleep(1)
            browser.quit()
            
    def test_page2(self):
        
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name_input = browser.find_element(By.XPATH, "//body/div/form/div[1]//input")
            first_name_input.send_keys("Ivan")
            email_input = browser.find_element(By.XPATH, "//body/div/form/div[1]/div[3]/input")
            email_input.send_keys("ivanivanov@mail.ru")
            phone_input = browser.find_element(By.XPATH, "//body/div/form/div[2]/div[1]/input")
            phone_input.send_keys("89123456789")
            address_input = browser.find_element(By.XPATH, "//body/div/form/div[2]/div[2]/input")
            address_input.send_keys("Somewhere in mother Russia...")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text is different")
            
            time.sleep(1)
            browser.quit()

if __name__ == "__main__":
    
    unittest.main()