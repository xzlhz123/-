import requests
import json

url= "http://api.mkt.robotabc.com.cn/uaa/login"
param = {
    "isAgree":"1",
    "username":"18458163208",
    "password":"lhz123456",
    "loginType":"WORK_WX_WEB"
}
headers = {'content-type':'application/json'}
r = requests.post(url,data=param,headers=headers)
print(r.text)