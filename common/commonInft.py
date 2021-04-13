'''
    @功能：     获取sql查询语句的返回值
    @para: command 带执行的db查询
    @return: 存在返回第一个字段值,否则返回None
    @ hongzenghui  2015-11-10
'''
import os
import logging
import pymysql

from common import Globle, Log
from common.Globle import LogLevel
from common.Log import logger


def getDbQueryResult(dbCommand = None, dbIp=Globle.sqwIpTest, dbInstance=Globle.sqwDbInstance01, dbUser=Globle.sqwUserNameTest, dbPass=Globle.sqwPasswordTest):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = pymysql.connect(host=dbIp, user =dbUser, password =dbPass, database =dbInstance, charset ='utf8')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `ww_channel_conf` ')
    exeRet = cursor.fetchone()
    print(exeRet)
    cursor.close ()
    conn.close()
    if exeRet is None:
        logger.warning('无法找到响应的记录')
        return None
    else:
        logger.info('找到相应记录')
        return exeRet[0]

if __name__ == '__main__':
    '验证拼接后的正确性'
    print(getDbQueryResult())