import unittest
from case.login import Login
from case.selectStation import SelectStation
from util.HTMLTestRunner import HTMLTestRunner
import time
from util.sendEmail import SendEmail

'''
    @describe TestSuite 用例执行
    @auther zw
    @time 2019-09-15
'''

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login"))
    suite.addTest(SelectStation("test_selectStation"))


    #保存执行结果到report目录
    report_name = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())+"_result.html"
    reportAddress = "../report/"+report_name
    fileReport = open(reportAddress, "wb")
    runner = HTMLTestRunner(stream=fileReport, title='服务商POS测试报告', description='用例执行情况：')
    runner.run(suite)
    fileReport.close()

    #发送测试报告邮件
    # SendEmail.send_email(reportAddress)