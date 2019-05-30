from Base.base import Base
from Page.all_page_elements import PageElements


class MyPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_result(self):
        return self.get_element(PageElements.my_order_id).text

    def click_setting(self):
        self.click_element(PageElements.setting_btn_id)
