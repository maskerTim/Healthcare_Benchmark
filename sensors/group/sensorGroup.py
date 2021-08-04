""" import module path
print(__name__)
"""

from sensors.handler.sensorHandler import SensorHandler
from sensors.exceptions.noSensors import NoSensorsError
from sensors.sensorFactory import SensorFactory
import threading
from actuators.actuatorFactory import ActuatorFactory
from networks.mqtt.callback.heartCallback import HeartCallback
import os
import logging
from apscheduler.schedulers.background import BlockingScheduler


class SensorGroup:
    """
    Monitor the healthcare of person
    """

    def __init__(self, name, ip, port):
        # a set of sensors in the same group
        self.sensors = []
        # the group name
        self.name = name
        # set IP and Port to connect a server/broker
        self.ip = ip
        self.port = port
        # manage the threads
        self.threadManager = []
        # create a lock
        self.lock = threading.Lock()
        # create kinds of sensors
        # self.sensorHR = SensorHandler('HR')
        # self.sensorBP = SensorHandler('BP')
        # self.sensorPO = SensorHandler('PO')
        # self.sensorFT = SensorHandler('FT')
        # create kinds of actuators
        # self.actuatorHA = ActuatorFactory('HA')

    def setSensors(self, sensors):
        """ set sensors in one group and those have a handler that can operate """
        for sensor in sensors:
            self.sensors.append(SensorHandler(sensor))

    def setup(self):
        """ setup the configuration for sensors """
        # check the sensor group is not empty
        if self.sensors:
            ID = threading.current_thread().ident
            for sensor in self.sensors:
                self.threadManager.append(threading.Timer(sensor.getInterval(),
                                                          sensor.execute,
                                                          args=(
                                                          ID, sensor.getInterval(), self.ip, self.port, self.lock,
                                                          sensor)))
        else:
            raise NoSensorsError("Error: No sensors in group!!")

    """
    @deprecated
    """

    def wearSensors(self):
        """ attaches the sensors on person """
        # ------ old version multithreading -----
        # self.ID = threading.current_thread().ident
        # threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        # threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3, self.ip, self.port, self.lock))
        # threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7, self.ip, self.port, self.lock))
        # threadFT = threading.Thread(target=self.sensorFT.execute, args=(self.ID, 5, self.ip, self.port, self.lock))
        # self.threadManager.append(threadHR)
        # self.threadManager.append(threadBP)
        # self.threadManager.append(threadPO)
        # self.threadManager.append(threadFT)
        # ----- new version multithreading (add the Timer) -----
        # threadHR = threading.Timer(5, self.sensorHR.execute,
        #                            args=(self.ID, 5, self.ip, self.port, self.lock, self.sensorHR))
        # threadBP = threading.Timer(3, self.sensorBP.execute,
        #                            args=(self.ID, 3, self.ip, self.port, self.lock, self.sensorBP))
        # threadPO = threading.Timer(2, self.sensorPO.execute,
        #                            args=(self.ID, 2, self.ip, self.port, self.lock, self.sensorPO))
        # threadFT = threading.Timer(6, self.sensorFT.execute,
        #                            args=(self.ID, 3, self.ip, self.port, self.lock, self.sensorFT))
        # self.threadManager.append(threadHR)
        # self.threadManager.append(threadBP)
        # self.threadManager.append(threadPO)
        # self.threadManager.append(threadFT)

    """
    @deprecated
    """

    def wearActuators(self):
        """ attaches the actuators on person """
        # self.actuatorHA.setOnConnect(HeartCallback.on_connect)
        # self.actuatorHA.setOnMessage(HeartCallback.on_message)
        # self.actuatorHA.connect(self.ip, 1881, "mqttSub")

    def active(self):
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
        # self.wearSensors()
        # self.wearActuators()
        self.setup()
        for t in self.threadManager:
            t.start()
