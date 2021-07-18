import time
import random
import logging
from .sensor import Sensor
import datetime
from ..events.models.bloodPressureEvent import BloodPressureEvent

class BloodPressure(Sensor):
    """ Operation of Blood Pressure """

    def read(self, ID, sleep, seed):
        # normal blood pressure
        time.sleep(sleep)
        #logging.info("Blood Pressure read per {}...".format(sleep))
        systolic = random.randint(90, 120)
        diastolic = random.randint(60, 80)
        self.ID = ID
        self.value = "{}/{}".format(systolic, diastolic)

    def makeEvent(self, format):
        self.event = BloodPressureEvent({
            "ID": self.ID,
            "startTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
            "endTime": None,
            "dataType": "Blood Pressure",
            "valueType": "String",
            "unit": "mmHg",
            "value": self.value
        })
        self.event = self.event.convert(format)