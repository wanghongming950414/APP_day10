import sys, os

import pytest

sys.path.append(os.getcwd())

from Base.getfiledata import GetFileData

from Page.allPageObjects import AllPageObjects
from Base.getDriver import get_phone_driver
from selenium.common.exceptions import TimeoutException


def get_login_data():
    # 预期成功的数据列表
    suc_list = []
    # 预期失败的数据列表
    fail_list = []
    # 调用ymal文件
    login_data = GetFileData().get_yaml_data("logindata.yml")
    for i in login_data:
        if login_data.get(i).get("toast"):
            # 预期失败测试用例 case_num, account, passwd, exp_data
            fail_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd"),
                              login_data.get(i).get("toast"), login_data.get(i).get("expect_data")))
        else:
            suc_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}
    # return (suc_list)
    # return (fail_list)


# print(get_login_data())

class TestLogin:

    def setup_class(self):
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")

        self.all_page = AllPageObjects(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in(self):
        # 点击首页"我"
        self.all_page.get_home_page().click_my_btn()
        """点击去登录页面的,已有账号去登录"""
        self.all_page.get_go_to_login_page().click_go_to_login()

    @pytest.mark.parametrize("case_num, account, passwd, expect_data", get_login_data().get("suc"))
    def test_login_suc(self, case_num, account, passwd, expect_data):
        """

        :param case_num: 用例编号
        :param account:用户名
        :param passwd: 密码
        :param exp_data: 预期结果
        :return:
        """

        # # 点击首页"我"
        # self.all_page.get_home_page().click_my_btn()
        # """点击去登录页面的,已有账号去登录"""
        # self.all_page.get_go_to_login_page().click_go_to_login()
        """输入账号   密码"""
        self.all_page.get_login_page().send_login(account, passwd)

        try:
            # 获取我的订单
            my_order = self.all_page.get_my_page().get_result()
            try:
                assert expect_data == my_order
            except AssertionError:
                """停留在个人中心,需要执行退出操作"""
                # 截图
                self.all_page.get_login_page().screen_page()
                assert False
            finally:
                # 点击设置
                self.all_page.get_my_page().click_setting()
                # 退出操作
                self.all_page.setting_page().click_out_btn()
        except TimeoutException:
            # 截图
            self.all_page.get_login_page().screen_page()
            # 关闭页面
            self.all_page.get_login_page().login_close_page()
            assert False

    @pytest.mark.parametrize("case_num, account, passwd, toast, expect_data", get_login_data().get("fail"))
    def test_login_fail(self, case_num, account, passwd, toast, expect_data):
        """

         :param case_num: 用例编号
        :param account:用户名
        :param passwd: 密码
        :param toast:  获取的toast信息
        :param exp_data: 预期结果
        :return:
        """
        # 点击首页"我"
        # self.all_page.get_home_page().click_my_btn()
        # """点击去登录页面的,已有账号去登录"""
        # self.all_page.get_go_to_login_page().click_go_to_login()
        """输入账号   密码"""
        self.all_page.get_login_page().send_login(account, passwd)
        try:
            # 获取toast消息
            toast_data = self.all_page.get_login_page().get_toast(toast)
            try:
                """登录页面操作"""
                # 判断登录按钮
                self.all_page.get_login_page().if_login_btn()
                # 断言
                assert toast_data == expect_data
                # 关闭登录页面
                self.all_page.get_login_page().login_close_page()
            except TimeoutException:
                """获取到toast消息错误提示,但登录成功,进入个人中心页面"""
                # 截图
                self.all_page.get_login_page().screen_page()
                # 点击设置
                self.all_page.get_my_page().click_setting()
                # 点击退出按钮
                self.all_page.setting_page().click_out_btn()
                assert False
            except AssertionError:
                """登录页面"""
                # 截图
                self.all_page.get_login_page().screen_page()
                # 关闭登录按钮
                self.all_page.get_login_page().login_close_page()
                assert False
        except TimeoutException:
            # 找不到toast
            # 截图
            self.all_page.get_login_page().screen_page()
            try:
                """登录页面"""
                # 登录按钮
                self.all_page.get_login_page().if_login_btn()
                # 关闭登录页面
                self.all_page.get_login_page().login_close_page()
            except TimeoutException:
                """个人中心页面"""
                # 点击设置
                self.all_page.get_my_page().click_setting()
                # 退出操作
                self.all_page.setting_page().click_out_btn()
            assert False
