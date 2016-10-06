# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:07 2016

@author: huliqun
"""
import unittest

from falcon import testing

import sys
sys.path.append('..')
from MainServer import app
from testing.common import auth
  
class TestCAPTCHATrans(testing.TestCase):  
  
    def setUp(self):  
        self.api = app
  
    def test_post_get_list(self):  
        print('tttt')
        headers = {'content-type':'application/json'}
#        'Authorization': auth.getAuthToken(self,'admin','admin')}
        body = '{}'
        print('dfffff')
        result = self.simulate_post('/api/putbox/putBoxFixedControl',query_string='method=searchActByWeixin', headers=headers,body=body) 
        print('dddd')
        print(result.json)
        self.assertEqual(result.status_code, 200) 

if __name__ == '__main__':  
    unittest.main()        