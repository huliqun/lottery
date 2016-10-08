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
import time
from sqlalchemy import *
import json
import random
import sqlite3 
import datetime
import BeautifulSoup
#dbName = './matchDData.db'
dbName = 'D:/WinPython-32bit-2.7.10.3/work/sportsWeb/matchDData.db'
engine = create_engine('sqlite:///'+dbName, echo=False)

def getMatchDate():
    try:    
        d = datetime.datetime.now()
#        delta = datetime.timedelta(days=1) 
#        d -= delta  
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


def getDate(dataStr):
    patternWeek=re.compile(u'[\u4e00-\u9fa5]{3}');
    patternDate=re.compile(u'\d{4}-\d{2}-\d{2}');
    weekday = ''
    text = patternWeek.findall(dataStr)[0]
    if text == u'星期一':
        weekday = u'周一'
    if text == u'星期二':
        weekday = u'周二'
    if text == u'星期三':
        weekday = u'周三'
    if text == u'星期四':
        weekday = u'周四'
    if text == u'星期五':
        weekday = u'周五'
    if text == u'星期六':
        weekday = u'周六'
    if text == u'星期日':
        weekday = u'周日'
    return [text,patternDate.findall(dataStr)[0],weekday]

def getMDate(date,TimeStr):
    patternDate=re.compile(u'\d{4}-\d{2}-\d{2}');
    timeD = patternDate.findall(TimeStr)
    patternTime=re.compile(u'\d{2}:\d{2}:\d{2}');
    timeT = patternTime.findall(TimeStr)
    if len(timeT)>0:
        if timeT[0] > '23:40:00':
            d = datetime.datetime.strptime(date,"%Y-%m-%d")
            delta = datetime.timedelta(days=1) 
            d += delta 
            return d.strftime("%Y-%m-%d")
    if not timeT:
        return TimeStr
    else:
        return timeD[0]

def getMTime(TimeStr):
    patternTime=re.compile(u'\d{2}:\d{2}:\d{2}');
    timeT = patternTime.findall(TimeStr)
    if not timeT:
        return TimeStr
    else:
        return timeT[0]
        
def getNum(NumStr):
    if NumStr is None:
        return '0'
    patternNum=re.compile(u'\[(\d+)\]');
    NumT = patternNum.findall(NumStr)
    if not NumT:
        return '0'
    else:
        return NumT[0]

def getScore(ScoreStr):
    if ScoreStr is None:
        return ['','']
    patternScore=re.compile(u'(\d+):(\d+)');
    ScoreT = patternScore.findall(ScoreStr)
    if not ScoreT:
        return ['','']
    else:
        return [ScoreT[0][0],ScoreT[0][1]]

def getMResult(ScoreR):
    mResult = ''
    if int(ScoreR[0]) > int(ScoreR[1]):
        mResult = 'W'
    elif int(ScoreR[0]) == int(ScoreR[1]):
        mResult = 'D'
    else:
        mResult = 'L'
    return mResult

def getMResultF(ScoreR,fixScore):
    fixResult = ''
    if int(ScoreR[0]) + int(eval(fixScore)) > int(ScoreR[1]):
        fixResult = 'W'
    elif int(ScoreR[0]) + int(eval(fixScore)) == int(ScoreR[1]):
        fixResult = 'D'
    else:
        fixResult = 'L'
    return fixResult

def getWDLRate(tdInfo):
    divS = tdInfo.findAll('div')
    spans = divS[0].findAll('span')
    rate=(u'0.00',u'0.00',u'0.00')
    rateF=(u'0.00',u'0.00',u'0.00')
    if len(spans) == 3:
        rate=(spans[0]['data-sp'],spans[1]['data-sp'],spans[2]['data-sp'])
        
    spansF = divS[1].findAll('span')
    if len(spansF) == 3:
        rateF = (spansF[0]['data-sp'],spansF[1]['data-sp'],spansF[2]['data-sp'])
    return [rate,rateF]

