import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os

# Введите логин и пароль
login = ""
password = ""
answer_string = ""
link_1 = "https://stepik.org/lesson/236895/step/1"
link_2 = "https://stepik.org/lesson/236896/step/1"
link_3 = "https://stepik.org/lesson/236897/step/1"
link_4 = "https://stepik.org/lesson/236898/step/1"
link_5 = "https://stepik.org/lesson/236899/step/1"
link_6 = "https://stepik.org/lesson/236903/step/1"
link_7 = "https://stepik.org/lesson/236904/step/1"
link_8 = "https://stepik.org/lesson/236905/step/1"


@pytest.fixture(scope = 'class')
def browser():
    browser = webdriver.Chrome()
    print("Loading the page")
    yield browser
    browser.quit()
    print("Quiting the browser")
        
def calc_answer():
    return math.log(int(time.time()))    
    
class TestStepikLogin():
    
    def test_login(self, browser):
        
        browser.get(link_1)
        
        time.sleep(5)
        
        login_form_button = browser.find_element(By.CSS_SELECTOR, "a[href='/lesson/236895/step/1?auth=login']")
        login_form_button.click()
        
        WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.modal-dialog-inner")))
        
        input_name_field = browser.find_element(By.ID, "id_login_email")
        input_name_field.send_keys(login)

        password_name_field = browser.find_element(By.ID, "id_login_password")
        password_name_field.send_keys(password)
        
        submit_button = browser.find_element(By.CSS_SELECTOR, "button.button_with-loader")
        submit_button.click()
    
    def test_1(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', "The status is incorrect"
        
    def test_2(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_2)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text
        
    def test_3(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_3)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', "The response string is different from 'Correct!'"
        answer_string = answer_string + response_status_text

    def test_4(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_4)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text
        
    def test_5(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_5)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text
        
    def test_6(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_6)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text
    
    def test_7(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_7)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text

    def test_8(self, browser):
                        
        # Находим поле ответа и проверяем его пустоту
        browser.get(link_8)
        
        answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/textarea")))    
        answer_field_text = answer_field.text 
        assert answer_field_text == '', "The text field is not empty"
                        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', answer_string + response_status_text
        
        """
        answer_field = browser.find_element(By.TAG_NAME, "textarea")
        answer_field_text = answer_field.text
        assert answer_field_text == '', "The text field is not empty"
        
        answer_input = calc_answer()
        answer_field.send_keys(answer_input)
        
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
                
        response_status = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint")))
        response_status_text = response_status.text
        
        assert response_status_text == 'Correct!', "The status is incorrect"
        """
        
        
print(answer_string)        

