# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.baidu.com")

driver.find_element('id', 'kw').send_keys("python")
driver.find_element('id', 'su').click()
sleep(5)

driver.find_element('xpath', '//*[@id="7"]/div/div/h3/a').click()
print(driver.title)
# 切换句柄
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
sleep(5)
print(driver.title)
# driver.close()
driver.switch_to.window(handles[0])
print(driver.title)

# 鼠标悬停
el = driver.find_element('xpath', '//*[@id="u"]/a[2]')
# 创建一个actions对象，进行悬停的操作
actions = ActionChains(driver)
actions.move_to_element(el).perform()

driver.find_element('link text', '搜索设置').click()
driver.save_screenshot('./img/1.png')
# driver.quit()

# # 1、创建Chrome实例 。
# driver = webdriver.Chrome()
# # 2、driver.get方法将定位在给定的URL的网页 。
# driver.get("https://www.baidu.com/")  # get接受url可以是如何网址，此处以百度为例
# # 3、定位元素 。
# # 3.1、用id定位输入框对象，
# driver.find_element_by_id("kw").send_keys("python")
# # 3.2、用id定位点击对象，用click()触发点击事件
# driver.find_element_by_id('su').click()
# time.sleep(3)  # 延迟3秒
# # 4、退出访问的实例网站。
# driver.close()
