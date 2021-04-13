# -*- coding:UTF-8 -*-
import copy
import unittest

from common import Globle
from script.interface.channel import channelParam, channelIntf
from script.interface.channel.channelParam import addChannel


class Channel(unittest.TestCase):
    def setUp(self):
        '''可添加一些初始化的东西'''
    def tearDown(self):
        pass
    def testChannel_01(self):
        '''渠道管理--新增'''
        channelParam = copy.deepcopy(addChannel)
        channelParam['channelName'] = '添加渠dd道了'

        res = channelIntf.addChannel(riskDict=channelParam,username=Globle.sqwUser,password=Globle.sqwPass)
        print('dddfdf')
        print(res)
        #self.assertTrue(channelDict.result,'新增失败')
        #查看是否新增成功


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Channel("testChannel_01"))

