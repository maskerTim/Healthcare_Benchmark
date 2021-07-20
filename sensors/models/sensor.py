import logging
import networks.socket.client as socketClient


class Sensor:
    """ Interface of sensor"""
    def __init__(self):
        self.ID = None
        self.value = 0
        self.event = None
        self.ip = ""
        self.port = 0
        self.socket = None

    """ monitor the value of sensor"""
    def read(self, ID, sleep, seed):
        pass

    """ make the event data by some format (default=json)"""
    def makeEvent(self, format):
        pass

    """ 
        the network functionalities
        1. connect: connect to the server/some machine
        2. close: close the connection
        3. send: send the event to server/some machine
    """
    def connect(self, ip, port):
        self.socket = socketClient.createSocket()
        self.socket.connect((ip, port))

    def close(self):
        self.socket.close()

    def send(self):
        self.socket.send(self.event.encode(encoding="utf-8"))
        logging.info("Event: {}".format(self.event))