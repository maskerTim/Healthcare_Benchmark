from .sensor import Sensor
from ..events.models.heartRateEvent import HeartRateEvent
import datetime
import time
import random
import logging

class HeartRate(Sensor):
    """ Operation of Heart Rate """

    def read(self, ID, sleep, seed):
        # normal range of heartbeat
        time.sleep(sleep)
        #logging.info("Heart Rate read per {}...".format(sleep))
        self.ID = ID
        self.value = random.randint(60, 80)

    def makeEvent(self, format):
        self.event = HeartRateEvent({
            "ID": self.ID,
            "startTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
            "endTime": None,
            "dataType": "Heart Rate",
            "valueType": "Int",
            "unit": "Beats Per Minute (bpm)",
            "value": self.value
        })
        self.event = self.event.convert(format)