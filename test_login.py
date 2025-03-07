import logging
import time

from selenium.webdriver.common.by import By
from setup.basetest import BaseTest

class TestLogin(BaseTest):

    def test(self):
        self.driver.get("https://www.saucedemo.com/")
        logging.info("opened the site")

        username = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        username.click()
        username.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        login.click()

        product = self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']")
        product.click()

        description = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_desc large_size']")
        logging.info(description.text)

        price = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
        logging.info(price.text)

        time.sleep(6)



