
'''
    @describe 常量
    @auther zw
    @time 2019-09-12
'''


'''
    OPPO R15
'''
DESIRED_CAPS1 = {}
DESIRED_CAPS1['platformName'] = 'Android'  # android的apk还是IOS的ipa
DESIRED_CAPS1['platformVersion'] = '8.1.0'  # android系统的版本号
DESIRED_CAPS1['deviceName'] = 'OPPO R15'  # 手机设备名称，通过adb devices  查看
DESIRED_CAPS1['appPackage'] = 'com.service.provider.app'  # apk的包名
DESIRED_CAPS1['appActivity'] = 'com.service.provider.app.ui.login.activity.LauncherActivity'  # apk的launcherActivity

DESIRED_CAPS2 = {}
DESIRED_CAPS2['platformName'] = 'Android'  # android的apk还是IOS的ipa
DESIRED_CAPS2['platformVersion'] = '5.0.2'  # android系统的版本号
DESIRED_CAPS2['deviceName'] = 'Redmi Note 3'  # 手机设备名称，通过adb devices  查看
DESIRED_CAPS2['appPackage'] = 'com.service.provider.app'  # apk的包名
DESIRED_CAPS2['appActivity'] = 'com.service.provider.app.ui.login.activity.LauncherActivity'  # apk的launcherActivity





'''
    登录人信息
'''
MOBILE = "18916606950"
PASSWORD = '888888'

'''
    发送邮件
'''
# 发件人地址
FROM_ADDR = 'zhangwei_7154@163.com'
#收件人地址
TO_ADDR = 'zhangwei_7154@163.com'
# 发送邮箱的服务器地址
MAIL_SERVER = 'smtp.163.com'
# 邮件的标题
SUBJECT = '服务商POS自动化结果测试'
# 发件人的邮箱地址
EM_USERNAME = 'zhangwei_7154@163.com'
EM_PASSWORD = 'zhangwei19940624'