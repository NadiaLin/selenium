from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException       


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    
    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, element_locator, time=10):   
        try:  
            print("Waiting", element_locator.locator) 
            element = WebDriverWait(self.driver, time).until(element_locator)
            print(element_locator.locator, "is present!")
        except NoSuchElementException:
            print("Element not found", element_locator.locator)

        return element

    def wait_and_click(self, element_locator):      
        element = self.wait_for(element_locator)
        element.click()

    def get_text(self, element_locator):      
        element = self.wait_for(element_locator)
        return element.text

    def type_text(self, element_locator, text):
        element = self.wait_for(element_locator)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, element_locator):
        try: 
            self.wait_for(element_locator, 3)
            return True
        except NoSuchElementException: 
            return False
        

        