def getMatchSync(trs500W,dateInfo,num):
    try:
        df = pd.DataFrame( columns=['matchid','mid','match', 'date', 'mdate', 'mtime', 'matchtype','matchzhu','zhuRank','matchke','keRank','rankDValue','zhuHScore','keHScore','zhuScore','keScore','mResult','status',
                                'wrate','drate','lrate','minrate','fixScore','fixResult','wrateS','drateS','lrateS','minrateS','allmax','allresult','singleFlag']).set_index('matchid')
        for line in trs500W:
            tds = line.findAll('td')
            
            mid = line['mid']
            match = dateInfo[2]+tds[0].a.contents[0]
            date = dateInfo[1]
            mdate = getMDate(date,line['pendtime'])
            matchid = mdate.replace(u'-','')+match
            mtime = getMTime(line['pendtime'])
            matchtype = line['lg']
            matchzhu = tds[3].a['title']
            zhuRank = getNum(tds[3].span.string)
            
            matchke = tds[5].a['title']
            keRank = getNum(tds[5].span.string)
            rankDValue = int(zhuRank) - int(keRank)
            if int(zhuRank) == 0:
                rankDValue = 4
            rates=getWDLRate(tds[7]) 
            wrate,drate,lrate=rates[0]        
            wrateS,drateS,lrateS=rates[1]
            minrate = getMinRate( (string.atof( rates[0][0]),string.atof( rates[0][1]),string.atof( rates[0][2])) )
            minrateS  = getMinRate( (string.atof( rates[1][0] ),string.atof( rates[1][1] ),string.atof( rates[1][2] )) )  
            
            if minrate <= minrateS:
                allmax = minrateS
                allresult = 'S'
            else:
                allmax = minrate
                allresult = 'N'
                           
            fixScore = tds[6].findAll('p','concede t_line green')[0]['span']
            singleFlag = '0'
            if tds[0].attrs:
                if tds[0]['class']=='danguan_game_icon':
                    singleFlag = '1'
            
            zhuScore = ''
            keScore = ''
            mResult = ''
            fixResult = ''
            status = '0'
            if tds[4].attrs:
                scores = getScore(tds[4]['a'])
                zhuScore = scores[0]
                keScore = scores[1]
                mResult = getMResult(scores)
                fixResult = getMResultF(scores,fixScore)
                status = '1'
            
            line = pd.DataFrame([[ matchid,mid,match,date,mdate,mtime,matchtype,
                  matchzhu,zhuRank,matchke,keRank,rankDValue,'','',zhuScore,
                  keScore,mResult,status,wrate,drate,lrate,minrate,fixScore,
                  fixResult,wrateS,drateS,lrateS,minrateS,allmax,allresult,singleFlag]],
                  columns=['matchid','mid','match', 'date', 'mdate', 'mtime', 'matchtype',
                  'matchzhu','zhuRank','matchke','keRank','rankDValue','zhuHScore','keHScore','zhuScore',
                  'keScore','mResult','status','wrate','drate','lrate','minrate','fixScore',
                  'fixResult','wrateS','drateS','lrateS','minrateS','allmax','allresult','singleFlag']
                  ).set_index('matchid')
            df= df.append(line)
        
        if num == 0:
            df.to_sql('score_data_500',engine,if_exists='replace')
        else:
            df.to_sql('score_data_500',engine,if_exists='append')
        
        return True
    except Exception as e:
        print e
        return False

def get500Wan(date):
    urlid500W = 'http://trade.500.com/jczq/?date='+date+'&playtype=both'
    content500W = urllib2.urlopen(urlid500W,timeout = 2).read()
    message500W = content500W.decode('gbk').encode('utf8')
#    fp = open("test.txt",'w')
#    fp.write(message500W)
#    fp.close()
#    fp = open("test.txt",'r')
#    soup500W = BeautifulSoup.BeautifulSOAP(fp.read())
#    fp.close
    soup500W = BeautifulSoup.BeautifulSOAP(message500W)
    tb500Wdate = soup500W.findAll('div','bet_date')
    for i in range(0,len(tb500Wdate)):
        dateInfo = getDate(tb500Wdate[i].contents[0])
        tb500Wtb = soup500W.findAll('table','bet_table')
        trs500W = tb500Wtb[i].findAll('tr')
        getMatchSync(trs500W,dateInfo,i)
        
if __name__ =="__main__":
    match_date = getMatchDate()
    get500Wan(match_date)
