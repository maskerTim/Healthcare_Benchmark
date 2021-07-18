from src.sensors.handler.sensorHandler import SensorHandler
import threading

class Person:
    """
    Monitor the healthcare of person
    """
    def __init__(self, ip, port):
        self.threadManager = []
        self.ip = ip
        self.port = port
        self.sensorHR = SensorHandler('HR')
        self.sensorBP = SensorHandler('BP')
        self.sensorPO = SensorHandler('PO')
        self.sensorFT = SensorHandler('FT')

    def wearSensors(self):
        self.ID = threading.current_thread().ident
        threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5, self.ip, self.port,))
        threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3, self.ip, self.port,))
        threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7, self.ip, self.port,))
        threadFT = threading.Thread(target=self.sensorFT.execute, args=(self.ID, 5, self.ip, self.port,))
        self.threadManager.append(threadHR)
        self.threadManager.append(threadBP)
        self.threadManager.append(threadPO)
        self.threadManager.append(threadFT)

    def operate(self):
        self.wearSensors()
        for t in self.threadManager:
            t.start()
