#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 21:31
# @Author : 展昭
# @File : conftest.py
from random import random

import allure
import pytest

from class46.pytest_intf_auto.api_keyword.api_key import ApiKey
from class46.pytest_intf_auto.params.allParams import *


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

#项目级fix，整个项目只初始化一次
@pytest.fixture(scope='session')
def token_fix():
    # 初始化工具类
    ak = ApiKey()
    with allure.step("发送登陆接口请求，并生成token，整个项目仅生成一次"):
        # 定义访问链接‘
        # url = 'http://39.98.138.157:5000/api/login'
        url = URL + PORT + '/api/login'
        # 定义请求用户数据
        userInfo = {
            'username': 'admin',
            'password': '123456'
        }
        # 发送post请求
        res = ak.post(url=url,json = userInfo)
        # 获取token
        token = ak.get_text(res.text,'token')
        # 验证代码，验证token只生成一次
        token_random = random()
        return ak,token,res,token_random
