import time
from pageobjects.loginpage import loginpage
from utilities.readproperties import readconfig
from utilities.customLogger import loggen
from baseclass import BasePage


class Test_001:
    baseurl=readconfig.geturl()
    username=readconfig.getusername()
    password=readconfig.getpassword()
    logger=loggen.getlog()



    def test_homepagetitle(self,setup):
        self.logger.info("********** Test_001 *************")
        self.logger.info("********** verifying home page  *************")

        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(5)

        act_url = self.driver.current_url


        if act_url!="https://www.saucedemo.com/":
            self.logger.info("homepage URL verified")
            print(f"{act_url}!=https://www.saucedemo.com/")
            self.screenshot = BasePage(self.driver)
            self.screenshot.save_screenshot()
            assert False


        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepagetitle1.png")
            self.logger.error("homepage URL not verified ")
            assert False


    def test_login(self,setup):
        self.logger.info("************* trying to login *****************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp=loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        self.logger.info("*****opening items page*********")
        time.sleep(3)




        act_url=self.driver.current_url

        if act_url=="https://www.saucedemo.com/inventory.html":
            self.logger.info("loginpage URL verified")

            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.error("loginpage  URL not verified")
            assert False


