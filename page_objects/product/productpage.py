import logging

from page_objects.product.productprop import ProductPageProperties


class ProductPage(ProductPageProperties):
    def __init__(self,driver):
        self.driver =driver


    def description_details(self):
        product= self.product
        product.click()
        description=self.description
        logging.info(f"Product description: {description.text}")
        price = self.price
        logging.info(f"Product price: {price.text}")







