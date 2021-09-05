import json
import sys

sys.path.append(r'/home/maskertim/Desktop/Healthcare_Benchmark')

import unittest
from sensors.sensorFactory import SensorFactory
from sensors.group.sensorGroup import SensorGroup
from actuators.actuatorFactory import ActuatorFactory


class SensorUnitCase(unittest.TestCase):
    def test_single_sensor(self):
        """
        Test a single sensor (10 times)
        """
        events = []
        # create Sensor of Heart Rate
        sensorHR = SensorFactory('HR')
        # sensor read with interval
        sensorHR.setInterval(3)
        for _ in range(10):
            sensorHR.read("50021")
            # convert to event format (e.g., json format)
            sensorHR.makeEvent('json')
            events.append(sensorHR.event)
        # the number of events is correct
        self.assertEqual(len(events), 10)  # add assertion here
        # the name is heart rate
        eventDict = json.loads(events[0])
        self.assertEqual(eventDict['dataType'], 'Heart Rate')

    def test_single_actuator(self):
        """
        Test a single actuator
        """
        actuatorHA = ActuatorFactory('HA')
        try:
            for _ in range(10):
                actuatorHA.do()
            # if not raise an exception, the procedure is running successfully
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False)

    def test_single_producer(self):
        """
        Test a single producer (Sensor->If...else...->Actuator)
        """
        events = []
        sensorHR = SensorFactory('HR')
        sensorHR.setInterval(3)
        actuatorHA = ActuatorFactory('HA')
        for _ in range(10):
            # sensor reads the value
            sensorHR.read("50020")
            sensorHR.makeEvent('json')
            events.append(sensorHR.event)
            eventDict = json.loads(sensorHR.event)
            # if detecting the abnormal state, trigger the actuator
            if eventDict['value'] > 80:
                actuatorHA.do()
                self.assertTrue(True)
                self.assertEqual(eventDict['dataType'], 'Heart Rate')
            else:
                self.assertFalse(False)
                self.assertEqual(eventDict['dataType'], 'Heart Rate')
        # check all events are collected
        self.assertEqual(len(events), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
