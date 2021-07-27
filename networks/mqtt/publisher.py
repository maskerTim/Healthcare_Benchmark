import paho.mqtt.client as mqtt

class Publisher:
    def __init__(self):
        self.publisher = None

    def createPublisher(self):
        """ create a publisher instance """
        self.publisher = mqtt.Client()
        return self.publisher

    def publish(self, topic, message):
        pass