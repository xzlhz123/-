import  requests
import  json

def qrcode_query(url = "",params = None,headers = None):
    url ="http://api.mkt.test.robotabc.com.cn/mkt-mobile/qw-marketing/qrcode-query"
params = {
    "pageSize":"10",
    "pageNum":"1"
}
headers = {'content-type':'application/json'}
r=requests.get(url=url,data = json.dumps(params),headers=headers)
d = json.loads(r.text)
print(d)