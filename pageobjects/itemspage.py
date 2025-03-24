from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class itemsprice:

    sort_click_xpath = "//select[@class='product_sort_container']"
    lowtohigh_click_xpath = "//select[@class='product_sort_container']/option[3]"
    itemsprice_get_xpath = "//div[@class='inventory_item_price']"
    scroll_down_len="window.scrollBy(0, 500)"
    scroll_up_len = "window.scrollBy(0, -500)"

    def __init__(self, driver):
        self.driver = driver

    def clicksortmenu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_click_xpath))
        )
        self.driver.find_element(By.XPATH, self.sort_click_xpath).click()

    def select_low_to_high(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lowtohigh_click_xpath))
        )
        self.driver.find_element(By.XPATH, self.lowtohigh_click_xpath).click()

    def get_all_item_prices(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.itemsprice_get_xpath))
        )
        prices_elements = self.driver.find_elements(By.XPATH, self.itemsprice_get_xpath)


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











