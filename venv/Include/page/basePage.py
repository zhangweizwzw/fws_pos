from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import logs
'''
    @describe 所有page页面父类
    @auther zw
    @time 2019-08-27
'''
class BasePage(object):
    log = None
    #初始化
    def __init__(self, driver):
        self.driver = driver
        # self.log = logs.Logger(self.__class__.__name__).get_logger()
        self.log = logs.Logger("").get_logger()

    #元素是否存在
    def isElementExists(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return True
        except Exception:
            self.log.info("未能找到 %s 元素" % "".join(str(loc)))
            return False

    #查找元素
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception:
            self.log.info("".join(loc))
            self.log.info("未找到 s% 元素" % "".join(str(loc)))

    # 查找多个
    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception:
            self.log.info("未找到 s% 元素" % "".join(str(loc)))



    # 重写定义send_keys方法
    def send_keys(self, vaule, *loc, clear_first=True):
        try:
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
            else:
                self.find_element(*loc).clear()

        except AttributeError:
            self.log.info("未能找到 %s 元素" % "".join(str(loc)))

    # 重写定义点击元素
    def click_element(self, *loc):
        try:
            self.find_element(*loc).click()
        except:
            self.log.info("未能找到 %s 元素" % "".join(str(loc)))

    # 重写定义获取text
    def get_text(self, *loc):
        try:
            return self.find_element(*loc).text
        except Exception:
            self.log.info("未能找到 %s 元素" % "".join(str(loc)))



