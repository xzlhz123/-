'''
    @功能：     对http报文的response进行解析，并返回一个类，包含解析后的结果、状态、及text属性
    @para:
    httpResponse: http报文响应
    @return: 如果一个类的对象，类中有result、statusLine及text三个属性
'''
import json
import re

from common.Globle import responseClass


def httpResponseResultDeal(httpResponse):
    responseObject = responseClass()
    responseObject.result = False
    if httpResponse is not None:
        responseObject.text = httpResponse.text
        responseObject.statusLine = httpResponse.status_code
        responseObject.content = httpResponse.content
        try:
            # 当返回不为json时，该函数会抛出异常
            #             httpResponse.json()
            responseDict = json.loads(httpResponse.text)
            # 最新开发框架，有错误返回的格式为{'errorCode':'BE100-01','message':'获取失败','expLevel':'error'}
            if responseDict.has_key('errorCode'):
                if responseDict['errorCode'] != "0":
                    responseObject.result = False
                    return responseObject
            # 线索运维平台返回错误格式：{"errorMsg":"修改大转盘活动配置出错"}
            if responseDict.has_key('errorMsg'):
                responseObject.result = False
                return responseObject
            if responseDict.has_key('success'):
                if responseDict['success'] == "false":
                    responseObject.result = False
                    return responseObject
            # 线索返回判断
            if responseDict.has_key('response'):
                if responseDict['response'].has_key('success'):
                    if responseDict['response']['success'] == False:
                        responseObject.result = False
                        return responseObject
            responseObject.result = True
        except:  # 非json异常
            if re.search(httpResponse.text, 'true'):
                responseObject.result = True
            elif re.search(httpResponse.text, 'null'):
                responseObject.result = True
            #             elif isinstance(httpResponse.text, list) and len(httpResponse.text):
            elif re.search(httpResponse.text, '^\[.+\]$'):
                responseObject.result = True

            elif re.search(httpResponse.text, '''^[0-9]+$'''):
                responseObject.result = True
            elif re.search(httpResponse.text, '''^\"[0-9]+\"$'''):
                responseObject.result = True
            else:
                responseObject.result = False
    return responseObject
