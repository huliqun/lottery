# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:35 2016

@author: huliqun
"""
import falcon

from workserver.util import GLBConfig
from workserver.service.ServiceBase import ServiceBase
from workserver.module.models import MatchInfoD
from workserver.util import SysUtil

class getMatchesResource(ServiceBase):
    def on_get(self, req, resp):
        self.initialize()
        
        matches = self.session.query(MatchInfoD).\
            filter(MatchInfoD.date==SysUtil.getTomorrow()).all()
            
        maData = []
        if matches:
            for m in matches:
                maData.append({'matchid': m.matchid,
                               'match': m.match,
                               'date': m.date.strftime('%Y-%m-%d'),
                               'matchTime': m.matchTime.strftime('%H:%M'),
                               'matchtype': m.matchtype,
                               'matchzhu': m.matchzhu,
                               'matchke': m.matchke,
                               'singleFlag': m.singleFlag,
                               'wrate': m.wrate,
                               'drate': m.drate,
                               'lrate': m.lrate,
                               'fixScore': m.fixScore,
                               'wrateS': m.wrateS,
                               'drateS': m.drateS,
                               'lrateS': m.lrateS})

        self.result['data'] = maData
        
        req.context['result'] = self.result
        resp.set_header('Powered-By', 'huliquns@126.com')
        resp.status = falcon.HTTP_200
        self.release()                           
                               


        
    