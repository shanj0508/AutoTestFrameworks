#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/16 21:54
# @Author : 展昭
# @File : test_case06.py
import allure
import pytest

from class46.pytest_intf_auto_V2.data_driver import yaml_driver
from  class46.pytest_intf_auto_V2.logic.shopingApi import ApiCase
"""
    尽量简化用例内容，方便管理用例，以及进行模块划分
"""
@allure.epic("shopXo电商平台接口-接口测试")
class TestTree():
    #初始化用例库
    action1 = ApiCase()

    @allure.feature("01.登陆")
    @allure.story("02.一般场景")
    @pytest.mark.parametrize('userData', yaml_driver.load_yaml('./data/user.yaml'))
    def test_case01(self,userData):
        self.action1.params_login(userData)

    @allure.feature("02.个人查询")
    @allure.story("01.典型场景")
    @allure.title("个人查询")
    def test_case02(self,token_fix):
        self.action1.getuserinfo(token_fix)

    @allure.feature("03.添加商品到购物车")
    @allure.story("01.典型场景")
    @allure.title("添加商品到购物车")
    def test_case03(self,token_fix):
        self.action1.addcart(token_fix)

    @allure.feature("04.下单")
    @allure.story("01.典型场景")
    @allure.title("下单")
    def test_case04(self,token_fix):
        self.action1.createorder(token_fix)