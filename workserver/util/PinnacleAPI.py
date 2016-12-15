# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:17:46 2016

@author: Administrator
"""
import base64
import urllib
import http
import json

from . import SysUtil

APIHOST = 'api.pinnacle.com'
GLB_TIMEOUT = 10
username = 'LH874811'
password = '!55286668hlq'

def authorization(usr, pwd):
    return 'Basic ' + base64.b64encode((usr + ':' + pwd).encode(encoding="utf-8")).decode()
    
def GetSportsV1(logger = None):
    try:
        headers = {'Authorization': authorization(username, password)}       
        host = APIHOST
        url = '/v1/sports'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url, '', headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        print(response.read().decode())
        conn.close()
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None

def GetSportsV2(logger = None):
    try:
        headers = {'Authorization': authorization(username, password)}
    #    params = {'username':'xxxx'}        
    #    data = urllib.urlencode(params)        
        host = APIHOST
        url = '/v2/sports'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None

def GetLeaguesV1(sportid ,logger = None):
    try:
        headers = {'Authorization': authorization(username, password)} 
        params = {'SportID': sportid}        
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/leagues?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        print(response.read().decode())
        conn.close()
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetLeaguesV2(sportId ,logger = None):
    try:
        headers = {'Authorization': authorization(username, password)} 
        params = {'SportID': sportId}        
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v2/leagues?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetFixtures(sportId, leagueIds=[], since=None, islive=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if since:
            params['since'] = since
        if islive:
            params['islive'] = islive
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/fixtures?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
    
def GetSettledFixtures(sportId, leagueIds=[], since=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if since:
            params['since'] = since
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/fixtures/settled?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetSpecialFixtures(sportId, leagueIds=[], category=None, eventId=None, specialId=None, since=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if category:
            params['category'] = category
        if eventId:
            params['eventId'] = eventId
        if specialId:
            params['specialId'] = specialId
        if since:
            params['since'] = since
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/fixtures/special?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetSettledSpecialFixtures(sportId, leagueIds=[], since=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if since:
            params['since'] = since
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/fixtures/special/settled?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetTeaserGroups(oddsFormat, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {'oddsFormat': oddsFormat}
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/teaser/groups?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetOdds(sportId, leagueIds=[], since=None, islive=None, oddsFormat=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if since:
            params['since'] = since
        if islive:
            params['islive'] = islive
        if oddsFormat:
            params['oddsFormat'] = oddsFormat
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/odds?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetOddsParlay(sportId, leagueIds=[], since=None, islive=None, oddsFormat=None, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {}
        if sportId:
            params['sportId'] = sportId
        if leagueIds:
            params['leagueIds'] = ','.join(leagueIds)
        if since:
            params['since'] = since
        if islive:
            params['islive'] = islive
        if oddsFormat:
            params['oddsFormat'] = oddsFormat
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/odds/parlay?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None
        
def GetTeaserOdds(teaserId, logger=None):
    try:
        headers = {'Authorization': authorization(username, password)}
        params = {'teaserId': teaserId}
        data = urllib.parse.urlencode(params)        
        host = APIHOST
        url = '/v1/odds/teaser?'
        conn = http.client.HTTPSConnection(host, timeout=GLB_TIMEOUT)
        conn.request('GET', url + data, '', headers)
        response = conn.getresponse()
        rspjson = json.loads(response.read().decode())
        conn.close()
        return rspjson
    except Exception as ex:
        SysUtil.exceptionPrint(logger, ex)
        return None

    