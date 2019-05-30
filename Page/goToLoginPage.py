from Base.base import Base
from Page.all_page_elements import PageElements


class GoToLoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_go_to_login(self):
        self.click_element(PageElements.go_to_login_xpash)
