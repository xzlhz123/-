import json
import urllib

import paramunittest as paramunittest

from common.configHttp import RunMain
from common.readExcel import readExcel
from testcase import geturlParams
import unittest

'调用刚才拼接的url'
url = geturlParams.geturlParams().get_Url('login')

login_xls = readExcel().get_xls('userCase.xlsx','login')
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,Num,title,case_name,path,query,method):
        """"
        set params
        :param case_name
        :param path
        :param inParam
        :param method
        :return:
        """
        self.title = title
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
#      self.outParam = outParam
        self.Num = Num
    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return
        """
        print(self.case_name+"测试开始前准备")
    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        print('66')
        print(self.query)
        #url1 = "http://localhost:8080/login?"
        new_url = url + self.query
        print('new_url')
        print(new_url)

       # '将一个完整的url中的name=&pwd= 转换为{'name':'xxx','pwd':'xxx'}'
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        print(url)
        print(data1)
        print('0000')
        #根据EXCEL中的method调用run_main来进行request请求，并拿到响应
        info = RunMain().run_main(self.method,url,data1)
        #将响应转换为字典格式
        ss = json.loads(info)
        #如果case_name 是login,说明合法，返回的code应该是200
        if self.case_name == 'login':
            self.assertEqual(ss['code'],200)
        # 如果case_name 是login_error说明合法，返回的code应该是401
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],401)
        # 如果case_name 是login_null说明合法，返回的code应该是404
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],404)

if __name__ == '__main':
    testUserLogin.checkResult()





















