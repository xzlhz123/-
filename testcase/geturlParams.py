import readConfig
from common.readExcel import readExcel

readconfig = readConfig.ReadConfig()
'定义一个方法，将从配置文件中读取的信息进行拼接'
class geturlParams():
    def get_Url(self,sheet_name):
        #获取url
        url = readExcel().get_xls('userCase.xlsx', sheet_name)[1][3]
        #获取data
        data = readExcel().get_xls('userCase.xlsx', sheet_name)[1][5]
        #获取url+data
        #new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') +url+'?' + data
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + url + '?'
        return new_url
if __name__ == '__main__':
    '验证拼接后的正确性'
    print(geturlParams().get_Url('channel'))
