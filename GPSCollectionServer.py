# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:58:37 2016

@author: Huliqun
"""

import asyncore
import datetime
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json

import workserver.deamons.GPSCollection.GPSInfoAnalysis as GPSInfoAnalysis
from workserver.module.models import CarGPSDetails
import workserver.settings as settings

logger = logging.getLogger('GPSLog')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(settings.gps_log)#_'+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

engine_handle = create_engine(settings.dbUrl,echo=settings.dbEchoFlag)
db_handle = scoped_session(sessionmaker(bind=engine_handle))

carids={}
lastactive={}

class WorkHandler(asyncore.dispatcher_with_send):
    global carids
    global lastactive

    def __init__(self, sock, addr):
        super(WorkHandler, self).__init__(sock=sock)
        self._addr = addr

    def handle_read(self):
        # self.request is the TCP socket connected to the client
        self._session = db_handle()
        clientid = ':'.join( str(x) for x in self._addr)
        try:
            dataHead = self.recv(3)
        except Exception as ex:
            logger.error(ex)
            logger.error("get message error")
            self.close()
            self._session.close()
            return

        length = 0
        if len(dataHead) > 0:
            if int(dataHead[0])==120 and int(dataHead[1])==120: #0x78 0x78
                length = int(dataHead[2])
                # get the following bytes
                data = self.recv(length+2)
                if len(data) > 0:
                    if int(data[0]) == 1:#login packet
                        carid = ''.join(['%02x'%x for x in data[1:9]])
                        logger.info("get login packet from carid: "+carid)
                        carids[clientid] = carid
                        lastactive[clientid] = datetime.datetime.now()
                        record = [0x78, 0x78, 0x05, 0x01, data[-6], data[-5], 0x00, 0x00, 0x0d, 0x0a]
                        self.send('C*'.encode())
                    elif int(data[0]) == 19:#heart beat packet
                        try:
                            carid = carids[clientid]
                            logger.info( ' get heartbeat packet from car:' + clientid )
                            lastactive[clientid] = datetime.datetime.now()
                            record = [0x78, 0x78, 0x05, 0x01, data[-6], data[-5], 0x00, 0x00, 0x0d, 0x0a]
                            self.send('C*'.encode())
                        except Exception as ex:
                            logger.error(ex)
                            logger.info(clientid + ' has not logged in yet!')
                    elif int(data[0]) == 18:#gps packet
                        try:
                            carid = carids[clientid]
                            logger.info( ' get gps packet from car:' + clientid )
                            lastactive[clientid] = datetime.datetime.now()
                            bjtime = self.get_bjtime(data[1:7])
                            gpson = self.get_gpson(data[17])
                            if gpson==1:
                                latitude = self.get_lat(data[8:12], data[17])
                                longitude = self.get_long(data[12:16], data[17])
                                speed = int(data[16])
                                course = self.get_course(data[17:19])
                                gpsMsg = "%f,%f"%(longitude, latitude)
                                for index in range(0, 4):
                                    baiduCoordinate = self.ConvertCoordBaidu(gpsMsg)
                                    index += 1
                                    if baiduCoordinate is not None:
                                        break
                                if baiduCoordinate is not None:
                                    record = [carid, bjtime, gpsMsg, speed, course, baiduCoordinate]
                                    self.saveRecord(record)
                                    gpsAna = GPSInfoAnalysis(self._session, record, logger)
                                    gpsAna.gpsAnalysis()
                                
                            else:
                                logger.info('no valid gps for car: ' + carid)
                            self.send('C*'.encode())
                        except Exception as ex:
                            logger.error(ex)
                            logger.info(clientid + ' has not logged in yet!')
        else:
            self.close()
        self._session.close()

    def handle_close(self):
        clientid = ':'.join( str(x) for x in self._addr)
        #logger.info(clientid + ".Finishi work.")
        if clientid in carids.keys():
            logger.info(clientid + ".Finishi work.")
            carids.pop(clientid)
            lastactive.pop(clientid)

    def get_bjtime(self, timearray):
        year=int("20"+str(timearray[0]))
        month=timearray[1]
        day=timearray[2]
        hour=timearray[3]
        min=timearray[4]
        sec=timearray[5]

        time = datetime.datetime(year, month, day, hour, min, sec)
        return time

    def get_gpson(self, byte):
        gpson = (byte>>4)&0x1
        return gpson

    def get_lat(self, array, dir):
        dir=-1 if ((dir>>2)&0x1)==0 else 1
        coord=((array[3]+array[2]*256+array[1]*256*256+array[0]*256*256*256))/30000/60
        coord=coord*dir
        return coord

    def get_long(self, array, dir):
        dir=-1 if ((dir>>3)&0x1)==1 else 1
        coord=((array[3]+array[2]*256+array[1]*256*256+array[0]*256*256*256))/30000/60
        coord=coord*dir
        return coord

    def get_course(self, array):
        course=array[1]+256*(array[0]&0x3)
        return course

    def saveRecord(self, message): #[carid, bjtime, gpsMsg, speed, course, baiduCoordinate]
        try:
            record = CarGPSDetails(bmfVersion = 0,
                        typeId = 118820114,
                        active = 'Y',
                        createdOn = message[1],
                        updatedOn = message[1],
                        equipmentNo = message[0],
                        direction = str(message[4]),
                        gps = message[2],
                        speed = str(message[3]),
                        time = message[1],
                        baiduCoordinate = message[5])
            self._session.add(record)
            self._session.commit()
        except Exception as ex:
            logger.error(ex)
            logger.error('write db error!')

    def ConvertCoordBaidu(self,gps):
        try:
            r = requests.get('http://api.map.baidu.com/geoconv/v1/?coords='+gps+'&ak=uDPSbtnuxVgBgacG7bnOSZhV', timeout=1)
            jsonData = json.loads(r.text)
            return str(jsonData['result'][0]['x'])+','+str(jsonData['result'][0]['y'])
        except Exception as ex:
            logger.error(ex)
            return None

class GPSServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(200)

    def handle_accepted(self, sock, addr):
#        print('Incoming connection from %s' % repr(addr))
        handler = WorkHandler(sock, addr)

if __name__ == "__main__":
    server = GPSServer('192.168.2.245', 7000)
    asyncore.loop()
