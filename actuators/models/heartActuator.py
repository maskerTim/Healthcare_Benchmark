import logging
from .actuator import Actuator

class HeartActuator(Actuator):
    """ Actuator for heart rate"""
    def __init__(self):
        super().__init__()
        self.name = "Heart Actuator"
    @classmethod
    def do(self):
        logging.info("The Heart Actuator is executing...")