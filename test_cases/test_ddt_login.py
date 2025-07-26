from selenium import webdriver
import time
from utilities import xlutils
from pageobjects.loginpage import loginpage
from utilities.customLogger import loggen

from utilities.readproperties import readconfig


class Test_002_DDTlogin:
    baseurl = readconfig.geturl()
    logger=loggen.getlog()
    file=".//testdata/demoxlddt.xlsx"

    def test_DDTlogin(self,setup):
        self.logger.info("********Test_002_DDTlogin********** ")
        self.logger.info("*********verifying ddt login test********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=loginpage(self.driver)
        no_of_rows=xlutils.getnorows(self.file,'Sheet1')
        print(no_of_rows)
        lst_status=[]

        for r in range(2,no_of_rows+1):
            self.username=xlutils.readdata(self.file,'Sheet1',r,1)
            self.password=xlutils.readdata(self.file,'Sheet1',r,2)
            self.exp=xlutils.readdata(self.file,'Sheet1',r,3)

            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clickloginbutton()
            time.sleep(3)
            act_url=self.driver.current_url
            exp_url="https://www.saucedemo.com/inventory.html"
            if act_url==exp_url:
                if self.exp=="pass":
                    self.logger.info("**login ddt passed")
                    self.lp.clickmenubutton()
                    time.sleep(5)
                    self.lp.clicklogoutbutton()
                    lst_status.append("pass")

                    assert True
                elif self.exp=="fail":
                    self.logger.info("**login ddt failed")
                    self.lp.clickmenubutton()

                    self.lp.clicklogoutbutton()
                    lst_status.append("fail")
                    assert False, f"login  unsuccessful:{self.exp=='fail'}"

            elif act_url!=exp_url:
                if self.exp=="pass":
                    self.logger.info("***login ddt failed")
                    time.sleep(5)
                    lst_status.append("fail")

                    assert False
                elif self.exp=="fail":
                    self.logger.info("***login ddt passed")
                    #self.lp.clickmenubutton()
                    time.sleep(5)
                    #self.lp.clicklogoutbutton()
                    lst_status.append("pass")

                    assert True

        if "fail" not in lst_status:
            self.logger.info("****** Test_002_DDTlogin passed **********")

        else:
            self.logger.info("****** Test_002_DDTlogin failed **********")






