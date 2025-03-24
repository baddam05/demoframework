import time
#import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
options = Options()
prefs = {
    "credentials_enable_service": False,  # Disable password manager
    "profile.password_manager_enabled": False  # Disable the popup
}
options.add_experimental_option("prefs", prefs)


# Launch Chrome with options
driver = webdriver.Chrome(options=options)


class loginpage:
    textbox_username_id="user-name"
    textbox_password_id="password"
    button_click_id="login-button"
    menu_click_id="react-burger-menu-btn"
    logout_click_id="logout_sidebar_link"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_username_id))
        )
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.textbox_password_id))
        )
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickloginbutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.button_click_id))
        )
        self.driver.find_element(By.ID,self.button_click_id).click()

    def clickmenubutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.menu_click_id))
        )
        self.driver.find_element(By.ID, self.menu_click_id).click()

    def clicklogoutbutton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self. logout_click_id))
        )
        self.driver.find_element(By.ID, self.logout_click_id).click()





