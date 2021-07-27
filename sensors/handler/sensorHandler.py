from ..sensorFactory import SensorFactory
import logging
import time

class SensorHandler:
    """
    Create some sensor by factory and Operate it
    """
    def __init__(self, sensor="HR"):
        self.sensorHandler = SensorFactory(sensor)

    def execute(self, ID, sleep, ip, port, lock, period=4, seed=0.7,  format='json'):
        """ running the senser instances
        @synchronized
        @param {
            ID: Identification of which person wears,
            sleep: interval time to read
            ip: ip address
            port: port number
            lock: thread lock for synchronization
            @deprecated seed: the probability between normal and abnormal
                @default 0.7
            period: how many round it executes
                @default 4
            format: the event format it finally sends
                @default json
        @err error to connect
        }
        """
        try:
            lock.acquire()
            logging.info("{}, Take the lock".format(ID))
            self.sensorHandler.connect(ip, port, "mqttPub")
            self.sensorHandler.read(ID, sleep, seed)
            self.sensorHandler.makeEvent(format)
            self.sensorHandler.send("Try/MQTT")
        except:
            logging.error("Error connection exception...")
        finally:
            #logging.info("sensorhandler finishes to run")
            #self.sensorHandler.close()
            #logging.info("{}, Close the connection".format(ID))
            lock.release()
            logging.info("{}, Release the lock".format(ID))
            #time.sleep(sleep)