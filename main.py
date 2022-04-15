""" module path for search by python interpreter
import sys
print(sys.path)
"""

import os
from sensors.sensorFactory import SensorFactory
from sensors.group.sensorGroup import SensorGroup
from videos.videoFactory import VideoFactory
from videos.manager.videoManager import VideoManager
from actuators.actuatorFactory import ActuatorFactory
from actuators.group.actuatorGroup import ActuatorGroup

if __name__ == '__main__':
    load_dotenv()
    """ Sample of code for sensor benchmark """
    sensorHR = SensorFactory('HR')
    sensorHR.setInterval(5)
    sensorBP = SensorFactory('BP')
    sensorBP.setInterval(3)
    patient1 = SensorGroup('Patient1', "192.168.0.194", 1883)
    patient1.setSensors([sensorHR, sensorBP])
    patient1.do()
    # """ Sample code for video benchmark """
    # video = VideoFactory("CAM")
    # VM1 = VideoManager("Video", 1, "192.168.100.75", 1883, "HD720")
    # VM1.createVideos(video)
    # VM1.start()
    """ Sample code for actuator benchmark """
    # actuatorHA = ActuatorFactory("HA")
    # actuatorBA = ActuatorFactory("BA")
    # actuatorVA = ActuatorFactory("VA")
    # AG1 = ActuatorGroup("Actuator1", os.getenv("MQTT_BROKER_IP"), 1881)
    # AG1.setActuators([actuatorHA, actuatorBA, actuatorVA])
    # AG1.do()
    # print('Main Finish')




