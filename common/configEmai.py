import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import self as self


class SendEmail(object):
    def __init__(self,username,passwd,recv,title,content,file = None,ssl = False,
        email_host = 'smtp.163.com',port=25,ssl_port=465):
        # 用户名
        self.username = username
        #密码
        self.passwd = passwd
        #收件人，多个要传list['abc@qq.com','bbb@qq.com']
        self.recv = recv
        #邮件标题
        self.title = title
        #邮件正文
        self.content = content
        #邮件路径，如果不在当前目录下，要写绝对路径
        self.file = file
        #smtp服务器地址
        self.email_host = email_host
        #普通端口
        self.port = port
        #是否安全链接
        self.ssl = ssl
        #安全链接端口
        self.ssl_port = ssl_port

    def send_email(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file: #处理附件
            file_name = os.path.split(self.file)[-1] #只取文件名，不取路径
            try:
                f = open(self.file,'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！')
            else:
                att = MIMEText(f,'base64','utf-8')
                att['Content-Type'] = 'application/octet - stream'
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
            #邮件正文的内容
            msg.attach(MIMEText(self.content))
            #邮件主题
            msg['Subject'] = self.title
            #发送者账号
            msg['Form'] = self.username
            #接收者账号列表
            msg['TO'] = ','.join(self.recv)
            if self.ssl:
                self.smtp = smtplib.SMTP_SSL(self.email_host,port = self.ssl_port)
            else:
                self.smtp = smtplib.SMTP(self.email_host,port=self.port)
            #发送邮件服务器对象
            self.smtp.login(self.username,self.passwd)
            try:
                print(self.username)
                self.smtp.sendmail(self.username,self.recv,msg.as_string())
                pass
            except Exception as e:
                print('出错了。。。',e)
            else:
                print('发送成功')
            self.smtp.quit()

if __name__ == '__main__':
    m = SendEmail(
        username='18458163206@163.com',
        passwd='UIQMXUOXIWYEXLJL',
        recv = ['18458163206@163.com'],
        title = '测试邮件',
        content='测试发送邮件',
        file = r'C:\Users\admin\Pictures\Saved Pictures\图片2.png',
        ssl = True
    )
    m.send_email()



























