

from page_objects.LoginPom.loginpageprops import LoginPageProperties


class LoginPage(LoginPageProperties):

    def __init__(self,driver):
        self.driver=driver



    def login(self, username, pwd):
        uname= self.username_input

        uname.click()
        # self.wait.until()
        uname.send_keys(username)
        password=self.password_input
        password.click()
        password.send_keys(pwd)
        submit=self.button_click
        submit.click()
