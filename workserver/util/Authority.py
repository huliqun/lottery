# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:13:02 2016

@author: huliqun
"""

import falcon
import logging

from workserver.util import Security
from workserver.util import GLBConfig

class AuthMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger('serverLog')
        
    def process_request(self, req, resp):
        authCheckFlag = self.AuthEscape(req)

        if authCheckFlag is None:
            self.logger.info('authCheckFlag')
            raise falcon.HTTPError(falcon.HTTP_703,
                   'API error',
                   'Please make sure your api is correct.')

        if authCheckFlag:
            user = Security.token2user(req,self.logger)
            
            if user is None:
                self.logger.info('UNAUTHORIZED')
                raise falcon.HTTPError(falcon.HTTP_401,
                   'UNAUTHORIZED',
                   'Auth Failed or session expired')
            req.context['user'] = user
