# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 21:54:27 2016

@author: Administrator
"""

import urllib
#延长有效期 payTime=1 半年 payTime=2 一年
#url = 'http://127.0.0.1:8000/sports/webService/payMoney?userid=33333&payTime=2' 

#url = 'http://127.0.0.1:8000/sports/webService/userReg?userid=111111&username=aa&phone=18698729471&local=123456&IDNo=111111&accounttype=0'  注册借口 accounttype  0业主办 1 彩民版
#url = 'http://127.0.0.1:8000/sports/webService/setBaseMoney?userid=111111&basemoney=100.00'  设置金额 业主版和现在一样， 才民办小于 100 元, mode 字段 彩民班的模式现在有A B两个
url = 'http://127.0.0.1:8000/sports/webService/getCurrentResult?userid=111111' 获取投注未出结果的比赛信息 动态比分
#url = 'http://127.0.0.1:8000/sports/webService/getdealer?userid=222222' 获取dealer 信息
#url = 'http://127.0.0.1:8000/sports/webService/getGambleResult?userid=111111&gambleFlag=1&dealerid=1'  投注比赛 彩民版 mode A时需要参数 dealerid 从上个借口中获得的
#url = 'http://127.0.0.1:8000/sports/webService/getAccountLog?userid=111111' 获取账户流水信息

#url = 'http://127.0.0.1:8000/sports/webService/userReg?userid=222222&username=aa&phone=18698729472&local=123456&IDNo=111111&accounttype=1'
#url = 'http://127.0.0.1:8000/sports/webService/setBaseMoney?userid=222222&basemoney=100.00&mode=A'
url = 'http://127.0.0.1:8000/sports/webService/getCurrentResult?userid=222222'
#url = 'http://127.0.0.1:8000/sports/webService/getdealer?userid=222222'
#url = 'http://127.0.0.1:8000/sports/webService/getGambleResult?userid=222222&gambleFlag=1&dealerid=1'

#url = 'http://127.0.0.1:8000/sports/webService/userReg?userid=33333&username=aa&phone=18698729473&local=123456&IDNo=111111&accounttype=1'
#url = 'http://127.0.0.1:8000/sports/webService/setBaseMoney?userid=33333&basemoney=100.00&mode=B'
url = 'http://127.0.0.1:8000/sports/webService/getCurrentResult?userid=33333'
#url = 'http://127.0.0.1:8000/sports/webService/getGambleResult?userid=33333&gambleFlag=1&dealerid=1'

#url = 'http://127.0.0.1:8000/sports/webService/getAccountLog?userid=111111'

try:
     
    response= urllib.request.urlopen(url,timeout = 2)
    msg = response.read()
    print(msg)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)