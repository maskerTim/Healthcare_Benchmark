import logging
from networks.networkSelector import NetworkSelector
from multipledispatch import dispatch
import cv2


class Video:
    """ Interface of video"""
    def __init__(self):
        self.ID = None
        self.ip = ""
        self.port = 0
        self.cap = None
        self.socket = None
        self.protocol = None
        self.frames = []

    def setID(self, ID):
        """ Set the Identification
        @param {ID: the identification of video instance}
        """
        self.ID = ID

    """ the network functionalities
    1. connect:
        @param {ip: ip address, port: port number}
        @desc connect to the server/some machine
    2. close:
        @desc close the connection
    3. send:
        @param {frame: the video frame}
        @desc send the frame to server/some machine
    """
    def connect(self, ip, port, protocol):
        """ the network functionalities
        connect:
            @param {ip: ip address, port: port number}
            @desc connect to the server/some machine
        """
        ns = NetworkSelector(protocol)
        self.protocol = protocol
        if "socket" == protocol:
            self.socket = ns.createSocket()
            self.socket.connect((ip, port))
        elif "mqttPub" == protocol:
            self.socket = ns.createPublisher()
            self.socket.connect(ip, port)
        logging.info("succeed to connect to {}:{}".format(ip, port))

    def close(self):
        """ the network functionalities
        close:
            @desc close the connection
        """
        if "socket" == self.protocol:
            self.socket.close()
        elif "mqttPub" == self.protocol:
            self.socket.disconnect()
        logging.info("close the connection")

    @dispatch(bytes)
    def sendall(self, frame):
        """ the network functionalities
        sendall:
            @param {frame: the video frame}
            @desc send the frame to server/some machine
        """
        self.socket.sendall(frame)

    @dispatch(str, bytes)
    def sendall(self, topic, frame):
        """ the network functionalities for tcp socket
        send:
            @desc send the event to server/some machine
            @param {topic: the topic of mqtt}
        """
        self.socket.publish(topic, frame)
