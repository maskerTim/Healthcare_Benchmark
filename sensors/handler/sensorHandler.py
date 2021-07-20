from ..sensorFactory import SensorFactory
import logging
import time

class SensorHandler:
    """
    Create some sensor by factory and Operate it
    """
    def __init__(self, sensor="HR"):
        self.sensorHandler = SensorFactory(sensor)

    def execute(self, ID, sleep, ip, port, seed=0.7, period=4, format='json'):
        try:
            self.sensorHandler.connect(ip, port)
            for _ in range(period):
                self.sensorHandler.read(ID, sleep, seed)
                self.sensorHandler.makeEvent(format)
                self.sensorHandler.send()
        except:
            logging.error("Error connection exception...")
        finally:
            #logging.info("sensorhandler finishes to run")
            time.sleep(5)
            self.sensorHandler.close()