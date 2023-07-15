import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get(link)
    print("Loading the page")
    yield browser
    browser.quit()
    print("Quiting the browser")
    
class TestStepikLogin:
    
    @pytest.mark.xfail(reason = "pop-up window not available")
    def test_login(self, browser):
        
        time.sleep(5)
        
        login_form_button = browser.find_element(By.CSS_SELECTOR, "a[href='/lesson/236895/step/1?auth=login']")
        login_form_button.click()
        
        WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.modal-dialog-inner")))
        
        input_name_field = browser.find_element(By.ID, "id_login_email")
        input_name_field.send_keys("nick95a@yandex.ru")

        password_name_field = browser.find_element(By.ID, "id_login_password")
        password_name_field.send_keys("2627578aA")
        
        submit_button = browser.find_element(By.CSS_SELECTOR, "button.button_with-loader")
        submit_button.click()
        
        time.sleep(5)
        
        login_form_button = browser.find_element(By.CSS_SELECTOR, "a[href='/lesson/236895/step/1?auth=login']")
        login_form_button.click()           
        
        WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.modal-dialog-inner")))
