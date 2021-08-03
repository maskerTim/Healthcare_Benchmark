""" import module path
print(__name__)
"""

from sensors.handler.sensorHandler import SensorHandler
import threading
from actuators.actuatorFactory import ActuatorFactory
from networks.mqtt.callback.heartCallback import HeartCallback
import os
import logging
from apscheduler.schedulers.background import BlockingScheduler

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
        # create kinds of sensors
        self.sensorHR = SensorHandler('HR')
        self.sensorBP = SensorHandler('BP')
        self.sensorPO = SensorHandler('PO')
        self.sensorFT = SensorHandler('FT')
        # create kinds of actuators
        self.actuatorHA = ActuatorFactory('HA')

    def wearSensors(self):
        """ attaches the sensors on person """
        # ------ old version multithreading -----
        self.ID = threading.current_thread().ident
        # threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        # threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3, self.ip, self.port, self.lock))
        # threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7, self.ip, self.port, self.lock))
        # threadFT = threading.Thread(target=self.sensorFT.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        # self.threadManager.append(threadHR)
        # self.threadManager.append(threadBP)
        # self.threadManager.append(threadPO)
        # self.threadManager.append(threadFT)
        # ----- new version multithreading (add the Timer) -----
        threadHR = threading.Timer(5, self.sensorHR.execute,
                                   args=(self.ID, 5, self.ip, self.port, self.lock, self.sensorHR))
        threadBP = threading.Timer(3, self.sensorBP.execute,
                                   args=(self.ID, 3, self.ip, self.port, self.lock, self.sensorBP))
        threadPO = threading.Timer(2, self.sensorPO.execute,
                                   args=(self.ID, 2, self.ip, self.port, self.lock, self.sensorPO))
        # threadFT = threading.Timer(6, self.sensorFT.execute,
        #                            args=(self.ID, 3, self.ip, self.port, self.lock, self.sensorFT))
        self.threadManager.append(threadHR)
        self.threadManager.append(threadBP)
        self.threadManager.append(threadPO)
        # self.threadManager.append(threadFT)

    def wearActuators(self):
        self.actuatorHA.setOnConnect(HeartCallback.on_connect)
        self.actuatorHA.setOnMessage(HeartCallback.on_message)
        self.actuatorHA.connect(self.ip, 1881, "mqttSub")


    def operate(self):
        """ running the sensor instances """
        # ------ old version multithreading -----
        # for i in range(period):
        #     self.wearSensors()
        #     for t in self.threadManager:
        #         t.start()
        #     for t in self.threadManager:
        #         t.join()
        #     self.threadManager.clear()
        # ------ new version multithreading -----
        self.wearSensors()
        #self.wearActuators()
        for t in self.threadManager:
            t.start()