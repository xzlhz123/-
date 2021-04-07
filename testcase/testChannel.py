import json
import logging
import urllib

import paramunittest as paramunittest

from common.configHttp import RunMain
from common.ddd import sessionRequest
from common.readExcel import readExcel
from config.Globle import header
from testcase import geturlParams
import unittest
from testcase.geturlParams import geturlParams

'调用刚才拼接的url'

url = geturlParams().get_Url('channel')
login_xls = readExcel().get_xls('userCase.xlsx','channel')
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,Num,title,case_name,path,method,inParam,outParam):
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
        self.inParam = str(inParam)
        self.method = str(method)
        self.outParam = outParam
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
        print(self.case_name+"\n\n测试开始前准备")
    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """

        print('666')
        print(url)
       #'将一个完整的url中的name=&pwd= 转换为{'name':'xxx','pwd':'xxx'}'
        new_url = url +self.inParam
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        print('data1：')
        print(new_url)
        print(self.inParam)
        info = RunMain().run_main(self.method, url, data=None,headers=header)
        ss = json.loads(info)
        # #根据EXCEL中的method调用run_main来进行request请求，并拿到响应
        # data = self.inParam.encode('utf-8')
        # info = RunMain().run_main(self.method, url, data=data)
        # #将响应转换为字典格式
        # ss = json.loads(info)
        #如果case_name 是login,说明合法，返回的code应该是200
        if self.case_name == '正确渠道名称':
            print(ss['code'])
            self.assertEqual(ss['code'],200)
            #logging.info(f"case:添加渠道，渠道名称为空\n请求地址：{url}\t请求方式:{self.method}\n请求正文：{self.inParam}\n响应头：{ss}\n响应正文：{info.text}\n")
        # 如果case_name 是login_error说明合法，返回的code应该是401
        if self.case_name == '渠道名称大于10个字符':
            print(ss['code'])
            self.assertEqual(ss['code'],500)
        # 如果case_name 是login_null说明合法，返回的code应该是404
        else:
            print(ss['code'])
            self.assertEqual(ss['code'],500)

if __name__ == '__main':
    testUserLogin.checkResult()





















