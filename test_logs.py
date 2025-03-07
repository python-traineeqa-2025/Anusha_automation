import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from setup.basetest import BaseTest

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class Test_logs(BaseTest):

    def test_cred(self):
        self.driver.get("https://www.saucedemo.com/")
        logging.info("opened the site")
        credentials = self.driver.find_elements(By.XPATH, "//div[@id='login_credentials']")
        logging.info(credentials)
        for i in credentials:
            cred = i.text
            logging.info(cred)
            cred_list = cred.split('\n')
            logging.info(cred_list)














