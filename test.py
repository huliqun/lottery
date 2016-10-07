# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 21:54:27 2016

@author: Administrator
"""

import urllib
#url = 'http://127.0.0.1:8000/sports/webService/userReg?userid=222222&username=aa&phone=18698729479&local=123456&IDNo=111111&accounttype=1'
#延长有效期 payTime=1 半年 payTime=2 一年
#url = 'http://127.0.0.1:8000/sports/webService/payMoney?userid=222222&payTime=2'

#url = 'http://127.0.0.1:8000/sports/webService/setBaseMoney?userid=222222&basemoney=100.00'
#url = 'http://127.0.0.1:8000/sports/webService/getCurrentResult?userid=222222'
url = 'http://127.0.0.1:8000/sports/webService/getGambleResult?userid=222222&gambleFlag=1'
#url = 'http://127.0.0.1:8000/sports/webService/getMatchResult?userid=9a7cdc479b8706657096e845769a3807&date=2016-04-19'
#url = 'http://127.0.0.1:8000/sports/webService/getAccountLog?userid=dc3fafc32ec267143b9a5aa3530413f9'
#url = 'http://127.0.0.1:8888/sports/webService/getdealer?userid=222222'
#url = 'http://127.0.0.1:8888/sports/webService/dealwithdealer?userid=222222&dealerid=1'
#url = 'http://127.0.0.1:8888/sports/webService/userReg?userid=39429f547fce78c5b4f63dee0c4185f1&username=zzz&phone=15555555555&local=%E5%93%88%E5%93%88&IDNo=111111&accounttype=1'
try:
    msg = urllib.request.urlopen(url,timeout = 2).read()
    print(msg)
except Exception as e:
    print(e)