from .sensor import Sensor
from ..events.models.pulseOximeterEvent import PulseOximeterEvent
import datetime
import time
import random
import logging

class PulseOximeter(Sensor):
    """ Operation of Pulse Oximeter """
    def __init__(self):
        super().__init__()
        self.name = "PulseOximeter"

    def read(self, ID, sleep, seed):
        """ simulate to read the value
        @param {
            ID: identification of which person wears
            sleep: interval time to read
            @deprecated seed: the probability between normal and abnormal
        }
        """
        # normal range of heartbeat
        #time.sleep(sleep)
        #logging.info("Pulse Oximeter read per {}...".format(sleep))
        self.ID = ID
        if self.count < 5:
            self.value = random.randint(95, 100)
        elif self.count >= 5 and self.count < 15:
            self.value = random.randint(80, 94)
        else:
            self.value = random.randint(95, 100)
        self.count+=1
        if self.count > 25:
            self.count = 0

    def makeEvent(self, format):
        """ make the event to send out
        @param {
            format: the event format
        }
        """
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