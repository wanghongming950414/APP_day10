from Base.base import Base
from Page.all_page_elements import PageElements


class LoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def send_login(self, name, pwd):
        self.send_element(PageElements.send_account_id, name)
        self.send_element(PageElements.send_password_id, pwd)
        self.click_element(PageElements.login_ptn_id)

    def login_close_page(self):
        self.click_element(PageElements.close_page_btn_id)

    def if_login_btn(self):
        """判断登录按钮是否存在"""
        self.get_element(PageElements.login_ptn_id)
