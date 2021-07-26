""" import module path
print(__name__)
"""
import time

from sensors.handler.sensorHandler import SensorHandler
from videos.handler.videoHandler import VideoHandler
import threading
import os

class Person:
    """
    Monitor the healthcare of person
    """
    def __init__(self, ip, port):
        self.threadManager = []
        self.ip = ip
        self.port = port
        # create a lock
        self.lock = threading.Lock()
        self.sensorHR = SensorHandler('HR')
        self.sensorBP = SensorHandler('BP')
        self.sensorPO = SensorHandler('PO')
        self.sensorFT = SensorHandler('FT')

    def wearSensors(self):
        """ attaches the sensors on person """
        # old version multithreading
        self.ID = threading.current_thread().ident
        # new version multiprocessor
        # ID as processor ID
        #self.ID = os.getpid()
        threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3, self.ip, self.port, self.lock))
        threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7, self.ip, self.port, self.lock))
        threadFT = threading.Thread(target=self.sensorFT.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        self.threadManager.append(threadHR)
        self.threadManager.append(threadBP)
        self.threadManager.append(threadPO)
        self.threadManager.append(threadFT)

    def operate(self, period):
        """ running the sensor instances """
        print(os.getpid())
        for i in range(period):
            self.wearSensors()
            for t in self.threadManager:
                t.start()
            for t in self.threadManager:
                t.join()
            self.threadManager.clear()

