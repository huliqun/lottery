# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:45:49 2016

@author: Administrator
"""
import urllib
import datetime
import json

from workserver.util import SysUtil
from workserver.batch.BatchBase import BatchBase
from workserver.module.models import MatchInfoD
import spiderSports500WCurrent, SpiderSports, SpiderSports500W

class SpiderSportsCurrentBatch(BatchBase):
    def run(self):
        self.initialize()
        self.getMatch()
        self.release()
        
    def getMinRate(self, my_list):
        minNum = my_list[0]
        if minNum > 40:
            return 0.00
        for i in my_list:
            if i < minNum:
                minNum = i
        return minNum
        
    def getMatch(self):
        urlM = "http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=had&_=1460170422871"   
        try:
#            self.session.execute(text('truncate table tbl_matchinfod'))
            self.session.query(MatchInfoD).delete()
            self.session.flush()
            content = urllib.request.urlopen(urlM,timeout = 10).read()
            message = content.decode('gbk')
            message = message.replace('getData(','')
            message = message.replace(');','')
            decode = json.loads(message)
            matchInfos=decode['data']
            for match in matchInfos:
                wrate = drate = lrate = wrateS = drateS = lrateS = 0.0
                fixScore = '0'
                if matchInfos[match]['status'] != 'Selling':
                    continue
                matchid = matchInfos[match]['date'].replace('-','') + matchInfos[match]['num']
                singleFlag = '0'
                if matchInfos[match].get('had') is not None:
                    wrate = float(matchInfos[match]['had']['h'])
                    drate = float(matchInfos[match]['had']['d'])
                    lrate = float(matchInfos[match]['had']['a'])
                    singleFlag = matchInfos[match]['had']['single']
                minrate = self.getMinRate( (wrate,drate,lrate) )
                if matchInfos[match].get('hhad') is not None:
                    fixScore = matchInfos[match]['hhad']['fixedodds']
                    wrateS = float(matchInfos[match]['hhad']['h'])
                    drateS = float(matchInfos[match]['hhad']['d'])
                    lrateS = float(matchInfos[match]['hhad']['a'])
                minrateS = self.getMinRate( (wrateS,drateS,lrateS) )
                
                mi = MatchInfoD(matchid = matchid,
                                match = matchInfos[match]['num'],
                                date = datetime.datetime.strptime(matchInfos[match]['date'], '%Y-%m-%d').date(),
                                matchtype = matchInfos[match]['l_cn'],
                                matchtypename = matchInfos[match]['l_cn_abbr'],
                                matchzhu = matchInfos[match]['h_cn'],
                                matchke = matchInfos[match]['a_cn'],
                                status = matchInfos[match]['status'],
                                wrate = wrate,
                                drate = drate,
                                lrate = lrate,
                                minrate = minrate,
                                fixScore = fixScore,
                                wrateS = wrateS,
                                drateS = drateS,
                                lrateS = lrateS,
                                minrateS = minrateS,
                                singleFlag = singleFlag)
                self.session.add(mi)
            self.session.commit()
            
            return True
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            return False        
    
if __name__ == '__main__':  
    SpiderSportsCurrentBatch().run()
    spiderSports500WCurrent.SpiderSports500WCurrentBatch().run()
    SpiderSports.SpiderSportsBatch().run()
    SpiderSports500W.SpiderSports500WBatch().run()