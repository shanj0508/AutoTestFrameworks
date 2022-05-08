#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/16 20:08
# @Author : 展昭
# @File : test_intf.py
import pytest


class Test_Case():
    @classmethod
    def setup_class(cls):
        print("setup_class=========>")
        cls.token = 1111111111111

    def test_case01(self):
        a = self.token
        print(a)

if __name__ == '__main__':
    pytest.main(['-s'])
