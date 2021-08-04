import paho.mqtt.client as mqtt


class Subscribe:
    """ The Subscriber class for MQTT"""

    def __init__(self):
        self.subscriber = None

    def createSubscriber(self):
        """ create a subscriber instance """
        self.subscriber = mqtt.Client()
        return self.subscriber
