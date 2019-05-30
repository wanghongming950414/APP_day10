import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, poll_frequency=1.0):
        return self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=30, poll_frequency=1.0):
        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def scroll_sreen(self, sc):
        """
        滑动页面
        :param sc: 1:向上  2:向下 3:向左  4:向右
        :return:
        """
        time.sleep(2)
        phone_size = self.driver.get_window_size()
        width = phone_size.get("width")
        height = phone_size.get("height")
        if sc == 1:
            """向上滑动"""
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, duration=2000)
        if sc == 2:
            """向下滑动"""
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, duration=2000)
        if sc == 3:
            """向左滑动"""
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, duration=2000)
        if sc == 4:
            """向右滑动"""
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, duration=2000)

    def screen_page(self, name="截图"):
        """

        :param name:
        :return:
        """
        # 定义图片的名字
        png_name = "./image" + os.sep + "{}.png".format(int(time.time()))
        # 截图
        self.driver.get_screenshot_as_file(png_name)
        # 二进制打开文件
        # 使用添加附件,添加到allure
        with open(png_name, "rb", encoding="utf-8") as f:
            allure.attach("截图的名字", f.read(), allure.attach_type.PNG)

    def get_toast(self, toast):
        """
        获取toast消息
        :param toast: 拼接xpath的toast内容
        :return: 返回获取到的toast
        """
        # 找toast
        toast_xpath = (By.XPATH, "//*[contains(@text, '{}')]".format(toast))
        # 找元素
        data = self.get_element(toast_xpath).text
        # 返回toast
        return data
