from selenium.webdriver.common.by import By


class PageElements:
    """主菜单页面元素属性"""
    # 定位"我"按钮
    my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")
    """去登陆页面元素属性"""
    # 定位"去登陆"
    go_to_login_xpash = (By.ID, "com.yunmall.lc:id/gotologon")
    close_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """登录页面元素属性"""
    # 定位"账号'输入框
    send_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 定位"密码'输入框
    send_password_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 定位"登录"按钮
    login_ptn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    """我的页面元素属性"""
    # 定位"我的订单"
    my_order_id = (By.ID, "com.yunmall.lc:id/order_txt")
    # 定位"设置"按钮
    setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """设置页面元素属性"""
    # 定位"退出"按钮
    out_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 定位"确认退出"按钮
    really_out_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 定位"取消退出"按钮
    dis_out_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
