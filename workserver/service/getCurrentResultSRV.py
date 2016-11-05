# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon
import datetime

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import MatchData, MatchInfoD
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
                    maData.append({'match': m.matchAID,
                       'matchtype': matInfo.matchtype,
                       'zhu': matInfo.matchzhu,
                       'ke': matInfo.matchke,
                       'wrate': matInfo.wrate,
                       'drate': matInfo.drate,
                       'lrate': matInfo.lrate,
                       'result': m.matchAResult,
                       'money': m.money})
                else:
                    mA = self.session.query(MatchInfoD).filter( MatchInfoD.matchid == m.matchAID ).first()
                    mB = self.session.query(MatchInfoD).filter( MatchInfoD.matchid == m.matchBID ).first()
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
                    
            self.result['data'] = maData
        else:
            self.errorReturn(GLBConfig.API_ERROR, '无数据.')
                
        req.context['result'] = self.result
        resp.set_header('Powered-By', 'huliquns@126.com')
        resp.status = falcon.HTTP_200
        self.release()
