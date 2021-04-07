import configparser
import os

import getpathInfo

'首先获取配置文件路径'
path = getpathInfo.get_Path()
'这句话是在path路径下再加一级'
config_path = os.path.join(path,'config.ini')
'调用外部的读取配置文件的方法'
config = configparser.ConfigParser()
config.read(config_path,encoding='utf-8')

class ReadConfig():
    '获取config配置文件中的 http信息'
    def get_http(self,name):
        value = config.get('HTTP01',name)
        return value
    '获取config配置文件中的EMAIL信息'
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value
    '获取config配置文件中的mysql信息'
    def get_mysql(self,name):
        value = config.get('DATABASE01',name)
        return value
if __name__ == '__main__':
    print('HTTP中的baseurl值为：',ReadConfig().get_http('baseurl'))
    print('EMAIL中的是否发送邮件开关值为',ReadConfig().get_email('on_off'))
    print('DATABASE01数据库中的值：',ReadConfig().get_mysql('dbname01'),ReadConfig().get_mysql('dbname02'))