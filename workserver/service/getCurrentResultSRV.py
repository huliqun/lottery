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
            filter(MatchData.date == SysUtil.getTomorrow()).\
            filter(MatchData.userid == req_para['userid']).\
            filter(MatchData.money > 0).all()
        maData = []
        if matches:
            for m in matches:
                matInfo = self.session.query(MatchInfoD).ilter(MatchInfoD.matchid == m.matchAID).first()
                maData.append({'match': m.matchAID,
                               'matchtype': matInfo.matchtype,
                               'zhu': matInfo.matchzhu,
                               'ke': matInfo.matchke,
                               'wrate': matInfo.wrate,
                               'drate': matInfo.drate,
                               'lrate': matInfo.lrate,
                               'result': m.matchAResult,
                               'money': m.money})
            self.result['data'] = maData
        else:
            self.errorReturn(GLBConfig.API_ERROR, '无数据.')
                
        req.context['result'] = self.result
        resp.set_header('Powered-By', 'huliquns@126.com')
        resp.status = falcon.HTTP_200
        self.release()
