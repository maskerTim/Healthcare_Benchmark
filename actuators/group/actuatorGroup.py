""" import module path
print(__name__)
"""


import threading
import logging
from actuators.handler.actuatorHandler import ActuatorHandler
from actuators.exceptions.NoActuators import NoActuatorsError


class ActuatorGroup:
    """
    Organize a set of sensors in one group
    """

    def __init__(self, name, ip, port, protocol="mqttSub"):
        # a set of actuators in the same group
        self.actuators = []
        # the group name
        self.name = name
        # set IP and Port to connect a server/broker
        self.ip = ip
        self.port = port
        self.protocol = protocol
        # manage the threads
        self.threadManager = []

    def setActuators(self, actuators):
        """ set actuators in one group and those have a handler that can operate """
        for actuator in actuators:
            self.actuators.append(ActuatorHandler(actuator))

    def setup(self):
        if self.actuators:
            for actuator in self.actuators:
                self.threadManager.append(threading.Thread(target=actuator.execute, args=(
                    self.ip, self.port, self.protocol
                )))
            logging.info("{} is ready...".format(self.name))
        else:
            raise NoActuatorsError("Error: no actuators in group")

    def do(self):
        """ running the sensor instances """
        self.setup()
        for t in self.threadManager:
            t.start()
        logging.info("{} is running...".format(self.name))
