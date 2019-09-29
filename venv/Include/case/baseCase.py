# coding=utf-8
import unittest
from util import logs
from util.getDriver import DriverClient
'''
    @describe 所有Case父类
    @auther zw
    @time 2019-08-28
'''
class BaseCase(unittest.TestCase):
    log = None
    driver = None

    def setUp(self):
        # self.log = logs.Logger(self.__class__.__name__).get_logger()
        self.log = logs.Logger("").get_logger()
        self.log.info(self.__class__.__name__ + "------->setUp")

        # 获取driver
        self.driver = DriverClient().getDriver()

    def tearDown(self):
        self.log.info(self.__class__.__name__ + "------->tearDown")