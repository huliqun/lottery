# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:45:49 2016

@author: Administrator
"""
import threadpool 
import datetime
from sqlalchemy import distinct

import sys
#sys.path.append('../..')
sys.path.append('/home/putbox/putboxserver')
from workserver.util import SysUtil
from workserver.util.putBox import util
from workserver.util import GLBConfig
from workserver.batch.BatchBase import BatchBase
from workserver.module.models import TrunkList, BLN2CarrierMissmatch, CarrierInfo
from workserver.util.putBox import informationQuery
from workserver.util.preplanQuery import preplanQuery

class trunkListQueryBatch(BatchBase):
    def run(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
        trunks = self.session.query(distinct(TrunkList.billLodingNo)).\
                    filter(TrunkList.status == GLBConfig.TRANKSTATUS_SUBMIT).\
                    filter(TrunkList.webQueryCount < 10).\
                    filter(TrunkList.webQueryFlag == GLBConfig.WEBQ_NO).\
                    filter(TrunkList.dataStatus == GLBConfig.ENABLE).\
                    filter(TrunkList.maketime > yesterday).all()
        billLodingNoList = [ item[0] for item in trunks]
        pool = threadpool.ThreadPool(10)
        
        requests = threadpool.makeRequests(self.updateTrunkList, billLodingNoList) 
        [pool.putRequest(req) for req in requests] 
        pool.wait()
#        self.updateTrunkList(billLodingNoList[0])
        
    def updateTrunkList(self, billLodingNo):
        workSession = self.db()
        try:
            yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
            trunkLists = workSession.query(TrunkList).\
                filter(TrunkList.status == GLBConfig.TRANKSTATUS_SUBMIT).\
                filter(TrunkList.webQueryFlag == GLBConfig.WEBQ_NO).\
                filter(TrunkList.dataStatus == GLBConfig.ENABLE).\
                filter(TrunkList.maketime > yesterday).\
                filter(TrunkList.billLodingNo == billLodingNo).with_lockmode('update').all()
            CarrierCodeList = informationQuery.billLodingNo2CarrierCodeQuery(billLodingNo)
            
#           查不到船代
            if not CarrierCodeList:
                self.logger.info('rules not exist' + billLodingNo)
                mismatch = BLN2CarrierMissmatch(billLodingNo = billLodingNo,
                                                errMessage = 'rules not exist')
                workSession.add(mismatch)
            else:
                CarrierCode = ''
                BLNInfo = []
#               只匹配到一个船代
                if len(CarrierCodeList) == 1:
                    CarrierCode = CarrierCodeList[0]
                    BLNInfo = preplanQuery(self.logger, workSession).preplanQuery(CarrierCode,{'billLodingNo': billLodingNo})                        
                else:
                    for item in CarrierCodeList:
                        info = preplanQuery(self.logger, workSession).preplanQuery(CarrierCode,{'billLodingNo': billLodingNo}) 
                        if info:
                            CarrierCode = item
                            BLNInfo = info
                            break
                if len(trunkLists) != len(BLNInfo):
                    self.logger.info('登记数量与网页查询的不一致:' + str(len(trunkLists)) +', ' + str(len(BLNInfo)) +', ' + billLodingNo)
                    mismatch = BLN2CarrierMissmatch(billLodingNo = billLodingNo,
                                                    errMessage = '登记数量与网页查询的不一致:' + str(len(trunkLists)) +', ' + str(len(BLNInfo)),
                                                    data = str(BLNInfo))
                    workSession.add(mismatch)
#               找到船代

                if CarrierCode != '':
                    carrier = workSession.query(CarrierInfo).filter(CarrierInfo.code == CarrierCode).first()
                    if carrier is None:
                        self.logger.error('carrier do not exist' + billLodingNo + ' code:' + CarrierCode)
                    else:                        
#                       更新抓取信息
                        updateCount = 0
                        for tk in trunkLists:
                            for item in BLNInfo:
                                if 'containerType' in item and 'containerSize' in item:
                                    if item['containerType'] == util.getContainerTypeName(tk.containerType) and item['containerSize'] == util.getContainerSizeName(tk.containerSize):
                                        tk.webQueryFlag = GLBConfig.WEBQ_SUCCESS
                                        tk.sameFlag = GLBConfig.TRUE
                                        tk.containerTypeWeb = item['containerType']
                                        tk.containerSizeWeb = item['containerSize']
                                        tk.containerCountWeb = item['containerCount']
                                        if 'shipName' in item:
                                            tk.shipNameWeb = item['shipName']
                                            if tk.shipNameWeb != tk.shipName:
                                                tk.sameFlag = GLBConfig.FALSE
                                                
                                        if 'voyageNo' in item:
                                            tk.voyageNoWeb = item['voyageNo']
                                            if tk.voyageNoWeb != tk.voyageNo:
                                                tk.sameFlag = GLBConfig.FALSE
                                                
                                        if 'containerCount' in item:
                                            if item['containerCount'] != tk.containerCount:
                                                tk.sameFlag = GLBConfig.FALSE
                                                
                                        if 'transportationHub' in item:
                                            tk.transportationHubWeb = item['transportationHub']
                                        if 'destinationPort' in item:
                                            tk.destinationPortWeb = item['destinationPort']

                                        updateCount += 1
                                        
                        if updateCount != len(BLNInfo):
                            self.logger.info('更新数量与preplanQuery查询结果不一致' + billLodingNo)
                            mismatch = BLN2CarrierMissmatch(billLodingNo = billLodingNo,
                                                            errMessage = '更新数量与preplanQuery查询结果不一致',
                                                            data = str(BLNInfo))
                            workSession.add(mismatch)
                        
#                        更新费用
                        queryPara = {'OID': tk.OID, 'carManagerID': tk.carManagerID, 'carrierID': tk.carrierID, 'cond1': GLBConfig.PBCG_LH_01,
                                     'containerType': tk.containerType, 'containerSize': tk.containerSize, 'containerCount': tk.containerCount}
                        if tk.logisticsHitCharge == 0:
                            tk.logisticsHitCharge = informationQuery.logisticsHitChargeQuery(workSession, queryPara)
                        
                        if tk.serviceCharge == 0:
                            tk.serviceCharge = informationQuery.serviceChargeQuery(workSession, queryPara)
                        
                        if tk.carrierID != carrier.userID:
                            tk.carrierIDB = tk.carrierID
                            tk.carrierID = carrier.userID
                            tk.operatorID = informationQuery.Carrier2OperatorQuery(workSession, tk.OID, tk.carrierID, '')
                            tk.putterID  = informationQuery.Carrier2PutterQuery(workSession, tk.OID, carrier.userID, '')
                            tk.sameFlag = GLBConfig.FALSE
                            
                        tk.modifytime = datetime.datetime.now()
                        tk.webQueryCount += 1
                else:
                    for tk in trunkLists:
                        tk.webQueryCount += 1
                    self.logger.info('preplanQuery no date ' + billLodingNo)
            
            workSession.commit()
        except Exception as ex:
            SysUtil.exceptionPrint(self.logger, ex)
            self.logger.error('billLodingNo do not exists' + billLodingNo)
            workSession.rollback()
    
        
if __name__ == '__main__':  
    trunkListQueryBatch().run()