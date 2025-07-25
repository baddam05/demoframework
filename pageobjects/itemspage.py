from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baseclass import BasePage

class itemsprice:

    sort_click_xpath = (By.XPATH,"//select[@class='product_sort_container']")
    lowtohigh_click_xpath = (By.XPATH,"//select[@class='product_sort_container']/option[3]")
    itemsprice_get_xpath = (By.XPATH,"//div[@class='inventory_item_price']")
    scroll_down_len="window.scrollBy(0, 500)"
    scroll_up_len = "window.scrollBy(0, -500)"

    def __init__(self, driver):
        self.driver = driver
        self.base=BasePage(self.driver)
    def clicksortmenu(self):
            self.base.click_element(self.sort_click_xpath)

    def select_low_to_high(self):
        self.base.click_element(self.lowtohigh_click_xpath)

    def get_all_item_prices(self):

        prices_elements = self.base.wait_for_elements_visible(self.itemsprice_get_xpath)


        lis_prices=[]
        for price in prices_elements:
            conprice=price.text.replace('$','')
            fltprice=float(conprice)
            lis_prices.append(fltprice)
        return lis_prices

    def scroll_down(self):
        self.driver.execute_script(self.scroll_down_len)

    def scroll_up(self):
        self.driver.execute_script(self.scroll_up_len)

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#scroll to bottom of the page
    #driver.execute_script("window.scrollTo(0, 0);")# scroll till top of the page

    #scroll till a specific element
    #element = driver.find_element(By.ID, "element_id")
    #driver.execute_script("arguments[0].scrollIntoView();", element)











