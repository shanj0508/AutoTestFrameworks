'''
    工具类：底层逻辑代码层
    Selenium关键字驱动类：常用操作行为给封装为各类关键字。
        将常用的自行封装到自定义类中，在使用时，直接调用自定义封装的类即可。
        1. 创建webdriver
        2. 访问url
        3. 定位元素
        4. click
        5. sendkeys
        6. webdriverWait
        7. quit
        8. 相对定位器
        ......
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from ui_test_frame_excel_driver.conf.chrome_options import ChromeOptions

# 基于type_值决定生成的driver对象是什么类型
def open_browser(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=ChromeOptions().options())
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            print("Exception Information:" + str(e))
            driver = webdriver.Chrome()
    return driver


class WebKey:

    # 构造函数
    def __init__(self, type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, content):
        self.driver.get(content)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击操作
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, content):
        self.locate(name, value).send_keys(content)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(name, value), message='元素查找失败')

    # 强制等待
    def wait(self, content):
        sleep(int(content))

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

    # 句柄的切换（考虑不同场景的不同切换）
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 句柄切换2
    # def switch_handle_1(self, index):
    #     handles = self.driver.window_handles
    #     self.driver.switch_to.window(handles[index])

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, name, value, expect):
        try:
            reality = self.locate(name, value).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False

        # reality = self.locate(name, value).text
        # assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
