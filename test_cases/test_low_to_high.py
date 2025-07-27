from utilities.readproperties import readconfig
from pageobjects.loginpage import loginpage
from pageobjects.itemspage import itemsprice
from utilities.customLogger import loggen
import time


class Test_003_check_price_lowtohigh:
    baseurl=readconfig.geturl()
    username=readconfig.getusername()
    password=readconfig.getpassword()
    logger=loggen.getlog()



    def test_price_low_to_high(self,setup):
        self.logger.info("********Test_003_check_price_lowtohigh************")
        self.logger.info("********trying to login ************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        self.logger.info("********login successful************")
        time.sleep(3)
        self.ip=itemsprice(self.driver)
        self.ip.clicksortmenu()
        self.ip.select_low_to_high()
        self.ip.scroll_down()
        time.sleep(5)



        allitemprices=self.ip.get_all_item_prices()
        self.logger.info("********got all prices in list************")
        self.logger.info("********now trying to verify low to high using loop statement************")

        sorted_prices=sorted(allitemprices)  #sorted(items,reverse=false(default low to high),true(high to low))
        if sorted_prices==allitemprices:
            self.logger.info("prices sorted from low to high")
        else:
            self.logger.error("price not sorted from low to high")
            self.driver.save_screenshot(".\\screenshots\\" + "test_price_low_to_high.png")
            self.logger.info(f"actual prices :{allitemprices}")
            self.logger.info(f"expected sorted prices:{sorted_prices}")

        self.logger.info(f"prices sorted:{sorted_prices==allitemprices}")

        #approach 2 this loop statement to verify low to high prices
        # x=allitemprices[0]
        # y=[]
        #
        # for price in allitemprices:
        #     if price>=x:
        #         x=price
        #
        #         y.append(x)
        #
        #     else:
        #         self.logger.error("items price is not low to high")













