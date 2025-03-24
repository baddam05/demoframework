import random
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class login_signup_page:

    textbox_name_name="name"
    textbox_mail_bycss="input[data-qa='signup-email']"
    click_button_xpath="//button[@class='btn btn-default' and @data-qa='signup-button']"

    click_gender_xpath="//input[contains(@id,'id_gender1')]"
    click_button_byid = "id_gender2"
    textbox_byname="name"
    textbox_byid="password"
    click_date_byid="days"
    click_month_byid = "months"
    click_year_byid="years"
    checkbox_newleteer_byid="newsletter"
    checkbox_specialoffer_byid = "optin"


    textbox_firstname_byid="first_name"
    textbox_lastname_byid="last_name"
    textbox_company_byid="company"
    textbox_address1_byid="address1"
    textbox_address2_byid="address2"
    textbox_country_byid="country"
    textbox_state_byid="state"
    textbox_city_byid="city"
    textbox_zipcode_byid="zipcode"
    textbox_mobilenumber_byid="mobile_number"
    click_button_byxpath="//button[@data-qa='create-account']"
    textofscreen_by_xpath="//header[@id='header']/parent::body"







    def __init__(self,driver):
        self.driver=driver

    def random_mail_gen(self):
        random_string=''.join(random.choices(string.ascii_letters,k=8))
        random_email=random_string+"@gmail.com"
        return random_email

    def entermail(self, username_mail):
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_mail_bycss).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_mail_bycss).send_keys(username_mail)


    def entername(self,name):
        self.driver.find_element(By.NAME,self.textbox_name_name).clear()
        self.driver.find_element(By.NAME,self.textbox_name_name).send_keys(name)

    def click_button(self):
        #self.driver.find_element(By.ID, self.textbox_mail_name).clear()
        self.driver.find_element(By.XPATH, self.click_button_xpath).click()

    try:
        def click_gender_button(self,gender):
            if gender=="Mr":
                self.driver.find_element(By.XPATH,self.click_gender_xpath).click()
            elif gender=="Mrs":
                self.driver.find_element(By.XPATH, self.click_gender_xpath).click()
            else:
                assert f"provide right gender"
    except:

        assert f"not provided right gender"

    def enter_name(self,name):
        self.driver.find_element(By.XPATH, self.textbox_byname).clear()
        self.driver.find_element(By.XPATH,self.textbox_byname).send_keys(name)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_byid).clear()
        self.driver.find_element(By.ID,self.textbox_byid).send_keys(password)

    def select_date(self,date):
        date_ele=Select(self.driver.find_element(By.ID, self. click_date_byid))
        date_ele.select_by_visible_text(str(date))

    def select_month(self,month):
        month_ele=Select(self.driver.find_element(By.ID, self.click_month_byid))
        month_ele.select_by_visible_text(month)

    def select_year(self,year):
        year_ele=Select(self.driver.find_element(By.ID, self.click_year_byid))
        year_ele.select_by_visible_text(str(year))

    def click_newsletter(self):
        self.driver.find_element(By.ID,self.checkbox_newleteer_byid).click()

    def click_specialoffer(self):
        self.driver.find_element(By.ID,self.checkbox_specialoffer_byid).click()

    def enterfirstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_byid).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_byid).send_keys(firstname)

    def enterlastname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_byid).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_byid).send_keys(lastname)

    def entercompany(self, company):
        self.driver.find_element(By.ID, self.textbox_company_byid).clear()
        self.driver.find_element(By.ID, self.textbox_company_byid).send_keys(company)

    def enteraddrees1(self,address1):
        self.driver.find_element(By.ID,self.textbox_address1_byid).clear()
        self.driver.find_element(By.ID,self.textbox_address1_byid).send_keys(address1)

    def enteraddress2(self, address2):
        self.driver.find_element(By.ID, self.textbox_address2_byid).clear()
        self.driver.find_element(By.ID, self.textbox_address2_byid).send_keys(address2)

    def entercountry(self, country):
        allcountries=Select(self.driver.find_element(By.ID, self.textbox_country_byid))
        allcountries.select_by_visible_text(country)

    def enterstate(self, state):
        self.driver.find_element(By.ID, self.textbox_state_byid).clear()
        self.driver.find_element(By.ID, self.textbox_state_byid).send_keys(state)

    def entercity(self, city):
        self.driver.find_element(By.ID, self.textbox_city_byid).clear()
        self.driver.find_element(By.ID, self.textbox_city_byid).send_keys(city)

    def enterzipcode(self, zipcode):
        self.driver.find_element(By.ID, self.textbox_zipcode_byid).clear()
        self.driver.find_element(By.ID, self.textbox_zipcode_byid).send_keys(zipcode)

    def entermobilenumber(self, mobilenumber):
        self.driver.find_element(By.ID, self.textbox_mobilenumber_byid).clear()
        self.driver.find_element(By.ID, self.textbox_mobilenumber_byid).send_keys(mobilenumber)

    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.click_button_byxpath).click()

    def check_acc_created(self):
        ele=WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textofscreen_by_xpath)))
        alltext=ele.text
        print(f"Actual text found: '{alltext}'")
        if "ACCOUNT CREATED!" in alltext:
            return True
        else:
            return False









































