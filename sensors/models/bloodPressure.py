import time
import random
import logging
from .sensor import Sensor
import datetime
from ..events.models.bloodPressureEvent import BloodPressureEvent

class BloodPressure(Sensor):
    """ Operation of Blood Pressure """

    def read(self, ID, sleep, seed):
        """ simulate to read the value
        @param {
            ID: identification of which person wears
            sleep: interval time to read
            @deprecated seed: the probability between normal and abnormal
        }
        """
        # normal blood pressure
        #time.sleep(sleep)
        #logging.info("Blood Pressure read per {}...".format(sleep))
        if self.count < 5:
            systolic = random.randint(90, 120)
            diastolic = random.randint(60, 80)
        elif self.count >= 5 and self.count <= 15:
            systolic = random.randint(121, 130)
            diastolic = random.randint(81, 90)
        else:
            systolic = random.randint(90, 120)
            diastolic = random.randint(60, 80)
        self.ID = ID
        # self.value = "{}/{}".format(systolic, diastolic)
        self.value = systolic
        self.count+=1
        if self.count > 25:
            self.count = 0

    def makeEvent(self, format):
        """ make the event to send out
        @param {
            format: the event format
        }
        """
        self.event = BloodPressureEvent({
            "ID": self.ID,
            "startTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
            "endTime": None,
            "dataType": "Blood Pressure",
            "valueType": "Int",
            "unit": "mmHg",
            "value": self.value
        })
        self.event = self.event.convert(format)