import time 
import unittest
from selenium import webdriver

import sys
sys.path.append("..")
from page import home_page, base_page, login_page
from config import URL
from config import Path
from config import Account_Info

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Path.CHROME_74

    def setUp(self):
        self.driver.get(URL)
        self.app = base_page.BasePage(self.driver)

        print("*** web launch ***")

    def test_login_1_with_empty_password(self):   
        HomePage = home_page.HomePage(self.app)     
        LoginPage = HomePage.click_account_list()
        LoginPage = LoginPage.type_email(Account_Info.WRONG_ID)
        LoginPage = LoginPage.click_login()

        self.assertEqual(LoginPage.display_password_missing_message() , True)

    def test_login_2_with_wrong_account(self):   
        HomePage = home_page.HomePage(self.app)     
        LoginPage = HomePage.click_account_list()
        LoginPage = LoginPage.type_email(Account_Info.WRONG_ID).type_password(Account_Info.WRONG_PASSWORD).click_login()

        self.assertEqual(LoginPage.display_login_fail_message() , True)

    def test_login_3_with_correct_account(self):
        HomePage = home_page.HomePage(self.app) 
        LoginPage = HomePage.click_account_list()      
        LoginPage = LoginPage.type_email(Account_Info.CORRECT_ID).type_password(Account_Info.CORRECT_PASSWORD).click_login()
        HomePage = home_page.HomePage(self.app)
        
        self.assertEqual(Account_Info.USER_NAME, HomePage.get_user_name())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
