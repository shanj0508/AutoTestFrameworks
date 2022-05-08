import os
from time import sleep
import pytest
from selenium import webdriver

# @pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='session')
@pytest.fixture(scope='function')
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    # 使用编写的脚本开启浏览器debug模式,调试时可注释
    os.popen("D:/github/AutoTestFrameworks/ui_frame_pom_v2_demo/chrome.bat")
    # 实践证明，不可用。。
    # os.system(r'chrome.exe --remote-debugging-port=9222')
    sleep(3)
    print("成功打开浏览器")
    # 复用已有浏览器，方便调试
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)

    # 隐式等待10秒
    driver.implicitly_wait(10)
    # 用例执行，返回driver
    yield driver
    # 用例后置，关闭浏览器
    # driver.quit()
    # driver.close()
    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')
    print("test end!")