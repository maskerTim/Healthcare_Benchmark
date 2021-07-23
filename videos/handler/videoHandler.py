import threading

from ..videoFactory import VideoFactory
import logging
import time
import pickle
import struct
import datetime
import cv2
import logging
from resources.resource import resources_configs

class VideoHandler:
    cars_cascade = cv2.CascadeClassifier(resources_configs["models"]()[0])
    """
    Create some video for healthcare by factory and Operate it
    """
    def __init__(self, video="CAM"):
        self.videoHandler = VideoFactory(video)

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

    """ open the video """
    @classmethod
    def open(cls, filepath):
        return cv2.VideoCapture(filepath)

    """ detect the car per video frame """
    @classmethod
    def detectCar(cls, frame):
        car_count = 0
        cars = cls.cars_cascade.detectMultiScale(frame, 1.15, 4)
        for _ in cars:
            car_count+=1
        return car_count

    """ Network Functionalities """
    def connectTo(self, ip, port):
        try:
            self.videoHandler.setID(threading.get_ident())
            self.videoHandler.connect(ip, port)
        except Exception as e:
            logging.error("Error: {}".format(e))

    def sendAll(self, frame):
        self.videoHandler.sendall(frame)

    def close(self):
        self.videoHandler.close()

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