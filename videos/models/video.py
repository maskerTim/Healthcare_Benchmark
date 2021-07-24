import logging
import networks.socket.client as socketClient
import cv2

class Video:
    """ Interface of video"""
    def __init__(self):
        self.ID = None
        self.ip = ""
        self.port = 0
        self.cap = None
        self.socket = None
        self.frames = []

    def setID(self, ID):
        """ Set the Identification
        @param {ID: the identification of video instance}
        """
        self.ID = ID


    """ @Deprecated Code, later will clean it """
    # """ open the video streaming"""
    # def open(self, filepath, type):
    #     self.openVideoFile(filepath)
    #     return self.cap

    def openVideoFile(self, filepath):
        """ open the video file
        @param {filepath: the path of video file}
        """
        # open the video file
        cap = cv2.VideoCapture(filepath)
        # get the position/index of frame in this video
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap = cap

    """ @Deprecated Code, later will clean it """
    # def recordVideo(self, frame):
    #     self.frames.append(frame)

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
    def connect(self, ip, port):
        """ the network functionalities
        connect:
            @param {ip: ip address, port: port number}
            @desc connect to the server/some machine
        """
        self.socket = socketClient.createSocket()
        self.socket.connect((ip, port))
        logging.info("succeed to connect to {}:{}".format(ip, port))

    def close(self):
        """ the network functionalities
        close:
            @desc close the connection
        """
        self.socket.close()
        logging.info("close the connection")

    def sendall(self, frame):
        """ the network functionalities
        sendall:
            @param {frame: the video frame}
            @desc send the frame to server/some machine
        """
        self.socket.sendall(frame)