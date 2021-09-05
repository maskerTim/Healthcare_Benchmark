from configs.logConfig import Logger
import threading
import os

logger = Logger.instance()


class SensorHandler:
    """
    Create some sensor by factory and Operate it
    """

    def __init__(self, sensor):
        self.sensorHandler = sensor

    def register(self, sensor):
        self.sensorHandler = sensor

    def getInterval(self):
        return self.sensorHandler.getInterval()

    def execute(self, ID, interval, ip, port, lock, sensor, format='json'):
        """ running the senser instances
        @synchronized
        @param {
            ID: Identification of which person wears,
            sleep: interval time to read
            ip: ip address
            port: port number
            lock: thread lock for synchronization
            sensor: sensor instance itself for implementing the repeated execution
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
            logger.info("{}, Take the lock".format(ID))
            self.sensorHandler.connect(ip, port, "mqttPub")
            self.sensorHandler.read(ID)
            self.sensorHandler.makeEvent(format)
            self.sensorHandler.send("{}/{}".format(os.getenv("MQTT_TOPIC_SENSOR_PREFIX"), self.sensorHandler.name))
        except Exception as e:
            logger.error("Error: {}".format(e))
        finally:
            self.sensorHandler.close()
            logger.info("{}, Close the connection".format(ID))
            lock.release()
            logger.info("{}, Release the lock".format(ID))
            # time.sleep(sleep)
            threading.Timer(interval, sensor.execute, args=(ID, interval, ip, port, lock, sensor)).start()
