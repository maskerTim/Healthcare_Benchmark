from .sensor import Sensor
from ..events.models.heartRateEvent import HeartRateEvent
import datetime
import time
import random
import logging

class HeartRate(Sensor):
    """ Operation of Heart Rate """

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
        #logging.info("Heart Rate read per {}...".format(sleep))
        self.ID = ID
        if self.count < 5:
            self.value = random.randint(60, 80)
        elif self.count >= 5 and self.count < 15:
            self.value = random.randint(81, 90)
        else:
            self.value = random.randint(60, 80)
        self.count+=1

    def makeEvent(self, format):
        """ make the event to send out
        @param {
            format: the event format
        }
        """
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