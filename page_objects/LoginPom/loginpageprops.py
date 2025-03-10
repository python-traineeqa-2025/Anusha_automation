
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.LoginPom.loginpagelocator import LoginPageLocators


class LoginPageProperties(LoginPageLocators):

    @property
    def username_input(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME)

    @property
    def password_input(self):

        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    @property
    def button_click(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN)




























# from page_objects.LoginPom.loginpagelocator import LoginPageLocators
#
#
# class LoginPageProperties(LoginPageLocators):
#
#
#     @property
#     def username_input(self):
#         return self.driver.find_element(*LoginPageLocators.USERNAME)
#     @property
#     def password_input(self):
#         return self.driver.find_element(*LoginPageLocators.PASSWORD)
#
#     @property
#     def button_click(self):
#         return self.driver.find_element(*LoginPageLocators.LOGIN)
