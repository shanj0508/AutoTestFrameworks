#先从base文件导入基类。
from pom_v3.base import BasePage

"""
   创建baidu_page.py文件用来存储百度搜索页面。
"""
"""百度Page层，百度页面封装操作到的元素"""
#创建BaiduPage类继承BasePage类
class BaiduPage(BasePage):
    #定义url变量，供父类中的open()方法使用
    url = "https://www.baidu.com"

    # 文本定位，并输入
    def search_input(self, search_key):
        #使用父类的locator方法来定位元素
        #比原生的Selenium方法简短一些
        # self.locator("id", "kw").send_keys(search_key)
        self.locator("xpath", "//input[@name='wd']").send_keys(search_key)

    # 按钮定位，并点击
    def search_button(self):
        self.locator("id","su").click()

