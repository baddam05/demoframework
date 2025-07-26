import os
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,ElementClickInterceptedException
from utilities.customLogger import loggen


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.logger=loggen.getlog()

    def save_screenshot(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        screenshot_path = os.path.join(os.getcwd(), "screenshots", filename)
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)


    def wait_for_element_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            self.logger.info(f"Timeout: Element {locator} not visible after {self.timeout} seconds")
            self.save_screenshot()
            return None

    def wait_for_elements_visible(self, locator):
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            self.logger.info(f"Timeout: Element {locator} not visible after {self.timeout} seconds")
            self.save_screenshot()
            return None

    def wait_for_element_clickable(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            self.logger.info(f"Timeout: Element {locator} not visible after {self.timeout} seconds")
            self.save_screenshot()
            return None

    def wait_for_element_present(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.logger.info(f"Timeout: Element {locator} not visible after {self.timeout} seconds")
            self.save_screenshot()
            return None

    def wait_for_alert(self):
        try:
            element = self.wait.until(EC.alert_is_present())
            return element
        except TimeoutException:
            self.logger.info(f"Timeout: Alert not visible after {self.timeout} seconds")
            self.save_screenshot()
            return None
    def click_element(self, locator):
        try:
            element = self.wait_for_element_clickable(locator)
            if element:
                element.click()
            else:
                self.logger.info(f"Cannot click, element {locator} not found or not visible.")
        except (ElementClickInterceptedException, Exception) as e:
            self.logger.info(f"Exception while clicking element {locator}: {e}")
            self.save_screenshot()

    def send_keys(self,locator,text):
        try:
            element = self.wait_for_element_visible(locator)
            if element:
                element.clear()
                element.send_keys(text)
            else:
                self.logger.info(f"Cannot send keys, element {locator} not found or not visible.")
        except Exception as e:
            self.logger.info(f"Exception while sending keys to element {locator}: {e}")
            self.save_screenshot()

    def get_element_text(self, locator):
        try:
            element = self.wait_for_element_visible(locator)
            if element:
                return element.text
            else:
                self.logger.info(f"Cannot get text, element {locator} not found or not visible.")
                return ""
        except Exception as e:
            self.logger.info(f"Exception while getting text from element {locator}: {e}")
            self.save_screenshot()
            return ""

    
