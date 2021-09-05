""" import module path
print(__name__)
"""

from sensors.handler.sensorHandler import SensorHandler
from sensors.exceptions.noSensors import NoSensorsError
import threading
from configs.logConfig import Logger

logger = Logger.instance()


class SensorGroup:
    """
    Organize a set of sensors in one group
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
            logger.info("{} is ready...".format(self.name))
        else:
            raise NoSensorsError("Error: No sensors in group!!")

    def do(self):
        """ running the sensor instances """
        self.setup()
        for t in self.threadManager:
            t.start()
        logger.info("{} is running...".format(self.name))
