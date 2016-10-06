# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:45:49 2016

@author: Administrator
"""
import urllib
from urllib.parse import urlencode
import http.cookiejar
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
import json

import sys
#sys.path.append('../..')
sys.path.append('/home/putbox/putboxserver')
import workserver.settings as settings
from workserver.util import SysUtil
from workserver.batch.BatchBase import BatchBase
from workserver.module.models import EDIExportShipInfo

class EDIExportShipQueryBatch(BatchBase):
    def run(self):
        err = 0
        ret = self.getWebData()
        while not ret:
            err += 1
            if err >= settings.spyderErrorTimes:
                self.logger.error('查询EDI数据超时')
                break
            time.sleep(settings.spyderDelayTime)
            ret = self.getWebData()
        
    def getWebData(self):
        try:
            urlpage = 'http://edi.easipass.com/dataportal/q.do?qn=dp_export_shipinfo'
            header_dict={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Upgrade-Insecure-Requests': '1',
                         'Cache-Control': 'max-age=0',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.8'}   
            cj = http.cookiejar.CookieJar()
            cookie_support = urllib.request.HTTPCookieProcessor(cj)  
            opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
            urllib.request.install_opener(opener) 
            reqpage = urllib.request.Request(urlpage, headers=header_dict, method='GET')
            response = urllib.request.urlopen(reqpage, timeout= settings.spyderTimeout)
            
            bgdate = (datetime.now() -  timedelta(days=30)).strftime('%Y%m%d')
            eddate = (datetime.now() +  timedelta(days=60)).strftime('%Y%m%d')
            data = {
                'vessel1': '',
                'voyage1': '',
                'imo_no1': '',
                'vessel1_cn': '',
                'vess_call1': '',
                'carr_code1': '',
                'ship_agen1': '',
                'berth1': '',
                'esti_sail1': bgdate,
                'esti_sail2': eddate,
                'qid': '402803af0ecb1a4c010ecb1bc2bb00a0',
                'pagesize': '30',
                'submit': '查询'}
            
            urlquery = 'http://edi.easipass.com/dataportal/query.do?' + urlencode(data)
            reqpage = urllib.request.Request(urlquery, headers=header_dict, method='GET')
            response = urllib.request.urlopen(reqpage, timeout= settings.spyderTimeout)
            the_page = response.read().decode('utf-8')
            soup = BeautifulSoup(the_page, 'html.parser')
            
            tables = soup.find_all('table')
            pagesize = int(re.search(r'第[\d]+页/共([\d]+)页', str(tables[5]) ).groups()[0])
            
        except Exception as e:
            SysUtil.exceptionPrint(self.logger, e)
            return False
            
        for page in range(0,pagesize):
            errCount = 0
            time.sleep(5)
            while errCount < settings.spyderErrorTimes:
                if errCount != 0:
                    time.sleep(5)
                try:
                    self.logger.info('总共:' + str(pagesize) + '当前:' +str(page))
                    data['pageNo'] = str(page)
                    urlquery = 'http://edi.easipass.com/dataportal/query.do?' + urlencode(data)
                    reqpage = urllib.request.Request(urlquery, headers=header_dict, method='GET')
                    response = urllib.request.urlopen(reqpage, timeout= settings.spyderTimeout)
                    the_page = response.read().decode('utf-8')
                    soup = BeautifulSoup(the_page, 'html.parser')
                    
                    tables = soup.find_all('table')
                    dataTRs = tables[4].find_all('tr')
                    for col in dataTRs[1:]:
                        tds = col.find_all('td')
                        ETD = tds[7].text.strip()
                        if ETD != 'NONE':
                            shipinfo = self.session.query(EDIExportShipInfo).\
                                filter(EDIExportShipInfo.shipEnName == tds[0].text.strip()).\
                                filter(EDIExportShipInfo.ETD == datetime.strptime(ETD, '%Y%m%d')).\
                                first()
                            if not shipinfo:
                                transitPortWeb = []
                                errTransitPortCount = 0
                                time.sleep(5)
                                while errTransitPortCount < settings.spyderErrorTimes:
                                    if errTransitPortCount != 0:
                                        time.sleep(5)
                                    try:
                                        transitPortWeb = []
                                        transitPortData = {
                                            'qn': 'dp_export_ship_info_port',
                                            'vessel': tds[0].text.strip(),
                                            'voyage': tds[3].text.strip(),
                                            'estisail': tds[7].text.strip()
                                        }
                                        transitPortUrlquery = 'http://edi.easipass.com/dataportal/query.do?' + urlencode(transitPortData)
                                        transitPortReqpage = urllib.request.Request(transitPortUrlquery, headers=header_dict, method='GET')
                                        transitPortResponse = urllib.request.urlopen(transitPortReqpage, timeout= settings.spyderTimeout)
                                        transitPort_the_page = transitPortResponse.read().decode('utf-8')
                                        transitPort_soup = BeautifulSoup(transitPort_the_page, 'html.parser')
                                        
                                        transitPort_tables = transitPort_soup.find_all('table')
                                        transitPort_dataTRs = transitPort_tables[4].find_all('tr')
                                        for col in transitPort_dataTRs[1:]:
                                            transitPorttds = col.find_all('td')
                                            row = {'code': transitPorttds[1].text.strip(),
                                                   'name': transitPorttds[0].text.strip()}
                                            transitPortWeb.append(row)
                                        break
                                    except Exception as e:
                                        print(e)
                                        SysUtil.exceptionPrint(self.logger, e)
                                        errTransitPortCount+=1
                                
                                shiprc = EDIExportShipInfo(
                                            shipEnName = tds[0].text.strip(),
                                            shipCnName = tds[1].text.strip(),
                                            callSign = tds[2].text.strip(),
                                            voyageNo = tds[3].text.strip(),
                                            ShipCoCode = tds[4].text.strip(),
                                            carrierName = '',
                                            carrierCode = tds[5].text.strip(),
                                            wharfName = tds[6].text.strip(),
                                            wharfCode = '',
                                            ETD = datetime.strptime(tds[7].text.strip(), '%Y%m%d'),
                                            IMO = tds[7].text.strip(),
                                            transitPort = json.dumps(transitPortWeb)
                                        )
                                self.session.add(shiprc)
                                self.session.flush()
                    self.session.commit()
                    break
                except Exception as e:
                    SysUtil.exceptionPrint(self.logger, e)
                    errCount+=1
        return True 
    
if __name__ == '__main__':  
    EDIExportShipQueryBatch().run()