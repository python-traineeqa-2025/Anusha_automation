import logging
import time

from selenium.webdriver.common.by import By
import json
from setup.basetest import BaseTest

class TestCred(BaseTest):
    def test_cred(self):
        self.driver.get("https://www.saucedemo.com/")
        logging.info("opened the site")
        cred_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Class_automation\Anusha_automation\cred\cred.json"
        with open(cred_path, 'r') as file:
            cred = json.load(file)


        for user, credentials in cred.items():
            uname = credentials['uname']
            pwd = credentials['pwd']

            username = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
            password= self.driver.find_element(By.XPATH, "//input[@id='password']")
            login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
            username.send_keys(uname)
            password.send_keys(pwd)
            time.sleep(2)
            login.click()
            self.driver.back()











