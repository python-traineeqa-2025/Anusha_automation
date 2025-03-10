import logging
import time

from page_objects.LoginPom.loginpage import LoginPage
from page_objects.product.productpage import ProductPage
from setup.basetest import BaseTest


class TestProduct(BaseTest):

    def test_product_details(self):
        url=self.cred["base_url"]
        self.driver.get(url)
        logging.info("site opened")

        login_page=LoginPage(self.driver)
        uname = self.cred["standard_username"]
        pwd = self.cred["Password"]
        login_page.login(uname, pwd)
        logging.info("logged in")
        product=ProductPage(self.driver)
        product.description_details()
        logging.info("Product details")
        time.sleep(3)

