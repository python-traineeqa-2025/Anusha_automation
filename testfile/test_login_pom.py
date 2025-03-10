import logging
import time

from setup.basetest import BaseTest

from page_objects.LoginPom.loginpage import LoginPage

class TestLogs(BaseTest):
    def test_login(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        login_page = LoginPage(self.driver)
        uname = self.cred["standard_username"]
        pwd = self.cred["Password"]
        login_page.login(uname,pwd)
        logging.info("logged in")

        time.sleep(5)