import json

import requests

from common.ddd import sessionRequest
from testcase.geturlParams import geturlParams


class RunMain():
    '定义一个方法，传入需要的参数url和data'
    def send_post(self,url,data,header):
        '参数必须按照url，data顺序传入'
        #result = requests.post(url=url,data=None,headers=header).json()
        result = requests.post(url, data=None, json=data, headers=header).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def send_get(self,url,data,header):
        result = requests.get(url=url,data=None,header=header).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    '定义一个run_main函数，通过传过来的method来进行get或者post请求'
    def run_main(self,method,url=None,data=None,headers=None):
        result = None
        if method == 'post':
            result = self.send_post(url,data,headers)
        elif method == 'get':
            result = self.send_get(url,data,headers)
        else:
            print("method值错误！")
        return result

# if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
#  url = geturlParams().get_Url('channel')
#  headers = {
#      'platform': 'PC',
#      'wx-data-source': 'QW',
#      'Content-Type': 'application/json',
#      'v': '2.0.0',
#      'token':access_token
#  }
#  #添加渠道接口
#  result2 = RunMain().run_main('post', 'http://api.mkt.test.robotabc.com.cn/mkt-mobile/qw-marketing/add-channel?channelName=999',
#                               data=None,headers=headers)
#
#  print(result2)















