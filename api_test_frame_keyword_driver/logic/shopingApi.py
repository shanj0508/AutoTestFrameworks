#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 20:43
# @Author : 展昭
# @File : test_case01.py
import allure
import pytest

from class46.pytest_intf_auto_V2.api_keyword.api_key import ApiKey
from class46.pytest_intf_auto_V2.data_driver import yaml_driver
from class46.pytest_intf_auto_V2.params.allParams import *


class ApiCase():
    def params_login(self, userData):
        # 动态获取参数生成标题
        allure.dynamic.title(userData['title'])
        # 初始化工具类
        ak = ApiKey()
        # 定义接口url
        url = URL + PORT + '/api/login'
        # 定义请求参数
        userInfo = {
            'username': userData['user']['username'],
            'password': userData['user']['password']
        }
        res = ak.post(url=url, json=userInfo)
        with allure.step("接口返回信息校验及打印"):
            print("/api/login登陆请求响应信息")
            print(res.text)
            # 获取响应中的结果，用于校验是否成功
            msg = ak.get_text(res.text, 'msg')
            print(msg)
            assert msg == userData['msg']


    def getuserinfo(self,token_fix):
        # 从fix中获取预置的工具类和token
        # 所有返回都要获取，不然会报错
        ak,token,res,token_random01 = token_fix
        with allure.step("发送个人查询接口请求"):
            url = url = URL + PORT + '/api/getuserinfo'
            headers = {
                'token': token
            }
            res1 = ak.get(url=url, headers=headers)
        with allure.step("接口返回信息校验及打印"):
            print("/api/getuserinfo个人查询请求响应信息")
            print(res1.text)
            print("验证的random值，测试用")
            print(token_random01)
            name = ak.get_text(res1.text, 'nikename')
            assert "风清扬" == name
        return res1

    def addcart(self,token_fix):
        # 从fix中获取预置的工具类和token
        # 所有返回都要获取，不然会报错
        ak,token,res,token_random01 = token_fix
        with allure.step("调用getuserinfo接口获取返回信息"):
            res1 = self.getuserinfo(token_fix)
        with allure.step("发送添加商品到购物车请求"):
            # 添加商品到购物车,基于token、userid、openid、productid
            # url = 'http://39.98.138.157:5000/api/addcart'
            url = URL + PORT + '/api/addcart'
            hd = {
                "token": token
            }
            data = {
                "userid": ak.get_text(res1.text,'userid'),
                "openid": ak.get_text(res1.text,'openid'),
                "productid": 8888
            }
            # 发送请求
            res2 = ak.post(url=url, headers=hd, json=data)
        with allure.step("接口返回信息校验及打印"):
            print("/api/addcart添加商品到购物车请求响应信息")
            print(res2.text)
            print("验证的random值，测试用")
            print(token_random01)
            result = ak.get_text(res2.text,'result')
            assert 'success' == result
        return res2

    def createorder(self,token_fix):
        # 从fix中获取预置的工具类和token
        # 所有返回都要获取，不然会报错
        ak,token,res,token_random01 = token_fix

        with allure.step("调用addcart接口获取返回信息"):
            res_addcart = self.addcart(token_fix)

        with allure.step("发送下单请求"):
            # 购物车下单
            # 定义访问链接
            # url = 'http://39.98.138.157:5000/api/createorder'
            url = URL + PORT + '/api/createorder'
            # 从项目级fix中获取token
            hd = {
                "token": token
            }
            # 从添加商品到购物车接口中，获取userid、openid、cartid
            data = {
                "userid": ak.get_text(res_addcart.text,'userid'),
                "openid": ak.get_text(res_addcart.text,'openid'),
                "productid": 8888,
                "cartid": ak.get_text(res_addcart.text,'cartid')
            }
            # 发送请求
            res_order = ak.post(url=url, headers=hd, json=data)
        with allure.step("接口返回信息校验及打印"):
            print("/api/createorder下单请求响应信息")
            print(res_order.text)
            print("验证的random值，测试用")
            print(token_random01)
            result = ak.get_text(res_order.text,'result')
            assert 'success' == result

if __name__ == '__main__':
    pytest.main(['-s','test_case04.py'])

