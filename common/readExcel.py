
#首先拿到该项目所在的绝对路径
import os

from xlrd import open_workbook

import getpathInfo
#调用读Excel的第三方库xlrd


path = getpathInfo.get_Path()

class readExcel():
    '定义一个方法来获取Excel中的信息:xls_name 填写用例的EXCEL名称，sheet_name 为该Excel的sheet名称'
    def get_xls(self,xls_name,sheet_name):
        cls = []
        #获取用例文件路径
        xlspath = os.path.join(path,"testFile",'case',xls_name)
        #打开用例Excel
        file = open_workbook(xlspath)
        #获得打开Excel的sheet
        sheet = file.sheet_by_name(sheet_name)
        #获取sheet内容行数
        nrows = sheet.nrows
        '根据行数做循环'
        for i in range(nrows):
            '如果这个Excel的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]'
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))

        return cls
'我们执行该文件测试一下是否可以正常获取excel中的值'
if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx', 'channel')[0][0])
    print(readExcel().get_xls('userCase.xlsx', 'channel')[0][1])
    print(readExcel().get_xls('userCase.xlsx', 'channel')[1][2])






