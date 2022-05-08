import pytest
from time import sleep
from selenium import webdriver
from pom_v3.baidu_page import BaiduPage



class TestBaidu():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        """
            (说话)
            使用BaiduPage基类及它所继承的父类中的方法
            当需要用到哪个Page类时，
            只需要将它传入浏览器驱动，
            就可以使用该类中提供的方法了。
        """
        page = BaiduPage(self.driver)
        """
            （说话）
            因为前面封装了元素的定位，
            所以在编写测试用例时会方便不少
        """
        page.open()
        page.search_input("狗狗币")
        page.search_button()
        sleep(2)
        assert page.get_title() == "狗狗币_百度搜索"

    def test_baidu_search_case2(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        assert page.get_title() == "selenium_百度搜索"

    def test_baidu_search_case3(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("pytest")
        page.search_button()
        sleep(2)
        assert page.get_title() == "pytest_百度搜索"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','test_baidu.py'])