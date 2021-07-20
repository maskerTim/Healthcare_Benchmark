import logging
import networks.socket.client as socketClient
import cv2

class Video:
    """ Interface of video"""
    def __init__(self):
        self.ID = None
        self.ip = ""
        self.cap = None
        self.port = 0
        self.socket = None

    """ monitor the video streaming"""
    def open(self, ID, type, filepath):
        self.ID = ID
        self.openVideoFile(filepath)
        print('hello')
        return self.cap

    def openVideoFile(self, filepath):
        # open the video file
        print(filepath)
        cap = cv2.VideoCapture(filepath)
        # get the position/index of frame in this video
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap = cap

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

    def sendall(self, frame):
        self.socket.sendall(frame)