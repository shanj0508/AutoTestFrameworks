'''
    电商首页页面对象
'''
from selenium import webdriver

from ui_test_frame_pom_unittest.key_word.ui_keyword import WebKeys


class IndexPage(WebKeys):
    # url
    url = 'http://39.98.138.157/shopxo/'
    # 页面元素
    search_input = ('name', 'wd')
    search_button = ('id', 'ai-topsearch')

    info = ('link text', '个人中心')

    # 页面业务
    def search(self, txt):
        self.open(self.url)
        self.input(*self.search_input, txt=txt)
        self.click(*self.search_button)

    def userinfo(self):
        self.open(self.url)
        self.click(*self.info)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = IndexPage(driver)
    # ip.search('手机')
    ip.userinfo()
