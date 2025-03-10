from page_objects.product.productpagelocators import ProductLocators


class ProductPageProperties(ProductLocators):

    @property
    def product(self):
        return self.driver.find_element(*ProductLocators.PRODUCT)

    @property
    def description(self):
        return self.driver.find_element(*ProductLocators.DESCRIPTION)

    @property
    def price(self):
        return self.driver.find_element(*ProductLocators.PRICE)

