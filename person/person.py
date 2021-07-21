""" import module path
print(__name__)
"""

from sensors.handler.sensorHandler import SensorHandler
from videos.handler.videoHandler import VideoHandler
from resources.resource import resources_config
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
        self.filelist = resources_config["files"]
        self.videoUS = VideoHandler("US")
        """
        self.sensorHR = SensorHandler('HR')
        self.sensorBP = SensorHandler('BP')
        self.sensorPO = SensorHandler('PO')
        self.sensorFT = SensorHandler('FT')
        """

    def wearSensors(self):
        # old version multithreading
        #self.ID = threading.current_thread().ident
        # new version multiprocessor
        self.ID = os.getpid()
        self.videoUS.openAndRecordVideo(resources_config["files"][0])
        threadUS = threading.Thread(target=self.videoUS.play, args=(self.ID, self.ip, self.port))
        self.threadManager.append(threadUS)
        """
        threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5, self.ip, self.port,))
        threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3, self.ip, self.port,))
        threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7, self.ip, self.port,))
        threadFT = threading.Thread(target=self.sensorFT.execute, args=(self.ID, 5, self.ip, self.port,))
        self.threadManager.append(threadHR)
        self.threadManager.append(threadBP)
        self.threadManager.append(threadPO)
        self.threadManager.append(threadFT)
        """

    def operate(self, _):
        print(os.getpid())
        self.wearSensors()
        for t in self.threadManager:
            t.start()
