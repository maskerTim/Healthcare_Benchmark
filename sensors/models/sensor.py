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

    def read(self, ID, sleep, seed):
        """ simulate to read the value
        @param {
            ID: identification of which person wears
            sleep: interval time to read
            @deprecated seed: the probability between normal and abnormal
        }
        """
        pass

    def makeEvent(self, format):
        """ make the event to send out
        @param {
            format: the event format
        }
        """
        pass

    def connect(self, ip, port):
        """ the network functionalities
        connect:
            @param {ip: ip address, port: port number}
            @desc connect to the server/some machine
        """
        self.socket = socketClient.createSocket()
        self.socket.connect((ip, port))

    def close(self):
        """ the network functionalities
        close:
            @desc close the connection
        """
        self.socket.close()

    def send(self):
        """ the network functionalities
        send:
            @desc send the event to server/some machine
        """
        self.socket.send(self.event.encode(encoding="utf-8"))
        logging.info("Event: {}".format(self.event))