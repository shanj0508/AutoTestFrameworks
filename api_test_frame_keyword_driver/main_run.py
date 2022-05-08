#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 21:17
# @Author : 展昭
# @File : main_run.py
import os

import pytest


def run():
    # 指定执行文件
    pytest.main(['-v','./excel_case/test_case06.py',
                 '--alluredir', './result','--clean-alluredir'])
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')

if __name__ == '__main__':
    run()