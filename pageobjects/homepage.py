from selenium.webdriver.common.by import By
from baseclass import BasePage

class homepage:
    signup_login_xpath=(By.XPATH,"//a[text()=' Signup / Login']")

    def __init__(self,driver):
        self.driver=driver
        self.base=BasePage(self.driver)

    def clicklogin_signup_button(self):
        self.base.click_element(self.signup_login_xpath)









