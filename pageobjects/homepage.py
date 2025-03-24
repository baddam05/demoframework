
from selenium.webdriver.common.by import By



class homepage:
    signup_login_css="a[href='/login']"



    def __init__(self,driver):
        self.driver=driver

    def clicklogin_signup_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.signup_login_css).click()









