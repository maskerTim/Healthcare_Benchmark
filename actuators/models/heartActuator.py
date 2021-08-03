import logging
from .actuator import Actuator

class HeartActuator(Actuator):
    """ Actuator for heart rate"""
    def __init__(self):
        super().__init__()
        self.name = "HeartActuator"

    @classmethod
    def do(cls):
        logging.info("The Heart Actuator is executing...")