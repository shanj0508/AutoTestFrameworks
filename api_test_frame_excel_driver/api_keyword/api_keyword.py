# encoding=utf-8
"""
    这是接口测试的关键字驱动类，用于提供接口自动化测试的关键字方法。
    常用关键字方法包括：
        1.各种模拟请求方法：post/get/put/delete/header/.....
        2.设置入参的默认值的时候，设置的参数必须放到最后
"""
import json

import jsonpath
import requests


class ApiKey:
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url=url, data=data, json=json, **kwargs)

    def get_text(self, response_data, key):
        data = json.loads(response_data)
        value = jsonpath.jsonpath(data, "$..{0}".format(key))
        return value[0]


if __name__ == '__main__':
    ak = ApiKey()
    r = ak.get("http://www.baidu.com")
    print(r.text)
    print(r.status_code)
