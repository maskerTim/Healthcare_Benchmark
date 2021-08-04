import logging
from .actuator import Actuator
import os

class HeartActuator(Actuator):
    """ Actuator for heart rate"""

    def __init__(self):
        super().__init__()
        self.name = "HeartActuator"

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("{}/{}".format(os.getenv("MQTT_TOPIC_ACTUATOR_PREFIX"), self.name))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode('utf-8'))
        HeartActuator.do()

    @classmethod
    def do(cls):
        logging.info("The Heart Actuator is executing...")
