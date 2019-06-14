# selenium

### Installation
 - please follow the steps from [selenium-python](https://selenium-python.readthedocs.io/installation.html)
 
### How to run
 - make sure you have installed selenium
 - modify the user account information on config.py
 ```
 class Account_Info:
    CORRECT_ID = "User Email"
    CORRECT_PASSWORD = 'User password'
    USER_NAME = "User name"
 ```
 - If use chrome, then check the chrome version and change the browser from test.py file or you can change other browser you want
 ```
@classmethod
    def setUpClass(cls):
        cls.driver = Path.CHROME_74  # change driver of browser here
 ```
 - Run test case
 ```
 $ cd test_suit/
 $ python test_login.py
 ```

### driver
 - A folder to put browser driver

### page
 - Use page object to separate the web view
 
### test_suite
 - Test case will be put in this folder
 
 ### config.py
  - Put the config setting arguments
