import pytest
from time import sleep
from selenium import webdriver
from pom_v3.baidu_page import BaiduPage
from pom_v3.data_driver import yaml_driver

class TestBaidu():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
    """
        1.因为这3个用例的步骤是一摸一样的，
        因此我们可以使用数据驱动来简化代码
        将3个用例减少1个，搭配数据驱动仍可
        执行3次
        2.需要数据的测试用例: 数据驱动可以直接传递数值
        也可以像下面这个方法一样通过函数的形式将结果生成并返回。
    """
    @pytest.mark.parametrize('data', yaml_driver.load_yaml('./data/baidu.yaml'))
    def test_baidu_search_case1(self,data):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input(data["txt"])
        page.search_button()
        sleep(2)
        assert page.get_title() == data["txt"] + "_百度搜索"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','test_param.py'])