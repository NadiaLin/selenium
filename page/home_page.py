from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time 

import login_page
from base_page import BasePage
from config import Account_Info

sign_in_list_btn = EC.presence_of_element_located((By.ID, 'nav-link-accountList'))
sign_in_btn = EC.element_to_be_clickable((By.ID, 'nav-flyout-ya-signin'))
user_element = EC.element_to_be_clickable((By.CLASS_NAME, 'nav-shortened-name'))
order_btn = EC.presence_of_element_located((By.ID, 'nav-orders'))

class HomePage(BasePage):
    
    def __init__(self, Page):
        self.driver = Page.driver
        print("** Home Page")
        Page.wait_for(order_btn)   
        
    def click_account_list(self):       
        BasePage.wait_and_click(self, sign_in_list_btn)
        print("Go to Login Page!")
        # time.sleep(2)

        return login_page.LoginPage(self)

    def get_user_name(self):  
        user_name = BasePage.get_text(self, user_element)
        print(user_name)
        
        return user_name
