'''
    web端的关键字驱动类：
        结构中属于逻辑代码层，主要的目的是作为一个工具类的角色，
        在需要用到这些工具时，通过这个类来实现
        大型超市——购买工具箱——动用工具
        Selenium——关键字——web自动化
        工具箱一般包含有需要的常规操作行为：
            输入、点击、启动、、、、、、
'''

# 开始去超市购物
from time import sleep

from selenium import webdriver


# 定义工具类
from selenium.webdriver import ActionChains


class WebKeys:

    def __init__(self, driver):
        # 导入一下 webdriver包,方便后面代码编写，写完注释掉
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 访问URL
    def open(self, url):
        self.driver.get(url)

    # 退出
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, name,value):
        return self.driver.find_element(name, value)

    # 元素定位，传参List
    def locator_list(self, list):
        el = self.driver.find_element(list[0], list[1])
        # 将定位的地方框出来
        self.locator_station(el)
        # return self.driver.find_element(list[0], list[1])
        return el

    # 组元素定位，传参List
    def locator_list_group(self, list):
        return self.driver.find_elements(list[0], list[1])

    # 输入
    def input(self, name,value,txt):
        el = self.locator(name,value)
        el.clear()
        el.send_keys(txt)

    # 强制等待
    def wait(self, time_):
        sleep(time_)

    # 获取title，获取网页标题栏
    def get_title(self):
        return self.driver.title

    # 获取页面text，获取页面文本，使用xpath定位
    def get_text(self, path):
        return self.locator("xpath",path).text

    # 显示定位的地方，确定定位问题
    def locator_station(self,element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid green;"  # 边框border:2px; red红色
        )

    # 窗口切换
    def change_window(self,n):
        # 获取句柄
        handles = self.driver.window_handles
        # 切换到原始页面,n = 0
        # 切换句柄到第二个页面,n = 1 ,以此类推
        self.driver.switch_to.window(handles[n])
        print(self.driver.title)

    # 关闭当前窗口
    def close_window(self):
        self.driver.close()

    # 鼠标点击并悬停
    def mouse_hold(self,url):
        btn = self.driver.find_elements_by_xpath(url)[0]
        action = ActionChains(self.driver)
        action.click_and_hold(btn).perform()

    # 切换frame
    def change_frame(self,a):
        self.driver.switch_to.frame(a)

    # 切换回主框架
    def change_defaultFrame(self):
        self.driver.switch_to.default_content()