from appium import webdriver
from util import logs
from util import app

'''
    @describe  获取driver
       单例模式实现在多个class之间复用，
       执行完一个类的用例，再次执行下个类的用例时不需要初始化
    @auther zw
    @time 2019-09-12
'''
class Singleton(object):
    driver = None
    log = logs.Logger("GetDriver").get_logger()

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):

            orig = super(Singleton, cls)
            desired_caps = app.DESIRED_CAPS1

            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._instance


class DriverClient(Singleton):
    def getDriver(self):
        self.log.info("Get Driver")
        return self.driver