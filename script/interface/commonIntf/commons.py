import json

import requests
import self

from common.Globle import sqwPasswordTest,sqwUserNameTest,url,sqwUser,sqwPass
from common.Globle import headers
from common.Log import logger
from common.commonUtil import httpResponseResultDeal
from common.configHttp import RunMain


def check_login(self):
    # if userName is None or passWord is None:
    #     postData = {"userName": sqwUser, "password": sqwPass}
    # else:
    #     postData = {"userName": userName, "password": passWord}
    response = RunMain().run_main('post', 'http://api.mkt.test.robotabc.com.cn/uaa/login?isAgree=1&username=18458163205&loginType=WORK_WX_WEB&password=lhz123456', data=None, headers=headers)
    code = json.loads(response)['code']
    print(code)
    if self.assertEqual(code,200):
        logger.info('正常登录')
        return True
    else:
        logger.error("登录失败，请检查登录参数信息")



def sqw_get(url=None, param=None, headers=None, username=sqwUserNameTest,
                      password=sqwPasswordTest):
    global sidNumber
    if check_login(userName=username, passWord=password) is True:
        headersSend = {"Cookie": sidNumber}
        if headers is not None:
            headersSend.update(headers)
        response = requests.get("%s%s" % (url, url), params=param, headers=headersSend)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError("Login Failed")


def sqw_post(url=None, postdata=None, headers=None, username=sqwUserNameTest,
                       password=sqwPasswordTest):
    if check_login(userName=username, passWord=password) is True:
        response = requests.post("%s%s" % (url, url), data=postdata,
                                 headers=headers)
        print('登录成功了嘛')
        print(response)
        return httpResponseResultDeal(response)
    else:
        raise AssertionError("Login Failed")

if __name__ == "__main__":
    #ss = sqw_post(url,headers,username=sqwUser,password=sqwPass)
    ss = check_login(None)
    print(ss)