# -*- coding: UTF-8 -*-
import json
from random import random

from pip._internal.utils.misc import enum

from common.configHttp import RunMain

#获取登录返回值
url = 'http://api.mkt.test.robotabc.com.cn/uaa/login?isAgree=1&username=18458163205&loginType=WORK_WX_WEB&password=lhz123456'
header = {
    'platform': 'PC',
    'wx-data-source': 'QW',
    'Content-Type': 'application/json',
    'v': '2.0.0'
}
result1 = RunMain().run_main('post', url, data=None, headers=header)
access_token = json.loads(result1)['access_token']
#定义header中的
headers = {
    'platform': 'PC',
    'wx-data-source': 'QW',
    'Content-Type': 'application/json',
    'v': '2.0.0',
    'token': access_token
}

#数据库IP
sqwIpTest = '10.2.1.105'

#测试数据库用户名
sqwUserNameTest = 'java'

#测试数据库密码
sqwPasswordTest = 'Sl@mysql!2020@java'
#测试数据库名称
sqwDbInstance01 = 'dg_mobile'
sqwDbInstance02 = 'dg_mkt'
sqwDbInstance03 = 'dg_crm'

#测试环境登录用户名
sqwUser = '18458163205'
#测试环境登录密码
sqwPass = 'lhz123456'

LogLevel = enum(INFO=0,DEBUG=1,ERROR=2,WARN=3)






def createRandomString(length=6):
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(97, 123): # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, length)  # 从list中随机获取6个元素，作为一个片断返回
    random_string = ''.join(myslice) # list to string
    return random_string

class responseClass():
    result = None
    statusLine = None
    text = None
    content = None
