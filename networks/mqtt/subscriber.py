import paho.mqtt.client as mqtt

class Subscribe:
    """ The Subscriber class for MQTT"""
    def __init__(self):
        self.subscriber = None

    def createSubscriber(self):
        """ create a subscriber instance """
        self.subscriber = mqtt.Client()
        return self.subscriber

    def on_connect(self, client, userdata, flags, rc):
        """ when succeed to connect then execute """
        pass

    def on_message(self, client, userdata, msg):
        """ when succeed to receive from broker then execute """
        pass