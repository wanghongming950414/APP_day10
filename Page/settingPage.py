from Base.base import Base
from Page.all_page_elements import PageElements


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_out_btn(self, tag=1):
        self.scroll_sreen(1)
        self.click_element(PageElements.out_btn_id)
        if int(tag) == 1:
            self.click_element(PageElements.really_out_btn_id)
        else:
            self.click_element(PageElements.dis_out_btn_id)
