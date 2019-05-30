
from Base.base import Base
from Page.all_page_elements import PageElements


class HomePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        self.click_element(PageElements.my_btn_id)
