from appium import webdriver


def get_phone_driver(pac, act):
    desired_caps = {}
    # 测试平台
    desired_caps['platformName'] = 'Android'
    # 测试平台系统版本
    desired_caps['platformVersion'] = '5.1'
    # 设备名字
    desired_caps['deviceName'] = '192.168.56.101.5555'
    # app包名
    desired_caps['appPackage'] = pac
    # app启动名
    desired_caps['appActivity'] = act
    # 支持获取toast信息
    desired_caps['automationName'] = 'Uiautomator2'

    # 支持中文输入
    # desired_caps['unicodeKeyboard'] = True  # 重置手机键盘
    # desired_caps['resetKeyboard'] = True  # uncode 编码格式

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
