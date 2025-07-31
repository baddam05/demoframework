from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from baseclass import  BasePage

class login_signup_page:

    textbox_name_name=(By.NAME,"name")
    textbox_mail_bycss=(By.CSS_SELECTOR,"input[data-qa='signup-email']")
    click_button_xpath=(By.XPATH,"//button[@class='btn btn-default' and @data-qa='signup-button']")

    click_gender_xpath=(By.XPATH,"//input[contains(@id,'id_gender1')]")
    click_button_byid =(By.ID,"id_gender2")
    textbox_byname=(By.NAME,"name")
    textbox_byid=(By.ID,"password")
    click_date_byid=(By.ID,"days")
    click_month_byid =(By.ID,"months")
    click_year_byid=(By.ID,"years")
    checkbox_newleteer_byid=(By.ID,"newsletter")
    checkbox_specialoffer_byid =(By.ID,"optin")

    textbox_firstname_byid=(By.ID,"first_name")
    textbox_lastname_byid=(By.ID,"last_name")
    textbox_company_byid=(By.ID,"company")
    textbox_address1_byid=(By.ID,"address1")
    textbox_address2_byid=(By.ID,"address2")
    textbox_country_byid=(By.ID,"country")
    textbox_state_byid=(By.ID,"state")
    textbox_city_byid=(By.ID,"city")
    textbox_zipcode_byid=(By.ID,"zipcode")
    textbox_mobilenumber_byid=(By.ID,"mobile_number")
    click_button_byxpath=(By.XPATH,"//button[@data-qa='create-account']")
    textofscreen_by_xpath=(By.XPATH,"//header[@id='header']/parent::body")


    def __init__(self,driver):
        self.driver=driver
        self.base=BasePage(self.driver)

    def entermail(self,randommail):
        self.base.send_keys(self.textbox_mail_bycss,randommail)

    def entername(self,name):
        self.base.send_keys(self.textbox_name_name,name)


    def click_button(self):
        self.base.click_element(self.click_button_xpath)


    def click_gender_button(self,gender):
        try:
            if gender=="Mr":
                self.base.click_element(self.click_gender_xpath)
            elif gender=="Mrs":
                self.base.click_element(self.click_button_byid)
            else:
                assert f"provide right gender"
        except:
            assert f"not provided right gender"

    def enter_name(self,name):
        self.base.send_keys(self.textbox_byname,name)

    def enter_password(self,password):
        self.base.send_keys(self.textbox_byid,password)

    def select_date(self,date):
        date_ele=Select(self.base.wait_for_element_visible(self.click_date_byid))
        date_ele.select_by_visible_text(str(date))

    def select_month(self,month):
        month_ele=Select(self.base.wait_for_element_visible(self.click_month_byid))
        month_ele.select_by_visible_text(month)

    def select_year(self,year):
        year_ele=Select(self.base.wait_for_element_visible(self.click_year_byid))
        year_ele.select_by_visible_text(str(year))

    def click_newsletter(self):
        self.base.click_element(self.checkbox_newleteer_byid)

    def click_specialoffer(self):
        self.base.click_element(self.checkbox_specialoffer_byid)

    def enterfirstname(self,firstname):
        self.base.send_keys(self.textbox_firstname_byid,firstname)


    def enterlastname(self,lastname):
        self.base.send_keys(self.textbox_lastname_byid,lastname)

    def entercompany(self,company):
        self.base.send_keys(self.textbox_company_byid,company)

    def enteraddrees1(self,address1):
        self.base.send_keys(self.textbox_address1_byid,address1)

    def enteraddress2(self,address2):
        self.base.send_keys(self.textbox_address2_byid,address2)

    def entercountry(self, country):
        allcountries=Select(self.base.wait_for_element_visible(self.textbox_country_byid))
        allcountries.select_by_visible_text(country)

    def enterstate(self,state):
        self.base.send_keys(self.textbox_state_byid,state)

    def entercity(self,city):
        self.base.send_keys(self.textbox_city_byid,city)

    def enterzipcode(self, zipcode):
        self.base.send_keys(self.textbox_zipcode_byid,zipcode)

    def entermobilenumber(self, mobilenumber):
        self.base.send_keys(self.textbox_mobilenumber_byid,mobilenumber)

    def click_create_button(self):
        self.base.click_element(self.click_button_byxpath)

    def check_acc_created(self):
        ele=self.base.wait_for_element_visible(self.textofscreen_by_xpath)
        alltext=ele.text
        print(f"Actual text found: '{alltext}'")
        if "ACCOUNT CREATED!" in alltext:
            return True
        else:
            return False









































