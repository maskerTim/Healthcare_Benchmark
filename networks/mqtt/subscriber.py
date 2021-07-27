import paho.mqtt.client as mqtt

class Subscribe:
    """ The Subscriber class for MQTT"""
    def __init__(self):
        self.subscriber = None

    def createSubscriber(self):
        """ create a subscriber instance """
        self.subscriber = mqtt.Client()
        return self.subscriber

    def on_connect(self):
        """ when succeed to connect then execute """
        pass

    def on_message(self):
        """ when succeed to receive from broker then execute """
        pass