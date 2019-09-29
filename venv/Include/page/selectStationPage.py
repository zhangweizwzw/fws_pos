from page.basePage import BasePage
from selenium.webdriver.common.by import By

'''
    @describe 选择油站page
    @auther zw
    @time  2019-09-16
'''

class SelectStationPage(BasePage):
    # 切换站点按钮
    changeStation_loc = (By.ID, 'com.service.provider.app:id/tv_change_station')

    #选择油站框--判断选择油站框是否存在
    isSelect_loc = (By.ID, 'com.service.provider.app:id/tv_title')

    #选择的油站
    stations_loc = (By.ID, 'com.service.provider.app:id/rl_view')
    # station_loc = (By.ID, 'com.service.provider.app:id/rl_view')

    #确定按钮
    submit_loc = (By.ID, 'com.service.provider.app:id/btn_submit')

    # 首页扫码加油图标-判断是否需要登录
    needLogin_loc = (By.ID, 'com.service.provider.app:id/btn_add_oil')

    # 对账页面
    duizhang_loc = (By.ID, 'com.service.provider.app:id/bottom_menu_button2')

    # 点击对账
    def duizhang_click(self):
        self.click_element(self.duizhang_loc)

    # 加油按钮是否存在
    def isAddOil(self):
        return self.isElementExists(*self.needLogin_loc)


    # 切换油站按钮
    def changeStation_click(self):
        self.click_element(self.changeStation_loc)

    #判断是否弹出油站选择框
    def isSelect(self):
        select = self.isElementExists(self.isSelect_loc)
        return select

    #点击确定按钮
    def submit_click(self):
        self.click_element(self.submit_loc)

    # #选择油站
    # def selectStation(self):
    #     self.find_elements(self.stations_loc)[0].click()


