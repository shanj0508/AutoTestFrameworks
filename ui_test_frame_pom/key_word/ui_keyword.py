'''
    POM中的基类，类似于关键字驱动类
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait


class WebKeys:
    # 创建临时driver
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击操作
    def click(self, name, value):
        self.locate(name, value).click()

    # def click(self, loc):
    #     self.locate(*loc).click()

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(name, value), message='元素查找失败')

    # 强制等待
    def wait(self, time_):
        sleep(int(time_))

    # 切换Iframe
    '''
        传入一个参数：可以是id，name，webelement
    '''

    def switch_frame(self, value, name=None):
        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(name, value))

    # 切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 相对定位器
    # def locator_with(self, method, value, el_name, el_value, direction):
    #     el = self.locate(el_name, el_value)
    #     direction_dict = {
    #         'left': 'to_left_of',  # 左侧
    #         'right': 'to_right_of',  # 右侧
    #         'above': 'above',  # 上方
    #         'below': 'below',  # 下方
    #         'near': 'near'  # 靠近
    #     }
    #     if isinstance(method, str):
    #         method_dict = {
    #             "id": By.ID,
    #             "xpath": By.XPATH,
    #             "link text": By.LINK_TEXT,
    #             "partial link text": By.PARTIAL_LINK_TEXT,
    #             "name": By.NAME,
    #             "tag name": By.TAG_NAME,
    #             "class name": By.CLASS_NAME,
    #             "css selector": By.CSS_SELECTOR
    #         }
    #         self.locate(locate_with(By.TAG_NAME, 'input').to_left_of(el))
    #         return self.driver.find_element(getattr(
    #             locate_with(method_dict.get(method), value), direction_dict.get(direction))(el))

    # 句柄的切换（考虑不同场景的不同切换）
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, name, value, expect):
        try:
            reality = self.locate(name, value).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False

    # 获取指定元素的文本
    def get_text(self, name, value):
        return self.locate(name, value).text
