# -*- coding: utf-8 -*-
import requests
import unittest


class ApiDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokenId = None
        cls.url = "http://172.16.6.240"

    def test_01_getUrl(self):
        path = "/eap/"
        url = self.url + path
        # 发送一个get请求
        r = requests.get(url=url)
        self.assertEqual(r.status_code, 200, msg="断言失败")

    def test_02_doLogin(self):
        path = "/eap/doLogin.action"
        url = self.url + path
        # 发送一个post请求 data=None, json=None, **kwargs
        data = {
            "loginName": "admin",
            "loginPassword": "T2EApv2gAJl3AqrcDwMbIZV0lqjwyp9w1/2IwaJHr5EdRt58sL762uAYuACfVZImoPT9gyGT+F+SGe0FsnPPa5ckdVGceKilsFM1CnWtWioZvOwhjERuwisZr78PV0cwg1bwo9P09dpmRRmU3jSgvjpYZyXVbbfZnBOuUzOK4WI="
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

        r = requests.post(url=url, data=data, headers=headers)
        # print(r.text)
        # print(type(r.json()))
        self.assertEqual(r.json()["success"], True, msg="断言失败")
        ApiDemo.tokenId = r.json()["root"]["datas"][0]["tokenId"]

    def test_03_getUserList(self):
        path = "/eap/eobs/user/userData.action"
        url = self.url + path
        data = {
            "limit": 20,
            "start": 0
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "tokenId": self.tokenId
        }
        r = requests.post(url=url, data=data, headers=headers)
        self.assertEqual(r.status_code, 200, "断言失败")


if __name__ == '__main__':
    unittest.main()
