from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 

from base_page import BasePage
import home_page

sign_in_btn = EC.element_to_be_clickable((By.ID, 'signInSubmit'))
email_text_field = EC.element_to_be_clickable((By.ID, 'ap_email'))
password_text_field = EC.element_to_be_clickable((By.ID, 'ap_password'))
password_missing_message = EC.element_to_be_clickable((By.ID, 'auth-password-missing-alert'))
login_error_message = EC.element_to_be_clickable((By.ID, 'auth-error-message-box'))

class LoginPage(BasePage):
    
    def __init__(self, Page):
        self.driver = Page.driver
        print("** Login Page")
        Page.wait_for(sign_in_btn)

    def type_email(self, address):
        BasePage.type_text(self, email_text_field, address)
        # time.sleep(2)

        return self

    def type_password(self, password):
        BasePage.type_text(self, password_text_field, password)
        # time.sleep(2)

        return self
    
    def display_password_missing_message(self):
        # time.sleep(2)
        return BasePage.is_element_present(self, password_missing_message)

    def display_login_fail_message(self):
        # time.sleep(2)
        return BasePage.is_element_present(self, login_error_message)

    def click_login(self):
        # time.sleep(2)
        BasePage.wait_and_click(self, sign_in_btn)

        return self


    

        
