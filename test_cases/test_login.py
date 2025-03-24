import time

import pytest
from selenium import webdriver
from pageobjects.loginpage import loginpage
from utilities.readproperties import readconfig
from utilities.customLogger import loggen


class Test_001:
    baseurl=readconfig.geturl()
    username=readconfig.getusername()
    password=readconfig.getpassword()
    logger=loggen.getlog()



    def test_homepagetitle(self,setup):
        self.logger.info("********** Test_001 *************")
        self.logger.info("********** verifying home page title *************")

        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(5)
        act_title=self.driver.title



        if act_title=="Swag Labs":
            self.logger.info("homepage title verified")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepagetitle1.png")
            self.logger.error("homepage title not verified")
            self.driver.close()
            assert False


    # def test_login(self,setup):
    #     self.logger.info("************* trying to login *****************")
    #     self.driver=setup
    #     self.driver.get(self.baseurl)
    #     self.driver.maximize_window()
    #     time.sleep(5)
    #     self.lp=loginpage(self.driver)
    #     self.lp.setusername(self.username)
    #     self.lp.setpassword(self.password)
    #     self.lp.clickloginbutton()
    #
    #
    #
    #
    #     act_title=self.driver.title
    #
    #     if act_title=="Swag Labs":
    #         self.logger.info("loginpage title verified")
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
    #         self.logger.error("loginpage  title not verified")
    #         self.driver.close()
    #         assert False