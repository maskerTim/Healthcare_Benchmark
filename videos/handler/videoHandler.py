import threading

from ..videoFactory import VideoFactory
import logging
import time
import pickle
import struct
import datetime
import cv2
import logging
from multipledispatch import dispatch
from resources.resource import resources_configs

class VideoHandler:
    # config the classifier model for detecting car
    cars_cascade = cv2.CascadeClassifier(resources_configs["models"]()[0])

    def __init__(self, video="CAM"):
        """ Create some video for healthcare by factory and Operate it """
        self.videoHandler = VideoFactory(video)

    """ @Deprecated Code, later will clean it"""
    # """ Open the video and Record it"""
    # def openAndRecordVideo(self, file, type="file"):
    #     start = datetime.datetime.now()
    #     logging.info("open the video...")
    #     cap = self.videoHandler.open(file, type)
    #     logging.info("record the video...")
    #     try:
    #         while True:
    #             flag, frame = cap.read()
    #             if flag:
    #                 frame = pickle.dumps(frame)
    #                 p = struct.pack('I', len(frame))
    #                 frame = p + frame
    #                 #self.videoHandler.recordVideo(frame)
    #             # break down the recording video
    #             end = datetime.datetime.now()
    #             if (end-start).seconds > 30:
    #                 break
    #     except Exception as e:
    #         logging.error(e)
    #     logging.info("finish to record")

    @classmethod
    def open(cls, filepath):
        """ open the video
        @param {filepath: the file path}
        @return the video capture IO handler
        """
        return cv2.VideoCapture(filepath)

    @classmethod
    def detectCar(cls, frame):
        """ detect the car per video frame
        @param {frame: the video frame}
        @return the number of car in this frame
        """
        car_count = 0
        cars = cls.cars_cascade.detectMultiScale(frame, 1.15, 4)
        for _ in cars:
            car_count+=1
        return car_count

    def connectTo(self, ip, port, protocol="socket"):
        """ Network Functionalities
        connectTo:
            @param {ip: ip address, port: port number}
            @desc connect to the remote server/host
            @err {...}
        """
        try:
            self.videoHandler.setID(threading.get_ident())
            self.videoHandler.connect(ip, port, protocol)
        except Exception as e:
            logging.error("Error: {}".format(e))

    @dispatch(bytes)
    def sendAll(self, frame):
        """ Network Functionalities
        sendAll:
            @param {frame: the video frame}
            @desc send the video frame
        """
        self.videoHandler.sendall(frame)

    @dispatch(str, bytes)
    def sendAll(self, topic, frame):
        """ Network Functionalities
        sendAll:
            @param {frame: the video frame}
            @desc send the video frame
        """
        self.videoHandler.sendall(topic, frame)
        logging.info("publish")

    def close(self):
        """ Network Functionalities
        close:
            @desc close the connection
        """
        self.videoHandler.close()

    """ @Deprecated Code, later will clean it"""
    # """ Play the video """
    # def play(self, ip, port):
    #     try:
    #         # set process ID as identification
    #         self.videoHandler.setID(threading.get_ident())
    #         # connect the server/host
    #         self.videoHandler.connect(ip, port)
    #         # play the video
    #         for f in self.videoHandler.frames:
    #             self.videoHandler.sendall(f)
    #     except Exception as e:
    #         logging.error("Error: {}".format(e))
    #     finally:
    #         time.sleep(3)
    #         self.videoHandler.close()
    #         logging.info("Video is closed...")