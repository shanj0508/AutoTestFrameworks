#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 20:59
# @Author : 展昭
# @File : yaml_driver.py
import yaml

def load_yaml(path):
    file = open(path,'r',encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data