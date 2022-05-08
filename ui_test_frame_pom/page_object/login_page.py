'''
    商城的登录页面对象：用于执行登录相关行为
'''
from selenium import webdriver

from ui_test_frame_pom_unittest.key_word.ui_keyword import WebKeys


class LoginPage(WebKeys):
    # 页面url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 页面元素
    accounts = ('name', 'accounts')
    password = ('name', 'pwd')
    button = ('xpath', '//button[text()="登录"]')
    login_assert = ('xpath', '//*[text()="退出"]')

    # 页面业务
    def login(self, user, pwd, expect):
        self.open(self.url)
        self.input(*self.accounts, txt=user)
        self.input(*self.password, txt=pwd)
        self.click(*self.button)
        status = self.assert_text(*self.login_assert, expect=expect)
        return status


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('xuzhu666', '123456', '退出')
