from .sensor import Sensor
from ..events.models.pulseOximeterEvent import PulseOximeterEvent
import datetime
import time
import random
import logging

class PulseOximeter(Sensor):
    """ Operation of Pulse Oximeter """

    def read(self, ID, sleep, seed):
        # normal range of heartbeat
        time.sleep(sleep)
        #logging.info("Pulse Oximeter read per {}...".format(sleep))
        self.ID = ID
        self.value = random.randint(95, 100)

    def makeEvent(self, format):
        self.event = PulseOximeterEvent({
            "ID": self.ID,
            "startTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
            "endTime": None,
            "dataType": "Pulse Oximeter",
            "valueType": "Int",
            "unit": "SpO2 (%)",
            "value": self.value
        })
        self.event = self.event.convert(format)