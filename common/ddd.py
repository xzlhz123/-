import requests

#实例化会话对象
sessionRequest = requests.session()
loginurl = 'http://api.mkt.robotabc.com.cn'
data = {
    'username' : '18458163208',
    'password' : 'lhz123456',
    'isAgree' :1,
    'loginType':'WORK_WX_WEB'
}
headers = {
    'Content-Type':'application/json',
}
#第二次请求的url
channelUrl = 'https://api.mkt.robotabc.com.cn/mkt-mobile/qw-marketing/add-channel'
parame= {
    'channelName':'333'
}


# #登录
# resp = sessionRequest.post(url=loginurl,json=data,headers = headers)
# print(resp.text)
# #请求渠道接口
# channelResp = sessionRequest.post(channelUrl,json=parame)
# print(channelResp.text)