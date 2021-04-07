# -*- coding: UTF-8 -*-
import json
from common.configHttp import RunMain

#获取登录返回值
url = 'http://qw.mkt.test.robotabc.com.cn/uaa/login?'

result1 = RunMain().run_main('post', 'http://qw.mkt.test.robotabc.com.cn/uaa/login', {'username': '18458163205' ,'password' :'lhz123456' ,'isAgree' :1,'loginType' :'WORK_WX_WEB'})
print(result1)
#获取token
access_token = json.loads(result1)['access_token']
print(access_token)

#定义header中的
headers = {
    'platform': 'PC',
    'wx-data-source': 'QW',
    'Content-Type': 'application/json',
    'v': '2.0.0',
    'token': access_token
}
