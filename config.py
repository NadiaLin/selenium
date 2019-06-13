from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.amazon.com/"

class Path:
    # Choose the browser you want to test

    # CHROME_75 = webdriver.Chrome('../driver/chromedriver_75')
    CHROME_74 = webdriver.Chrome('../driver/chromedriver')
    # FIREFOX = 
    # SAFARI = 

class Account_Info:
    CORRECT_ID = "User Email"
    CORRECT_PASSWORD = 'User password'
    USER_NAME = "User name"

    WRONG_ID = "nadia@test.com"
    WRONG_PASSWORD = "imwrong"