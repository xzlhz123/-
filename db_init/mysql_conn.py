# -*- coding:utf-8 -*-


import pymysql as pymysql
# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
cnn = pymysql.connect(host='10.2.1.105',port=3306,user='java',password='Sl@mysql!2020@java',database='dg_mobile',charset='utf8')

# 使用cursor()方法获取操作游标
cursor = cnn.cursor();
sql = 'SELECT * FROM talk_material';

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone();
print(data[0]);
cnn.close();



# 执行sql语句

