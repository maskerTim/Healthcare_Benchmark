from src.sensors.handler.sensorHandler import SensorHandler
import threading

class Person:
    """
    Monitor the healthcare of person
    """
    def __init__(self):
        self.threadManager = []
        self.sensorHR = SensorHandler('HR')
        self.sensorBP = SensorHandler('BP')
        self.sensorPO = SensorHandler('PO')
        

    def wearSensors(self):
        self.ID = threading.current_thread().ident
        threadHR = threading.Thread(target=self.sensorHR.execute, args=(self.ID, 5,))
        threadBP = threading.Thread(target=self.sensorBP.execute, args=(self.ID, 3,))
        threadPO = threading.Thread(target=self.sensorPO.execute, args=(self.ID, 7,))
        self.threadManager.append(threadHR)
        self.threadManager.append(threadBP)
        self.threadManager.append(threadPO)

    def operate(self):
        self.wearSensors()
        for t in self.threadManager:
            t.start()
