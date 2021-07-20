import time
import random
import logging
from .sensor import Sensor
import datetime
from ..events.models.foreheadTemperatureEvent import ForeheadTemperatureEvent

class ForeheadTemperature(Sensor):
    """ Operation of Blood Pressure """

    def read(self, ID, sleep, seed):
        # normal blood pressure
        time.sleep(sleep)
        #logging.info("Temperature read per {}...".format(sleep))
        temperature = random.uniform(35.4, 37.4)
        self.ID = ID
        self.value = temperature

    def makeEvent(self, format):
        self.event = ForeheadTemperatureEvent({
            "ID": self.ID,
            "startTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
            "endTime": None,
            "dataType": "Forehead Temperature",
            "valueType": "Double",
            "unit": "Celsius",
            "value": self.value
        })
        self.event = self.event.convert(format)