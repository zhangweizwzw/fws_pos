from case.baseCase import BaseCase
from page.loginPage import LoginPage
import unittest
from util import app
from time import sleep
'''
    @describe 登录
    @auther zw
    @time 2019-08-28

'''
class Login(BaseCase):

    #验证码登录
    def codeLogin(self, loginPage):
        loginPage.sendK_phone(app.MOBILE)
        loginPage.sendK_password(app.PASSWORD)
        loginPage.login()

    #登录主方法
    def test_login(self):
        #初始化loginpage
        loginPage = LoginPage(self.driver)
        #判断是否需要登录（如果已登录就不需要登录）
        needLogin = loginPage.needLogin()
        if needLogin:
            self.codeLogin(loginPage)




if __name__ == "__main__":
    unittest.main()