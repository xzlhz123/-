import json
import unittest

import requests

from common import Globle
from ddt import ddt,data,file_data,unpack

class mytest(unittest.TestCase):
    def setUp(self):
        '获取测试接口的url'
    url = Globle.url

    @file_data('D:\\workplace\\InterfaceTest_master\\script\\interface\\test.json')
    def test_login(self,data):
        body = json.dumps(eval(data[0]))
        print(body)
        status = data[1]
        #re = requests.post()
if __name__ == '__main':
    unittest.main()
    mytest().test_login()

