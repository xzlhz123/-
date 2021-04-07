# import os
# import unittest
#
# import common
#
# import getpathInfo
# import readConfig
# from common import HTMLTestRunner, Log
# from common.configEmai import SendEmail
# import logging
# from logging.handlers import TimedRotatingFileHandler
#
#
# send_mail = SendEmail(
#     username='18458163206@163.com',
#     passwd='UIQMXUOXIWYEXLJL',
#     recv=['18458163206@163.com'],
#     title='测试邮件',
#     content='测试发送邮件',
#     file=r'C:\Users\admin\Pictures\Saved Pictures\图片2.png',
#     ssl=True
# )
# '获取项目绝对路径'
# path = getpathInfo.get_Path()
# '设置报告存放文件夹'
# report_path = os.path.join(path,'result')
# '获取配置文件中的邮件开关值'
# on_off = readConfig.ReadConfig().get_email('on_off')
# print(on_off)
# log = Log.logger
#
#
#
#
# '定义一个类AllTest'
# class AllTest:
#     '初始化一些参数和数据'
#     def __init__(self):
#         global resultPath
#         '设置报告存放路径为：result/report.html'
#         resultPath = os.path.join(report_path,'report.html')
#         print('路径：'+resultPath)
#         '配置执行那些测试文件的配置文件路径'
#         self.caseListFile = os.path.join(path,'caselist.text')
#         print('测试文件路径：'+self.caseListFile)
#         '真正的测试断言文件路径'
#         self.caseList = os.path.join(path,'testCase')
#         print('真正的测试断言文件路径：'+self.caseList)
#         self.caseList = []
#         '将resultPath的值输入到日志，方便定位查看问题'
#         log.info('resultPath',resultPath)
#         log.info('caseListFile',self.caseListFile)
#         log.info('caseList',self.caseList)
#     def set_case_list(self):
#         """
#         读取caselist.txt文件中的用例名称，并添加到caselist元素组
#         :return
#         """
#         '打开这些用例集'
#         print('打开用例集：')
#         fb = open('D://workplace//InterfaceTest_master//caselist.text','rb')
#         print('打开用例集44：'+self.caseListFile)
#         for value in fb.readlines():
#             data = str(value)
#             '如果data非空且不以#开头'
#             if data !='' and not data.startswith("#"):
#                 '读取每行数据会将换行转换为\n,去掉每行数据中的\n'
#                 self.caseListFile.append(data.replace('\n',''))
#         fb.close()
#     def set_case_suite(self):
#         """
#
#         :return:
#         """
#         '通过set_case_list()拿到caselist元素组'
#         self.set_case_list()
#         print('拿到caselist元素组：'+self.set_case_list())
#         test_suite = unittest.TestSuite()
#         suite_moudle = []
#         '从caselist元素组中循环取出case'
#         for case in self.caseList:
#             '通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面'
#             case_name = case.split("/")[-1]
#             '打印取出来的名称'
#             print(case_name+".py")
#             '批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名'
#             discover = unittest.defaultTestLoader.discover(self.caseList,pattern=case_name+'.py',top_level_dir=None)
#             '将discover存入suite_module元素组'
#             suite_moudle.append(discover)
#             print('suite_module:'+str(suite_moudle))
#         '判断suite_module元素组是否存在元素'
#         if len(suite_moudle) > 0:
#             '如果存在元素，则循环取出元素内容，命名为suite'
#             for suite in suite_moudle:
#                 '从discover中取出test_name,使用addTest添加到测试集中'
#                 for test_name in suite:
#                     test_suite.addTest(test_name)
#         else:
#             print('else:')
#             return None
#         '返回测试集'
#         return test_suite
#     def run(self):
#         global fp
#         """
#         run test
#         :return:
#         """
#         try:
#             '调用set_case_suite获取test_suite'
#             print('7777777777777777')
#             suit = self.set_case_suite()
#             print('try')
#             print(str(suit))
#             '判断test_suite是否为空'
#             if suit is not None:
#                 print('if-suit')
#                 '#打开result/20181108/report.html测试报告文件，如果不存在就创建'
#                 fp = open(resultPath,'wb')
#                 #调用HTMLTestRunner
#                 runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='Test Report')
#                 print(runner)
#                 runner.run(suit)
#             else:
#                 print("have no case to test")
#         except Exception as ex:
#             print(str(ex))
#         finally:
#             print('*************************TEST END**********************')
#             fp.close()
#         #判断邮件发送的开关
#         if on_off == 'on':
#             send_mail.send_email()
#         else:
#             print("邮件发送开关关闭，请打开开关后即可正常发送报告")
#
# if __name__ == '__main__':
#
#     AllTest().run()

import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from common.configEmai import SendEmail
from apscheduler.schedulers.blocking import BlockingScheduler


# import common.Log

send_mail = SendEmail(
    username='18458163206@163.com',
    passwd='UIQMXUOXIWYEXLJL',
    recv=['18458163206@163.com'],
    title='测试邮件',
    content='测试发送邮件',
    file=r'C:\Users\admin\Pictures\Saved Pictures\图片2.png',
    ssl=True
)
path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')


# log = common.Log.logger

class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, "report.html")  # result/report.html
        self.caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        print('等等'+self.caseListFile)
        fb = open(self.caseListFile,'r')
        print('大佬')
        for value in fb.readlines():
            print('zhizhiz')
            data = value
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suite(self):
        """
        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            print('try')
            print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                fp = open(resultPath, 'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            print("*********TEST END*********")
            # log.info("*********TEST END*********")
            fp.close()
        # 判断邮件发送的开关
        if on_off == 'on':
            send_mail.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()

if __name__ == '__main__':
    AllTest().run()





















