import logging
from networks.networkSelector import NetworkSelector
from multipledispatch import dispatch

class Sensor:
    """ Abstract class of sensor"""
    def __init__(self):
        # ID and value is set by read function
        self.ID = None
        self.value = 0
        # event is set by makeEvent function
        self.event = None
        self.ip = ""
        self.port = 0
        # the interval of execution per time
        self.interval = None
        # switch between the normal and abnormal value
        self.count = 0
        self.socket = None
        self.protocol = None

    def setInterval(self, interval):
        self.interval = interval

    def getInterval(self):
        return self.interval

    def read(self, ID):
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

    def connect(self, ip, port, protocol="socket"):
        """ the network functionalities
        connect:
            @param {ip: ip address, port: port number}
            @desc connect to the server/some machine
        """
        ns = NetworkSelector(protocol)
        self.protocol = protocol
        if "socket"==protocol:
            self.socket = ns.createSocket()
            self.socket.connect((ip, port))
        elif "mqttPub"==protocol:
            self.socket = ns.createPublisher()
            self.socket.connect(ip, port)

    def close(self):
        """ the network functionalities
        close:
            @desc close the connection
        """
        if "socket"==self.protocol:
            self.socket.close()
        elif "mqttPub"==self.protocol:
            self.socket.disconnect()

    @dispatch()
    def send(self):
        """ the network functionalities for tcp socket
        send:
            @desc send the event to server/some machine
        """
        self.socket.send(self.event.encode(encoding="utf-8"))
        logging.info("Event: {}".format(self.event))

    @dispatch(str)
    def send(self, topic):
        """ the network functionalities for mqtt
        send:
            @desc send the event to server/some machine
            @param {topic: the topic of mqtt}
        """
        self.socket.publish(topic, self.event.encode(encoding="utf-8"))
        logging.info("Event: {}".format(self.event))
