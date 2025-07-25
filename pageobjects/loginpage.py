from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from baseclass import BasePage
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
    username_input=(By.ID,"user-name")
    password_input=(By.ID,"password")
    click_login_button=(By.ID,"login-button")
    click_menu_button=(By.ID,"react-burger-menu-btn")
    click_logout_button=(By.ID,"logout_sidebar_link")
    #popup_close_button = (By.ID, "popup-close")  # Use correct locator
    def __init__(self,driver):
        self.driver=driver
        self.base=BasePage(self.driver)

    def setusername(self,username):
        self.base.send_keys(self.username_input,username)

    def setpassword(self,password):
        self.base.send_keys(self.password_input,password)

    def clickloginbutton(self):
        self.base.click_element(self.click_login_button)


    def clickmenubutton(self):
        self.base.click_element(self.click_menu_button)

    def clicklogoutbutton(self):
        self.base.click_element(self.click_logout_button)






