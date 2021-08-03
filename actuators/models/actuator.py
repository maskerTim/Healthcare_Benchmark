import logging
import threading
from networks.networkSelector import NetworkSelector

class Actuator:
    """ Abstract class of actuator """
    def __init__(self):
        self.ip = ""
        self.name = ""
        self.port = 0
        self.socket = None
        self.on_connect = None
        self.on_message = None
        self.protocol = None

    def prepare(self, threadManager):
        """add actuator to thread manager"""
        threadManager.append(threading.Thread(target=self.do))
        logging.info("The {} is added in thread list.".format(self.__class__))

    def do(self):
        """take the action"""
        pass

    def setOnConnect(self, connectfunc):
        self.on_connect = connectfunc

    def setOnMessage(self, messagefunc):
        self.on_message = messagefunc

    def connect(self, ip, port, protocol="socket"):
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
        elif "mqttSub" == protocol:
            self.socket = ns.createSubscriber()
            self.socket.on_connect = self.on_connect
            self.socket.on_message = self.on_message
            self.socket.connect(ip, port)
            self.socket.loop_start()

    def close(self):
        """ the network functionalities
        close:
            @desc close the connection
        """
        if "socket" == self.protocol:
            self.socket.close()
        elif "mqttSub" == self.protocol:
            self.socket.loop_stop()
            self.socket.disconnect()