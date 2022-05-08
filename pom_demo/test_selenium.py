import pytest
from selenium import webdriver
from time import sleep

class Test_Selenium():
    """
    （说话）
    通过setup_class和teardown_class，
    让下面执行的3个用例，只启动和关闭一次浏览器，
    减少资源消耗
    """

    # 环境准备
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_case01(self):
        self.driver.get("http://www.baidu.com")
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys('狗狗币')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        assert self.driver.title == "狗狗币_百度搜索"

    def test_baidu_case02(self):
        self.driver.get("http://www.baidu.com")
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        assert self.driver.title == "selenium_百度搜索"

    def test_baidu_case03(self):
        self.driver.get("http://www.baidu.com")
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys('pytest')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        assert self.driver.title == "pytest_百度搜索"

    # 环境清理
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','test_selenium.py'])