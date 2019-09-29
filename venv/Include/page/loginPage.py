from page.basePage import BasePage
from selenium.webdriver.common.by import By
'''
    @describe 登录page
    @auther zw
    @time  2019-08-28
'''
class LoginPage(BasePage):
    #短信登录
    messageType_loc = (By.ID, 'com.service.provider.app:id/tv_sms_login_title')

    #密码登录
    passwordType_loc = (By.ID, 'com.service.provider.app:id/tv_psw_login_title')

    #手机号
    phone_loc = (By.ID, 'com.service.provider.app:id/phone')

    #验证码/密码
    password_loc = (By.ID, 'com.service.provider.app:id/verify_code')

    #发送验证码
    sendMessage_loc = (By.ID, 'com.service.provider.app:id/obtain_verify_code')

    #登录
    login_loc = (By.ID, 'com.service.provider.app:id/verify_login')

    #服务协议
    protocol_loc = (By.ID, 'com.service.provider.app:id/bottom_layout')

    #首页扫码加油图标-判断是否需要登录
    needLogin_loc = (By.ID, 'com.service.provider.app:id/btn_add_oil')

    #判断是否需要登录
    def needLogin(self):
        need = self.isElementExists(*self.needLogin_loc)
        if need:
            self.log.info("不需要登录")
            return False
        else:
            self.log.info("需要登录")
            return True

    #点击验证码登录
    def click_messageType(self):
        self.click_element(*self.messageType_loc)

    # 点击密码登录
    def click_passwordType(self):
        self.click_element(*self.password_loc)

    #输入手机号
    def sendK_phone(self, phone):
        self.send_keys(phone, *self.phone_loc)

    #输入验证码/密码
    def sendK_password(self, password):
        self.send_keys(password, *self.password_loc)

    #获取验证码
    def click_getCode(self):
        self.click_element(*self.sendMessage_loc)

    #登录
    def login(self):
        self.click_element(*self.login_loc)

    #服务协议
    def click_protocol(self):
        self.click_element(*self.protocol_loc)
