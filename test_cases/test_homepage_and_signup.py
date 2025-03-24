import time

import pytest
from selenium import webdriver
from  pageobjects.homepage import homepage
from pageobjects.loginandsignuppage import login_signup_page
from utilities.readproperties import readconfig
from utilities.customLogger import loggen

class Test_001_signup:
    baseurl =readconfig.geturl()
    password=readconfig.getpassword()
    logger=loggen.getlog()
    name="raki"
    gender="Mr"
    date=12
    month="April"
    year=2018
    firstname="rakesh"
    lastname="baddam"
    company="EY"
    address1="room1"
    address2="room2"
    country="United States"
    state="telangana"
    city="kailashhills"
    zipcode="123456"
    mobilenumber=1234567890

    @pytest.mark.sanity
    def test_homepage_title(self,setup):
        self.logger.info("**********Test_001_signup***********")
        self.logger.info("**********launching home page***********")

        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        self.capturedtitle=self.driver.title
        if self.capturedtitle=="Automation Exercise":
            self.logger.info("title of homepage verified")
            assert True
        else:
            self.logger.info("title of homepage failed")
            assert  False

    @pytest.mark.sanity
    def test_signup(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.hp=homepage(self.driver)
        self.hp.clicklogin_signup_button()
        time.sleep(3)
        self.logger.info("**launched  signup form**")
        self.sp=login_signup_page(self.driver)
        self.username_mail=self.sp.random_mail_gen()
        self.sp.entername(self.name)
        self.sp.entermail(self.username_mail)
        time.sleep(2)
        self.sp.click_button()
        time.sleep(5)
        self.sp.click_gender_button(self.gender)


        self.driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(3)

        self.sp.enter_password(self.password)

        self.sp.select_date(self.date)
        self.sp.select_month(self.month)
        self.sp.select_year(self.year)
        self.sp.click_newsletter()
        self.sp.click_specialoffer()
        self.sp.enterfirstname(self.firstname)
        self.sp.enterlastname(self.lastname)
        self.sp.entercompany(self.company)
        self.sp.enteraddrees1(self.address1)
        self.sp.enteraddress2(self.address2)
        self.driver.execute_script("window.scrollBy(0, 400)")
        self.sp.entercountry(self.country)
        self.sp.enterstate(self.state)
        self.sp.entercity(self.city)
        self.sp.enterzipcode(self.zipcode)
        self.sp.entermobilenumber(self.mobilenumber)
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.sp.click_create_button()
        account_status=self.sp.check_acc_created()
        time.sleep(5)
        if account_status==True:
            self.logger.info("******Account created succefully*****")
            assert True
        else:
            self.logger.info("******Account creation unsuccessful*****")
            assert False

        time.sleep(6)

        self.driver.quit()




