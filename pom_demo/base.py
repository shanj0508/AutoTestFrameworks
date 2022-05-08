from selenium import webdriver
import time

"""
    （说话）首先， 创建 key_word.py文件。创建BasePage类作为
    所有Page类的基类，这个基类不是曹操说的那个食之无味，弃之可惜的鸡肋哈。
    这个是pom的核心。我们在BasePage类中封装一些方法，
    这些方法是我们在做自动化时经常用到的。
"""
class BasePage:
    """
    基础page层，封装一些常用方法。
    """

    def __init__(self, driver):
        # 导入一下 webdriver包,方便后面代码编写，写完注释掉
        # self.driver = webdriver.Chrome()
        self.driver = driver



    """
        （说话）
        open（） 方法 用于 打开 网页， 它 接收 一个 url 参数， 
        默认 为 None。 如果 url 参数 为 None， 则 默认 打开 
        子类 中 定义 的 url。 稍后 会在 子类 中 定义 url 变量。
        当然你也可以直接传递Url进去，这样就会打开你传递的url进去。
        这些写就比较灵活了，子类和open方法都可以定义url变量，按照
        你的习惯去写就行了。
    """

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    """
        (说话)接下来我们来重写一下元素定位方法
        我们 知道， Selenium 
        提供 的 元素 定位 方法 很长， 这里 做了 简化， 只是 为了 在 
        子类 中 使用 更加 简便。
    """
    # 元素定位
    def locator(self, name,value):
        return self.driver.find_element(name, value)


    """
        （说话）然后，我们定义一下获取网页标题栏get_title()和获取文本的get_text()方法。 
        这些 方法 是在 写 自动化 测试 时 经常 用到 的 方法， 也可以 定义 在
         BasePage基 类 中。 需要 注意 的 是， get_ text（） 方法 需要 
         接收 元素 定位， 这里使用 XPath 定位来接收。
    """
    # 获取title，获取网页标题栏
    def get_title(self):
        return self.driver.title

    # 获取页面text，获取页面文本，使用xpath定位
    def get_text(self, path):
        return self.locator("xpath",path).text

    """
        （说话）
        当然， 我们 还可以 根据 自己的 需求 封装 更多 
        的 方法 到 BasePage 基类 中。
        比如：执行JavaScript脚本和休眠时间。
    """
    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)

    # 休眠时间
    def sleep(self, sec):
        time.sleep(sec)
