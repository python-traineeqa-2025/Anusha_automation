from selenium.webdriver.common.by import By


class ProductLocators(object):
    PRODUCT=(By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']")
    DESCRIPTION=(By.XPATH, "//div[@class='inventory_details_desc large_size']")
    PRICE=(By.XPATH, "//div[@class='inventory_details_price']")



