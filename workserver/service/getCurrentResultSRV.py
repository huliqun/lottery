# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon
import datetime

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import MatchData, MatchInfo, MatchInfoD
from workserver.util import SysUtil

class getCurrentResultResource(ServiceBase):
    def on_get(self, req, resp):
        self.initialize()
        req_para = falcon.util.uri.parse_query_string(req.query_string)
        
        if 'userid' not in req_para.keys():
            self.errorReturn(GLBConfig.API_ERROR, 'userid 不存在.')
        
        matches = self.session.query(MatchData).\
            filter(MatchData.date >= SysUtil.getToday()).\
            filter(MatchData.status == GLBConfig.ENABLE).\
            filter(MatchData.userid == req_para['userid']).all()
        maData = []
        if matches:
            for m in matches:
                if m.singleFlag == GLBConfig.M_SINGLE:
                    matInfo = self.session.query(MatchInfoD).filter(MatchInfoD.matchid == m.matchAID).first()
                    if not matInfo:
                        matInfo = self.session.query(MatchInfo).filter(MatchInfo.matchid == m.matchAID).first()
                    if matInfo:
                        maData.append({'match': m.matchAID,
                           'matchtype': matInfo.matchtype,
                           'zhu': matInfo.matchzhu,
                           'ke': matInfo.matchke,
                           'wrate': matInfo.wrate,
                           'drate': matInfo.drate,
                           'lrate': matInfo.lrate,
                           'result': m.matchAResult,
                           'money': m.money})
                elif m.singleFlag == GLBConfig.M_DUAL:
                    mA = self.session.query(MatchInfoD).filter( MatchInfoD.matchid == m.matchAID ).first()
                    if not mA:
                        mA = self.session.query(MatchInfo).filter( MatchInfo.matchid == m.matchAID ).first()

                    mB = self.session.query(MatchInfoD).filter( MatchInfoD.matchid == m.matchBID ).first()
                    if not mB:
                        mB = self.session.query(MatchInfo).filter( MatchInfo.matchid == m.matchBID ).first()
                    if mA and mB:
                        maData.append({'matchAID': m.matchAID,
                                       'matchAResult': m.matchAResult,
                                       'matchAtype':mA.matchtypename,
                                       'matchAzhu':mA.matchzhu,
                                       'matchAke':mA.matchke,
                                       'matchAw':mA.wrate,
                                       'matchAd':mA.drate,
                                       'matchAl':mA.lrate,
                                       'matchBID':m.matchBID,
                                       'matchBResult':m.matchBResult,
                                       'matchBtype':mB.matchtypename,
                                       'matchBzhu':mB.matchzhu,
                                       'matchBke':mB.matchke,
                                       'matchBw':mB.wrate,
                                       'matchBd':mB.drate,
                                       'matchBl':mB.lrate,
                                       'money': m.money})
                elif m.singleFlag == GLBConfig.M_HAFU or m.singleFlag == GLBConfig.M_SCORE:
                    matInfo = self.session.query(MatchInfoD).filter(MatchInfoD.matchid == m.matchAID).first()
                    if not matInfo:
                        matInfo = self.session.query(MatchInfo).filter(MatchInfo.matchid == m.matchAID).first()
                    if matInfo:
                        maData.append({'matchid': matInfo.matchid,
                                   'match': matInfo.match,
                                   'date': matInfo.date.strftime('%Y-%m-%d'),
                                   'matchTime': matInfo.matchTime.strftime('%H:%M'),
                                   'matchtype': matInfo.matchtype,
                                   'matchzhu': matInfo.matchzhu,
                                   'matchke': matInfo.matchke,
                                   'wrate': matInfo.wrate,
                                   'drate': matInfo.drate,
                                   'lrate': matInfo.lrate,
                                   'fixScore': matInfo.fixScore,
                                   'wrateS': matInfo.wrateS,
                                   'drateS': matInfo.drateS,
                                   'lrateS': matInfo.lrateS,
                                   's0': matInfo.s0,
                                   's1': matInfo.s1,
                                   's2': matInfo.s2,
                                   's3': matInfo.s3,
                                   's4': matInfo.s4,
                                   's5': matInfo.s5,
                                   's6': matInfo.s6,
                                   's7': matInfo.s7,
                                   'ww': matInfo.ww,
                                   'wd': matInfo.wd,
                                   'wl': matInfo.wl,
                                   'dw': matInfo.dw,
                                   'dd': matInfo.dd,
                                   'dl': matInfo.dl,
                                   'lw': matInfo.lw,
                                   'ld': matInfo.ld,
                                   'll': matInfo.ll})
                    
            self.result['data'] = maData
        else:
            self.errorReturn(GLBConfig.API_ERROR, '无数据.')
                
        req.context['result'] = self.result
        resp.set_header('Powered-By', 'huliquns@126.com')
        resp.status = falcon.HTTP_200
        self.release()
