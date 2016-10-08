# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:49:31 2016

@author: huliqun
"""
import urllib
import urllib2
import string
import re
import pandas as pd
import spiderSports500WCurrent as S5W
import time
from sqlalchemy import *
import json
import random
import sqlite3 
import datetime

#dbName = './matchDData.db'
dbName = 'D:/WinPython-32bit-2.7.10.3/work/sportsWeb/matchDData.db'
engine = create_engine('sqlite:///'+dbName, echo=False)

def getMatchDate():
    try:    
        d = datetime.datetime.now()
        delta = datetime.timedelta(days=1) 
        d -= delta  
        return d.strftime("%Y-%m-%d")          
    except Exception as e:
        print e
        return None
    
    return None

def getMinRate(my_list):
    minNum = my_list[0]
    if minNum > 40:
        return 0.00
    for i in my_list:
        if i < minNum:
            minNum = i
    return minNum

def getMatch():
    urlM = "http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=had&_=1460170422871"   
    try:
        content = urllib2.urlopen(urlM,timeout = 2).read()
        message = content.decode('gbk').encode('utf8')
        message = message.replace('getData(','')
        message = message.replace(');','')
        df = pd.DataFrame( columns=['matchid','match', 'date', 'matchtype','matchtypename','matchzhu',
                                'matchke','matchzhuf','matchkef','zhuHScore','keHScore','zhuScore','keScore','mResult','status',
                                'wrate','drate','lrate','minrate','fixScore','fixResult','wrateS','drateS','lrateS','minrateS','allmax','allresult','singleFlag',
                                'score','s0','s1','s2','s3','s4','s5','s6','s7','infoUrl','zhuRank','keRank','rankDValue']).set_index('matchid')
        decode = json.loads(message)
        matchInfos=decode['data']
        for match in matchInfos:
            wrate = drate = lrate = wrateS = drateS = lrateS = '0.0'
            fixScore = '0'
            if matchInfos[match]['status'] != 'Selling':
                continue
            matchid = matchInfos[match]['date'].replace('-','') + matchInfos[match]['num']
            if matchInfos[match].get('had') is not None:
                wrate = matchInfos[match]['had']['h']
                drate = matchInfos[match]['had']['d']
                lrate = matchInfos[match]['had']['a']
                singleFlag = matchInfos[match]['had']['single']
            minrate = getMinRate( (string.atof( wrate),string.atof( drate),string.atof( lrate )) )
            if matchInfos[match].get('hhad') is not None:
                fixScore = matchInfos[match]['hhad']['fixedodds']
                wrateS = matchInfos[match]['hhad']['h']
                drateS = matchInfos[match]['hhad']['d']
                lrateS = matchInfos[match]['hhad']['a']
            #                singleFlag = matchInfos[match]['hhad']['single']
            minrateS = getMinRate( (string.atof( wrateS),string.atof( drateS),string.atof( lrateS )) )
            
            if minrate <= minrateS:
               allmax = minrateS
               allresult = 'S'
            else:
               allmax = minrate
               allresult = 'N'
                           
#            print matchInfos[match]['num'], matchInfos[match]['a_cn']
        
            line = pd.DataFrame([[ matchid,matchInfos[match]['num'],matchInfos[match]['date'],matchInfos[match]['l_cn'],matchInfos[match]['l_cn_abbr'],matchInfos[match]['h_cn'],
                  matchInfos[match]['a_cn'],'','','','','','','',matchInfos[match]['status'],
                  wrate,drate,lrate,str(minrate),fixScore, '', wrateS, drateS, lrateS,str(minrateS),str(allmax),allresult,singleFlag,
                  '', '', '', '', '', '', '', '', '','','','',4]],
                  columns=['matchid','match', 'date', 'matchtype','matchtypename','matchzhu',
                   'matchke','matchzhuf','matchkef','zhuHScore','keHScore','zhuScore','keScore','mResult','status',
                   'wrate','drate','lrate','minrate','fixScore','fixResult','wrateS','drateS','lrateS','minrateS','allmax','allresult','singleFlag',
                   'score','s0','s1','s2','s3','s4','s5','s6','s7','infoUrl','zhuRank','keRank','rankDValue']
                  ).set_index('matchid')
            df= df.append(line)
            
        df.to_sql('score_data',engine,if_exists='replace')
        
        return True
    except Exception as e:
        print e
        return False

def dataSync():
    conDData = sqlite3.connect(dbName)
    try:   
        sql_update="update score_data set zhuRank = (select b.zhuRank from score_data_500 b where b.matchid = score_data.matchid),keRank = (select b.keRank from score_data_500 b where b.matchid = score_data.matchid),rankDValue = (select b.rankDValue from score_data_500 b where b.matchid = score_data.matchid)"
        #获取游标  
        sqlite_cursor=conDData.cursor()
        sqlite_cursor.execute(sql_update) 
        conDData.commit()
    except Exception as e:
        print e
        print 'Sql Error'
        return None
    finally:
        conDData.close()
    
    return None
        
if __name__ =="__main__":
    match_date = getMatchDate()
    getMatch()
    match_date = S5W.getMatchDate()
    S5W.get500Wan(match_date)
    dataSync()
    
    
