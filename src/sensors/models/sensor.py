import logging
import src.networks.socket.client as socketClient


class Sensor:
    """ Interface of sensor"""
    def __init__(self):
        self.ID = None
        self.value = 0
        self.event = None
        self.socket = None

    def read(self, ID, sleep, seed):
        pass

    def makeEvent(self, format):
        pass

    def connect(self):
        self.socket = socketClient.createSocket()
        self.socket.connect(("192.168.0.99", 9999))

    def close(self):
        self.socket.close()

    def send(self):
        self.socket.send(self.event.encode(encoding="utf-8"))
        logging.info("Event: {}".format(self.event))