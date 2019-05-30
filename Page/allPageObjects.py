from Page.settingPage import SettingPage
from Page.goToLoginPage import GoToLoginPage
from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.myPage import MyPage

class AllPageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def get_go_to_login_page(self):
        return GoToLoginPage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_my_page(self):
        return MyPage(self.driver)

    def setting_page(self):
        return SettingPage(self.driver)