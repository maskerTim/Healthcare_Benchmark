""" module path for search by python interpreter
import sys
print(sys.path)
"""
import os

from configs import logConfig
from person.manager.personManager import PersonManager
from sensors.sensorFactory import SensorFactory
from sensors.group.sensorGroup import SensorGroup
from dotenv import load_dotenv
from videos.manager.videoManager import VideoManager
from resources.resource import resources_configs

if __name__ == '__main__':
    """ the entry point of program """
    logConfig.config()
    load_dotenv()
    sensorHR = SensorFactory('HR')
    sensorHR.setInterval(5)
    sensorBP = SensorFactory('BP')
    sensorBP.setInterval(3)
    patient1 = SensorGroup('Patient1', '192.168.100.75', 1882)
    patient1.setSensors([sensorHR, sensorBP])


    #VM1 = VideoManager(1, "192.168.0.99", 1883, "HD720")
    #VM1.start()
    #PM1 = PersonManager(2, os.getenv("MQTT_BROKER_SENSOR_IP"), 1882)
    #PM2 = PersonManager(2, "192.168.0.99", 1882)
    #PM1.start()
    #PM2.start()
    #PM3 = PersonManager(1, "192.168.0.99", 9999)
    #PM3.start()
    print('Main Finish')




